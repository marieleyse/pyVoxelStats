import os, configparser
import Util.Params.pyVSParams


class pyVoxelStats:
    def __init__(self):
        self.config = self.check_config()

    def check_config(self, config_path='{0}/.pyVS/pyVSParams.ini'.format(os.path.expanduser('~'))):
        if os.path.exists(config_path):
            cf = configparser.ConfigParser()
            cf.read(config_path)
            return cf
        else:
            config_dict = Util.Params.pyVSParams.config_dict
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            cf = configparser.ConfigParser()
            for k in config_dict.keys():
                cf[k] = config_dict[k]
            with open(config_path, 'w') as configfile:
                cf.write(configfile)
            return cf
