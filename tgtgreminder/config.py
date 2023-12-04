from os import environ
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = environ.get('ACCESS_TOKEN')
REFRESH_TOKEN = environ.get('REFRESH_TOKEN')
USER_ID = int(environ.get('USER_ID'))
COOKIE = environ.get('COOKIE')
