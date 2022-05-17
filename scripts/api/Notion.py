import json
import requests


class Notion:

    def __init__(self, token, base_rules, base_tests):
        self.token = token
        self.base_rules = base_rules
        self.base_tests = base_tests

        self.headers = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-02-22"
        }
        
    def create_rule(self, content):

        url = 'https://api.notion.com/v1/pages'

        data = {
            "parent": { "database_id": self.base_rules },
            "properties": {
                'title': {
                    'title': [
                        {
                            "text": {"content" :content.get('title')}
                        }, 
                    ]   
                },
                'Identifiant': {
                    'number': float(content.get('id'))
                },
                'Thème': {
                    'select': {
                        'name': content.get('category')
                    }
                },
                'Statut': {
                    'select': {
                        'name': "À auditer"
                    }
                }
            }
        }
    
        data = json.dumps(data)
        res = requests.request("POST", url, headers=self.headers, data=data)
        res = json.loads(res.text)
        #print(res.text)
        
        return res.get('id')
        #return res.text.get('id')
        #print(res.status_code)
        #print(res.text)


    def create_test (self, rule_id, content):
        url = 'https://api.notion.com/v1/pages'

        data = {
            "parent": { "database_id": self.base_tests },
            "properties": {
                'title': {
                    'title': [
                        {
                            "text": {"content" :content.get('title')}
                        }, 
                    ]   
                },
                'Critère': {
                    "relation": [
                        {
                            "id": rule_id
                        }
                    ]                   
                }
            }
        }
    
        data = json.dumps(data)
        res = requests.request("POST", url, headers=self.headers, data=data)
        res = json.loads(res.text)
        return res.get('id')