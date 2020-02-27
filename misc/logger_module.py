#!/usr/bin/env python
# coding: utf-8

"""
A CodeSnippet for a Logging Module
"""
import logging
import logging.config
import os
from datetime import datetime


def start_logging():
    '''A function to start the logging.
    return: logger
    '''
    if os.path.exists('./logs'):
        pass
    else:
        os.mkdir('./logs')

    logging_cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.cfg')
    logfile = os.path.join('./logs', f'logfile-{datetime.now().strftime("%Y-%m-%d")}.log')
    logging.config.fileConfig(logging_cfg_file, \
        disable_existing_loggers=False, \
        defaults={'logfilename' : logfile})
    logger = logging.getLogger()
    return logger
