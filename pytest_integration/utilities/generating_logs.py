import logging

# generation log to log file - rough example
# logging.basicConfig(filename="../Logs/logfile.log", format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
#
# log = logging.getLogger()
#
# log.info("This is our 1 log")

def log():
    logging.basicConfig(filename="logfile.log", format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
    logger = logging.getLogger()
    print("I'm inside")
    return logger

# example doesn't work with test_appium_allure_screen_on_failure.py
logger = log()
logger.info("12324")