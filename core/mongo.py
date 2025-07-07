#Copyright @ISmartDevs
#Channel t.me/TheSmartDev

from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import urlparse, parse_qs
from utils import LOGGER
from config import MONGO_URL

LOGGER.info("Creating MONGO_CLIENT From MONGO_URL")

try:
    parsed = urlparse(MONGO_URL)
    query_params = parse_qs(parsed.query)
    db_name = query_params.get("appName", [None])[0]

    if not db_name:
        raise ValueError("No database name found in MONGO_URL (missing 'appName' query param)")

    MONGO_CLIENT = AsyncIOMotorClient(MONGO_URL)
    db = MONGO_CLIENT.get_database(db_name)
    authusers_collection = db["authusers"]
    logindb_collection = db["logindb"]
    numbersdb_collection = db["numbersdb"]

    LOGGER.info(f"MONGO_CLIENT Created Successfully!")
except Exception as e:
    LOGGER.error(f"Failed to create MONGO_CLIENT: {e}")
    raise