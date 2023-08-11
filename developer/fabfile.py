import os
from fabric.contrib.files import sed
from fabric.api import env, local, run

# directorio base
abs_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env.hosts = ['44.201.178.214'] 


