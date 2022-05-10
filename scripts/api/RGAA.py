from contextlib import nullcontext
from datetime import datetime
import json
import requests


class BetaGouvStartups:

    def __init__(self):
        self.url = "https://beta.gouv.fr/api/v2.3/startups.json"
        self.incubators = {}
        self.startups = {}

    def all(self):
        # Récupérer les données de l'API
        startups = json.loads(requests.get(self.url).text)

        self.incubators = {i.get('id'): i.get("attributes").get(
            "title") for i in startups.get("included")}

        # Load result in a nice dict
        for se in startups.get('data'):
            incubator_id = "/incubators/{name}".format(name=se.get(
                'relationships').get('incubator').get('data').get('id'))

            self.startups[se.get('id')] = dict(
                name=se.get('attributes').get('name'),
                phase=se.get('attributes').get('phases')[-1].get('name'),
                mission=se.get('attributes').get('pitch'),
                incubator=self.incubators.get(incubator_id),
                statistiques=se.get("attributes").get('stats_url'),
                start=se.get('attributes').get('phases')[0].get('start'),
            )

        return self.startups

    def get(self, id):
        return self.startups.get(id)


class BetaGouvMembers:
    # Beta.gouv.fr community

    def __init__(self):
        self.url = "https://beta.gouv.fr/api/v2.3/authors.json"
        self.members = {}

        data = json.loads(requests.get(self.url).text)

        for member in data:
            self.members[member.get('id')] = dict(
                fullname=member.get('fullname'),
                role=member.get('role'),
                domain=member.get('domaine'),
                startups=member.get('startups'),
                start=self.__start(member.get('missions')),
                end=self.__end(member.get('missions')),
                status=self.__status(member.get('missions')),
            )

    def all(self):
        return self.members

    def designers(self):
        # List all designers
        designers = {}
        for id, member in self.members.items():
            if ("Design" == member['domain']):
                designers[id] = member
        return designers

    def __start(self, missions):
        return missions[0].get('start')

    def __end(self, missions):
        return missions[-1].get('end')

    def __status(self, missions):
        # Define if a member is currently working for beta or an alumni
        end = datetime.strptime(self.__end(missions), '%Y-%m-%d')
        status = 'En cours' if (end > datetime.today()) else 'Alumni'
        return status

    def get(self, id):
        return self.members[id]
