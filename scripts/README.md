# Synchronisation des données beta.gouv.fr sur Airtable

## Installation

### Dépendances
```
pip3 install -r requirements.txt
```

Pour mettre à jour les librairies utilisées dans le projet dans requirements.txt:
```
pip3 install pipreqs
pipreqs . --force
```

### Configuration

Créer un fichier `.env`
```
AIRTABLE_API_KEY={clé, trouvable dans account : personnal api key}

AIRTABLE_STARTUPS_BASE_ID={identifiant de la base startups, trouvable dans help > API Documentation}
AIRTABLE_STARTUPS_TABLE={Nom de la table contenant les startups}

AIRTABLE_DESIGNERS_BASE_ID={identifiant de la base designers, trouvable dans help > API Documentation}

MATTERMOST_URL={L'adresse de l'instance Mattermost}
MATTERMOST_KEY={L'identifiant du hook créé dans Mattermost}
```

Par exemple : 
```
AIRTABLE_API_KEY=keyXXXXXXXX

AIRTABLE_STARTUPS_BASE_ID=appXXXXXXXX
AIRTABLE_STARTUPS_TABLE=Startups d'État

AIRTABLE_DESIGNERS_BASE_ID=appXXXXXXXX

MATTERMOST_URL=https://mattermost.server.com
MATTERMOST_KEY=XXXXXXXXXX

```

## Lancer le programme

```
# Voir la liste des SE qui ont changé
python3 main.py

# Mettre à jour les SE
python3 main.py -w

# Mettre à jour les SE de l'environnement access
python3 main.py -w -e .access
```
