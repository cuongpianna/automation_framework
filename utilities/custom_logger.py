import sys
import os
import logging
from logging import handlers
import inspect


def custom_logger(log_level):
    # Get the name of class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)
    # file_handle = handlers.RotatingFileHandler(filename='logs/automation.log', mode='a', encoding='utf-8', maxBytes=10,
    #                                            backupCount=10)
    file_handle = logging.FileHandler('logs/automation.log', mode='a', encoding='utf-8')
    file_handle.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handle.setFormatter(formatter)
    logger.addHandler(file_handle)
    return logger


# def custom_logger(log_level):
#     # Get the name of class / method from where this method is called
#     logging.basicConfig(
#         handlers=[handlers.RotatingFileHandler(filename='logs/test.log', maxBytes=500,
#                                                backupCount=1, mode='a', encoding='utf-8')],
#         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#         datefmt='%m/%d/%Y %I:%M:%S %p',
#     )
#     logger_name = inspect.stack()[1][3]
#     logger = logging.getLogger(logger_name)
#     # By default, log all messages
#     logger.setLevel(logging.DEBUG)
    # file_handle = handlers.RotatingFileHandler(filename='logs/automation.log', mode='a', encoding='utf-8', maxBytes=10,
    #                                            backupCount=10)
    # file_handle = logging.FileHandler('logs/automation.log', mode='a', encoding='utf-8')
    # file_handle.setLevel(log_level)

    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #                               datefmt='%m/%d/%Y %I:%M:%S %p')
    #
    # file_handle.setFormatter(formatter)
    # logger.addHandler(file_handle)
    # logging.basicConfig(filename='logs/automation.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #                     datefmt='%m/%d/%Y %I:%M:%S %p')
    # return logger


def custom_logger(log_level):
    """
    Configuring logger
    """
    # setup formatter
    logger_name = inspect.stack()[1][3]

    LOG_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')

    logger = logging.getLogger(logger_name)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    # config logging to file
    info_log = os.path.join(LOG_FOLDER, "info.log")
    info_file_handler = handlers.RotatingFileHandler(
        info_log,
        maxBytes=50000,
        backupCount=10,
        encoding='utf-8',
        delay=True
    )
    info_file_handler.setLevel(logging.DEBUG)
    info_file_handler.setFormatter(formatter)
    logger.addHandler(info_file_handler)

    # config log console
    # handler_console = logging.StreamHandler(stream=sys.stdout)
    # handler_console.setFormatter(formatter)
    # handler_console.setLevel(logging.DEBUG)
    # logger.addHandler(handler_console)

    # set proper log level
    logger.setLevel(logging.DEBUG)

    # unify log format for all handers
    for h in logger.handlers:
        h.setFormatter(formatter)
    return logger

