import inspect
import logging
from pathlib import Path


def get_logger(loglevel = logging.DEBUG):
    #set class/method name
    logger_name = inspect.stack()[1][3]
    
    #create logger and set level
    logger = logging.getLogger(logger_name)
    logger.setLevel(loglevel)
    
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    #create file handler
    file_handler = logging.FileHandler("logs/automation.log")
    
    #formatter
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    
    #add formatter to file handling
    file_handler.setFormatter(formatter)
    
    #add file_handler to logger
    logger.addHandler(file_handler)
    
    return logger
    