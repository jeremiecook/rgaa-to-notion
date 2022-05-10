"""
Export all criteria to Notion

Usage:
	main.py
	main.py [--dry] [-e ENV]
	main.py -h|--help
	main.py -v|--version

Options:
	-h --help           Show this screen
	-v --version        Show version
	-e ENV --env=ENV    Use given file for Airtable configuration [default: .env]
"""

# coding: utf-8
from docopt import docopt
import os

from utils.Log import Log
from utils.Env import Env
log = Log()
env = Env()


class ExportToNotion:

    def __init__(self):
        pass

    def get_criteria(self, path):
        for root, subdirs, files in os.walk(path):
            print(root, subdirs, files)
        print("criteria")

    def add_criteria(self):
        pass


if __name__ == '__main__':

    arguments = docopt(__doc__, version='1.0')
    #dry = arguments['--dry']
    #env = arguments['ENV'] or ".env"

    if(env.exists('NOTION_RGAA_BASE_ID')):
        notion = ExportToNotion()
        notion.get_criteria("../src/rgaa/criteres")
