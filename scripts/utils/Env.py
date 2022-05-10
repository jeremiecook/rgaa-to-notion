from utils.Singleton import Singleton
import os
from os.path import join, dirname
from dotenv import load_dotenv


class Env(Singleton):

    def __init__(self, file='.env'):
        self.path = join(dirname(dirname(__file__)), file)
        if not os.path.exists(self.path):
            print("❌ Error: cannot find {path} file.".format(path=self.path))
            quit()

        # Récupérer les variables d'environnement
        load_dotenv(self.path)

    def exists(self, param):
        return os.getenv(param)

    def get(self, param):
        if not os.getenv(param):
            print("❌ Error: {param} missing in {file}.".format(
                param=param, file=self.path))
            quit()

        return os.getenv(param)
