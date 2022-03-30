import os
from environs import Env

env = Env()
env.read_env()

FILE_PATH = os.environ.get('FILE_PATH')

FILE_NAMES = os.environ.get("FILE_NAMES").split(" ")

PATH_FOR_DOWNLOAD = os.path.join(os.path.expanduser('~'), FILE_PATH)
