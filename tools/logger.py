import logging

logging.basicConfig(
    filename="logs/email.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_message(message):
    logging.info(message)