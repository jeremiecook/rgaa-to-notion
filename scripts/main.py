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
from utils.Log import Log
from utils.Env import Env
from api.Notion import Notion
from api.RGAA import Rules
log = Log()
env = Env()


notion = Notion('APIKEY', 'BASERULES', 'BASETESTS')


if __name__ == '__main__':

    arguments = docopt(__doc__, version='1.0')
    #dry = arguments['--dry']
    #env = arguments['ENV'] or ".env"

    if (not env.exists('NOTION_RGAA_BASE_ID')):
        raise Exception("Vous devez fournir un identifiant de base Notion")

    #e = ExportToNotion()
    #e.export_to_notion("../src/rgaa/criteres")

    rgaa = Rules()
    rules = rgaa.all_rules()
    categories = rgaa.all_categories()

    #print(rules)
    #print(list(rules.values()))
    for rule in list(rules.values())[1:10]:       
        id = notion.create_rule(rule)

        for test in rule.get('tests'):
            notion.create_test(id, test)
            pass