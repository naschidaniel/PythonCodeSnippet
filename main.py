#!/usr/bin/env python
# coding: utf-8

"""
Just a small PythonCodeSnippet with an argparse and logging module.
"""
import json
from misc import argparse_module
from misc import logger_module

def main():
    """Main function of the program.
    """
    # Logging
    logger = logger_module.start_logging()
    logger.info('The program PythonCodeSnippet was started.')

    # Read availableSettings.json file
    with open('availableSettings.json') as f:
        available_settings = json.load(f)

    # Argparse
    arguments = argparse_module.get_arguments(available_settings, logger)

    name = arguments['name']
    settings = arguments['settings']

    print('{} {}!'.format(settings['greeting'], name))

    logger.info('The program pythonCodeSnippet has run successfully.')

if __name__ == '__main__':
    main()
