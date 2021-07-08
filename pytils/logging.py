import logging
import sys


def logger(level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)
    return logger


def formatter():
    msg_format = '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
    return logging.Formatter(msg_format)


def file_handler(formatter, name='application'):
    handler = logging.FileHandler(f'{name}.log')
    handler.setFormatter(formatter)
    return handler


def console_handler(formatter):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    return handler


log_level = logging.INFO
logger = logger(log_level)
formatter = formatter()

file = file_handler(formatter)
logger.addHandler(file)

console = console_handler(formatter)
logger.addHandler(console)
