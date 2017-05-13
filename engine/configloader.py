from json import loads, dumps
from json.decoder import JSONDecodeError
import base64

def boolean(s):
    s = str(s)
    if s.lower() == "false":
        return False
    return True

class ConfigObject:
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

class ConfigArgument:
    def __init__(self, name, data_type, default, desc=None):
        self.name = name
        self.type = data_type
        self.default = default
        self.desc = desc


class BaseConfig:
    def __init__(self, path, defaults):
        self.path = path
        self.defaults = defaults
        self.config = None

    def load_config(self):
        return self

    def get_config(self):
        return ConfigObject(self.config)

    def __setitem__(self, key, value):
        self.config[key] = value


class JsonSave(BaseConfig):
    def load_config(self):
        with open(self.path, "a+") as f:
            f.seek(0)
            try:
                self.config = loads(f.read())
            except JSONDecodeError:
                self.config = dict()
            for val in self.defaults:
                if val.name in self.config:
                    self.config[val.name] = val.type(self.config[val.name])
                else:
                    self.config[val.name] = val.type(val.default)
        self.save_config()
        return self

    def save_config(self):
        with open(self.path, "w+") as f:
            f.write(dumps(self.config))
        return self


class EncodedSave(JsonSave):
    def save_config(self):
        with open(self.path, "w+") as f:
            f.write(base64.b64encode(dumps(self.config).encode("utf-8")).decode("utf-8"))
        return self

    def load_config(self):
        with open(self.path, "a+") as f:
            f.seek(0)
            text = base64.b64decode(f.read())
            try:
                self.config = loads(text)
            except JSONDecodeError:
                self.config = dict()
            for val in self.defaults:
                if val.name in self.config:
                    self.config[val.name] = val.type(self.config[val.name])
                else:
                    self.config[val.name] = val.type(val.default)
        self.save_config()
        return self
