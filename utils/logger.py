import logging

def setup_logger():
    logger = logging.getLogger("appium-test")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger