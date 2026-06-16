import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

log_dir = "logs"

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_handler = logging.FileHandler(
    os.path.join(log_dir, "test.log"),
    encoding="utf-8"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)