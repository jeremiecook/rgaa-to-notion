from contextlib import nullcontext
from datetime import datetime
import json
import requests
import os
from markdown import Markdown
from io import StringIO
from pathlib import Path

# https://stackoverflow.com/questions/761824/python-how-to-convert-markdown-formatted-text-to-text
def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)


class Rules:

    def __init__(self):
        self.url = "https://beta.gouv.fr/api/v2.3/startups.json"
        self.categories = {}
        self.rules = {}

        self.__load_categories()
        self.__load_rules()


    def __load_categories(self):
        path = '../src/_data/themes.json'
        f = open(path)
        self.categories = json.load(f)

    def __load_rules(self):
        path = '../src/rgaa/criteres/'
        rules={}
        for root, subdirs, files in os.walk(path):
            for file in files:
                #print(root, file)
                dir = root.rsplit('/', 1)[1] # Dernier élément du chemin, "12.1" ou "tests" par exemple

                # Critère
                if (file == "index.md"): 
                    id = root.rsplit('/', 1)[1] # ie. 12.1
                    category = id.rsplit('.', 1)[0] # ie. 12.1
                    rules[id] = {}

                    data = Path(os.path.join(root, file)).read_text(encoding='utf-8')
                    md = Markdown(extensions = ['meta'])
                    md.convert(data)

                    rules[id]['id'] = id
                    rules[id]['title'] = unmark(md.Meta['title'][0])
                    rules[id]['category'] = self.get_category(category)
                    rules[id]['tests'] = []
                    #print(os.path.join(root, file))

                # Tests
                if (dir == 'tests'):
                    test = {}

                    rule = root.rsplit('/', 2)[1] # ie. 12.1
                    id = file.split('.')[0]


                    data = Path(os.path.join(root, file)).read_text(encoding='utf-8')
                    md = Markdown(extensions = ['meta'])
                    md.convert(data)

                    test['id'] = id
                    test['title'] = unmark(md.Meta['title'][0])

                    rules[rule]['tests'].append(test)
            
        self.rules = rules





    def all_categories(self):
        return self.categories

    def get_category(self, id):
        return self.categories[id]['title']

    def all_rules(self):
        return self.rules


