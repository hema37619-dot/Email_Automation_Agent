import os
import logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/email.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_message(message):
    logging.info(message)
