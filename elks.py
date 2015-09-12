from urllib.parse import urlencode
from urllib.error import HTTPError
from urllib.request import urlopen, Request
from base64 import b64encode
import os

def b(x):
    return bytes(x, 'utf-8')

def query_api(message, recipient, sender='apini'):
    sms = {
            'from': sender,
            'to': recipient,
            'message': message
            }
    data = urlencode(sms)
    username = os.environ['ELKS_ID']
    secret = os.environ['ELKS_SECRET']
    api_url = "https://api.46elks.com/a1/SMS"
    conn = Request(api_url, b(data))
    auth = b('Basic ') + b64encode(b('%s:%s' % (username, secret)))
    conn.add_header('Authorization', auth)
    response = urlopen(conn)
    return response.read()

def send_url(url, amount, recipient):
    query_api('Apini Payment URL %s' % url, recipient)

def has_payed(payer, recipient):
    query_api('%s has payed' % payer, recipient)

