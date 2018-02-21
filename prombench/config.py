"""
Acquire runtime configuration from environment variables (etc).
"""

import os
import yaml


def logfile_path(jsonfmt=False, debug=False):
    """
    Returns the a logfileconf path following this rules:
      - conf/logging_debug_json.conf # jsonfmt=true,  debug=true
      - conf/logging_json.conf       # jsonfmt=true,  debug=false
      - conf/logging_debug.conf      # jsonfmt=false, debug=true
      - conf/logging.conf            # jsonfmt=false, debug=false
    Can be parametrized via envvars: JSONLOG=true, DEBUGLOG=true
  """
    _json = ""
    _debug = ""

    if jsonfmt or os.getenv('JSONLOG', 'false').lower() == 'true':
        _json = "_json"

    if debug or os.getenv('DEBUGLOG', 'false').lower() == 'true':
        _debug = "_debug"

    return os.path.join(PROMBENCH_CONF_DIR, "logging%s%s.conf" % (_debug,
                                                                  _json))


def getenv(name, default=None, convert=str):
    """
    Fetch variables from environment and convert to given type.

    Python's `os.getenv` returns string and requires string default.
    This allows for varying types to be interpolated from the environment.
    """

    # because os.getenv requires string default.
    internal_default = "(none)"
    val = os.getenv(name, internal_default)

    if val == internal_default:
        return default

    if callable(convert):
        return convert(val)

    return val


def envbool(value: str):
    return value and (value.lower() in ('1', 'true'))


APP_ENVIRON = getenv("APP_ENV", "development")

PROMBENCH_API = getenv("PROMBENCH_API", "https://prombench.example.com")
PROMBENCH_SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMBENCH_ROOT_DIR = os.path.abspath(os.path.join(PROMBENCH_SOURCE_DIR, "../"))
PROMBENCH_CONF_DIR = os.getenv("PROMBENCH_CONF_DIR",
                               os.path.join(PROMBENCH_ROOT_DIR, "conf/"))
PROMBENCH_CONF_FILE = os.getenv("PROMBENCH_CONF_FILE", None)


class PrombenchConfig(object):
    """
    """

    def __init__(self, defaults=None, confpath=None):
        self.settings = {
            'prombench': {
                'debug': False,
                'env': APP_ENVIRON,
                'url': PROMBENCH_API,
            },
        }
        if defaults:
            self.load_conf(defaults)

        if confpath:
            self.load_conffile(confpath)

    @property
    def gitlab(self):
        return self.settings['gitlab']

    @property
    def github(self):
        return self.settings['github']

    @property
    def prombench(self):
        return self.settings['prombench']

    def reload(self, confpath, inplace=False):
        if inplace:
            instance = self
            instance.load_conffile(confpath)
        else:
            instance = PrombenchConfig(defaults=self.settings,
                                       confpath=confpath)

        return instance

    def load_conf(self, conf):
        for key, v in conf.items():
            self.settings[key].update(v)

    def load_conffile(self, confpath):
        with open(confpath, 'r') as conffile:
            self.load_conf(yaml.load(conffile.read()))


GCONFIG = PrombenchConfig(confpath=PROMBENCH_CONF_FILE)
