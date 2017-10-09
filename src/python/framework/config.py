import json
import os


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Config():
    driver = None
    _path_to_resources = "../../../resources/"

    def __init__(self):
        with open(os.path.abspath("{}config.json".format(self._path_to_resources)), "r") as conf:
            self.config = json.load(conf)

        self.explicitly_wait = self.config['main']['explicitlyWaitDelay']

        if sys.platform == 'linux':
            if self.config['main']['language'] == 'ru':
                with open(os.path.abspath("{}localization_ru.json".format(self._path_to_resources)), "r") as lang:
                    self.localization = json.load(lang)

            elif self.config['main']['language'] == 'en':
                with open(os.path.abspath("{}localization_en.json".format(self._path_to_resources)), "r") as lang:
                    self.localization = json.load(lang)
        else:
            from src.resources.localization_ru import localization_ru
            self.localization = localization_ru
