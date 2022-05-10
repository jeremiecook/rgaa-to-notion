from utils.Singleton import Singleton


class Log(Singleton):

    logs = []
    warnings = []

    def info(self, text):
        self.logs.append(text)

    def warning(self, text):
        self.warnings.append('- 🔸 ' + text)

    def print(self):
        for text in self.logs:
            print(text)

        for text in self.warnings:
            print(text)

    def get(self):

        message = ""

        for text in self.logs:
            message += text + "\n"

        for text in self.warnings:
            message += text + "\n"

        return message
