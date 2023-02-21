import os

import pytz

from dotenv import load_dotenv

load_dotenv()

# for scraper
URL = "https://www.com/wp-admin/admin-ajax.php?enrol_total={}"

HEADERS = {
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://www.oxford-royale.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
}

# for google api
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = os.environ.get('*')
NAME_LIST = "*"
CRED_PATH = "*.*"
TOKEN_PATH = '*/*.*'

# time for docker and celery
CURRENT_TIME_ZONE = pytz.timezone("*")

# postgres connection
POSTGRES_CONNECTION_STR = 'postgresql://{}:{}@{}:{}/{}'.format(
    os.environ.get('POSTGRES_USER'), os.environ.get('POSTGRES_PASSWORD'), os.environ.get('POSTGRES_HOST'),
    os.environ.get('POSTGRES_PORT'), os.environ.get('POSTGRES_DB'))
