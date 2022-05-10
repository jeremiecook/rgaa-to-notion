from airtable import airtable


class Airtable:

    def __init__(self, base, api_key, table, fields, dry=False):
        self.api = airtable.Airtable(base, api_key)
        self.id = 'ID'  # airtable field for id
        self.table = table
        self.fields = fields  # field to get from airtable
        self.dry = dry

    def all(self):
        # Récupère tous les enregistrements Airtable...
        results = {}
        records = {}
        data = self.api.get(self.table, fields=self.fields)
        records = data['records']

        # ... en plusieurs fois si les enregistrements sont trop nombreux
        while data.get('offset'):
            data = self.api.get(
                self.table,
                fields=self.fields,
                offset=data.get('offset')
            )
            records += data['records']

        # Renvoie les résultats dans un beau dictionnaire
        for r in records:
            entry = dict()

            for id, field in self.fields.items():
                entry[id] = r.get("fields").get(field)
                entry['airtable_id'] = r.get("id")

            results[r.get("fields").get("ID")] = entry

        return results

    def get(self, id, field):
        data = self.api.get(self.table, fields=fields)

    def create(self, id, content):
        entry = {'ID': id}

        # Formater le contenu pour Airtable
        for id, key in self.fields.items():
            if id in content:
                # remplace la clé par un nom de champ Airtable
                entry[key] = content[id]

        try:
            if not self.dry:
                self.api.create(self.table, entry)

        except airtable.AirtableError as err:
            print(
                "❌ Error: cannot create startup {id}:" . format(id=id))
            print(err)

    def update(self, airtable_id, data):
        entry = {}

        # Formater le contenu pour Airtable
        for id, key in self.fields.items():
            if id in data:
                # remplace la clé par un nom de champ Airtable
                entry[key] = data[id]

        try:
            if not self.dry:
                self.api.update(self.table, airtable_id, entry)

        except airtable.AirtableError as err:
            print("❌ Error: cannot update startup {id}:".format(
                id=id))
            print(err)
