import os

import dotenv

dotenv.load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
DATABASE_NAME = os.environ["DATABASE_NAME"]

FIEF_BASEURL = os.environ["FIEF_BASEURL"]
FIEF_CLIENT_ID = os.environ["FIEF_CLIENT_ID"]
FIEF_CLIENT_SECRET = os.environ["FIEF_CLIENT_SECRET"]
FIEF_AUTHORIZATION_URL = os.environ["FIEF_AUTHORIZATION_URL"]
FIEF_TOKEN_URL = os.environ["FIEF_TOKEN_URL"]
