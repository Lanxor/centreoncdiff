#!/usr/bin/env python3

import os
import sys
import argparse
import logging
import glob
import json
import yaml

import centreoncdiff.log
from .parser import parse_export
from .centreon.Aclaction import Aclaction
from .centreon.Aclgroup import Aclgroup
from .centreon.Aclmenu import Aclmenu

DEFAULT_CENTREON_CONFIG_DIRECTORY = 'conf/centreon'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='centreon-configurator',
        description='Generate and apply configuration to a Centreon server')
    parser.add_argument('-c', '--config',
                        type=str,
                        default=DEFAULT_CENTREON_CONFIG_DIRECTORY)
    parser.add_argument('-d', '--debug',
                        action='store_true')
    args = parser.parse_args()

    # initialise logging configuration
    centreoncdiff.log.setup(args.debug)
    logging.debug(f'Values of parser : {args}')

    currentConfiguration = None

    # Mode diff enabled if export is provided in stdin
    if args.input:
        logging.info('Diff mode enabled. Start to read stdin.')
        currentConfiguration = parse_export(sys.stdin.read())
        logging.info('Reading completed.')

    # parse all centreon configuration yml files
    logging.info('Start to compile all centreon .yml configuration files.')
    configuration = []
    if os.path.isdir(args.config):
        searchFilter = f"{args.config}/**/*yml"
        logging.debug("Glob search: {0}".format(searchFilter))
        for filePath in glob.iglob(searchFilter, recursive=True):
            with open(filePath, 'rt') as configFile:
                try:
                    configuration += yaml.safe_load_all(configFile)
                    logging.debug(configuration)
                except yaml.YAMLError:
                    logging.exception(
                        f'An error occure when reading the following file {filePath}. Is it in the right format?')
    elif os.path.isfile(args.config):
        filePath = args.config
        with open(filePath, 'rt') as configFile:
            try:
                configuration += yaml.safe_load_all(configFile)
            except yaml.YAMLError:
                logging.exception(
                    f'An error occure when reading the following file {filePath}. Is it in the right format?')
    logging.info('Configuration compilation complete.')

    logging.info('Start to generate configuration.')
    for centreonObjects in configuration:
        if isinstance(centreonObjects, list):
            for centreonObject in centreonObjects:
                logging.debug(json.dumps(centreonObject, indent=2))
                currentCentreonObject = None
                if 'object' in centreonObject and centreonObject['object'].upper() == 'ACLACTION':
                    Aclaction.construct(centreonObject).generate(currentCentreonObject)
                if 'object' in centreonObject and centreonObject['object'].upper() == 'ACLGROUP':
                    Aclgroup.construct(centreonObject).generate(currentCentreonObject)
                if 'object' in centreonObject and centreonObject['object'].upper() == 'ACLMENU':
                    Aclmenu.construct(centreonObject).generate(currentCentreonObject)
    logging.info('Configuration generation is completed.')

    sys.exit(0)
