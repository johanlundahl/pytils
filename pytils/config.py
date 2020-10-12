import yaml
from box import Box
import sys

def load_config():
    app_name = sys.modules['__main__'].__file__.split('.')[0]
    config_file = '{}.yaml'.format(app_name) 
    with open(config_file, 'r') as stream:
        return yaml.safe_load(stream)
        
cfg = Box(load_config())
