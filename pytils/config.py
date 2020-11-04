import yaml
from box import Box
import sys

def load_config(file_name=None):
	config_file = file_name if file_name != None else get_main_name()
    with open(config_file, 'r') as stream:
        return yaml.safe_load(stream)

def get_main_name():
	app_name = sys.modules['__main__'].__file__.split('.')[0]
    return '{}.yaml'.format(app_name) 
   	
        
cfg = Box(load_config())
