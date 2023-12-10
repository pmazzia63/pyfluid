"""
This module is used to define a logger. This object is used to display
informations in the code or during the simulation.

This module requires `logging` to work.
"""
from typing import Optional
import logging
import sys

from pyfluid import __version__

APP_LOGGER_NAME = f"PyFluid v{__version__} Logs"
BASE_FORMAT = \
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def setup_applevel_logger(logger_name: str = APP_LOGGER_NAME,
                          file_name: Optional[str] = None,
                          log_format: str = BASE_FORMAT,
                          log_level: int = logging.DEBUG,
                          file_log_level: Optional[int] = None
                          ) -> logging.Logger:
    """
    Set up a "root" logger for the app/repository. This function will replace
    base logging logger by one following **logger_name**
    The logger will only write on stdout by default.
    By adding a file path **file_name** it will also create a file and save
    the logs on it.

    :param logger_name: name of the logger to display, defaults to
        APP_LOGGER_NAME
    :type logger_name: Optional[str]
    :param file_name: output file name for logs file (currently handle by
        FileHandler and not RotatingFileHandler), defaults to None
    :type file_name: Optional[str]
    :param log_format: wanted format for the logs
    :type log_format: str
    :param log_level: log level used for stream (and file is file level is None
        )
    :type log_level: Optional[int]
    :param file_log_level: log level used for files
    :type file_log_level: Optional[int]
    :return: a configured logger
    :rtype: Logger
    """
    logger = logging.getLogger(name=logger_name)
    formatter = logging.Formatter(fmt=log_format)
    # base logger level needs to be higher than every handlers
    logger.setLevel(level=logging.DEBUG)
    streamhandler = logging.StreamHandler(stream=sys.stdout)
    streamhandler.setLevel(level=log_level)
    streamhandler.setFormatter(fmt=formatter)
    logger.handlers.clear()
    logger.addHandler(hdlr=streamhandler)
    if file_name:
        if not file_log_level:
            file_log_level = log_level
        filehandler = logging.FileHandler(filename=file_name)
        filehandler.setLevel(level=file_log_level)
        filehandler.setFormatter(formatter)
        logger.addHandler(hdlr=filehandler)
    return logger


def get_logger(module_name: str) -> logging.Logger:
    """
    Get a module level logger (should have been setup at app level before in
    order to follow config and format).

    :param module_name: name of the module usually __name__
    :type module_name: str
    :return: module level logger
    :rtype: Logger
    """
    return logging.getLogger(name=APP_LOGGER_NAME).getChild(suffix=module_name)
