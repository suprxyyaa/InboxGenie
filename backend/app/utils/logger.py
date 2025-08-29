# backend/app/utils/logger.py
import logging
import sys

def setup_logger():
    """
    Configures the application logger.
    """
    logger = logging.getLogger("inbox_genie")
    logger.setLevel(logging.INFO)

    # Create a handler to print logs to the console
    stream_handler = logging.StreamHandler(sys.stdout)
    
    # Create a formatter and set it for the handler
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    stream_handler.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.handlers:
        logger.addHandler(stream_handler)
        
    return logger

log = setup_logger()