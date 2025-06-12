# settings.py

import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables from a .env file (if available)
load_dotenv()

# --- Environment-based Settings ---
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()  # e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = os.getenv("LOG_FILE", "central.log")  # Log file path
LOG_FORMAT = os.getenv("LOG_FORMAT", "[%(asctime)s] [%(levelname)s] %(message)s")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", 10 * 1024 * 1024))  # 10 MB by default
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", 5))  # Keep 5 rotated files

# --- Logging Configuration ---
# Create a central logger for your application
logger = logging.getLogger("centralLogger")
logger.setLevel(LOG_LEVEL)

# Rotating file handler for centralized log storage
file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT
)
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(LOG_LEVEL)
stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(stream_handler)

# Log an initial message to confirm configuration
logger.info("Central logging configured successfully.")

# --- Additional Settings ---
# Add any additional configuration variables or setup here.