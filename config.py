import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(BASE_DIR, 'config.env')
load_dotenv(dotenv_path)

secret_key = os.environ['SECRET_KEY']
username = os.environ['USERNAME']
debug = os.environ['DEBUG']

print(secret_key)
print(username)
print(debug)