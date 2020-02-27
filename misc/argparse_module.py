#!/usr/bin/env python
# coding: utf-8

"""
A CodeSnippet for a argparse with a settings Module
"""

import argparse
import sys

def get_arguments(available_settings, logger):
    '''A function to proceed some parsed Arguments.
    available_settings = dict()
    logger
    return: arguments = dict()
    '''
    parser = argparse.ArgumentParser(description='A simple program with a logging and an argparse module. The goal of this program is to standardize logging and argParse for python.')
    parser.add_argument('-n', '--name', dest="name", \
        help='Type in a name. e.g. Rudi', default='', type=str)
    parser.add_argument('-s', '--settings', dest="settings", \
        help='The settings are regulated in the file availableSettings.json.', \
        default='', type=str)

    options = parser.parse_args()
    print(options)

    logger.debug('options.name: %s', options.name)
    logger.debug('options.settings: %s', options.settings)

    if options.settings in available_settings.keys():
        settings = available_settings[options.settings]
    else:
        logger.error('The settings cannot be found in the settings file.')
        sys.exit(1)

    arguments = {
        'name': options.name,
        'settings': settings
    }

    return arguments
