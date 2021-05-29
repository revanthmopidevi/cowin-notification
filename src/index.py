from decouple import config
import time

from telegram.telegram import teleMessage
from cowin.cowin import *

# Telegram Message Details
API_ID = config('API_ID')
API_HASH = config('API_HASH')
PHONE = config('PHONE')
# Vaccination Location Details
STATE = config('STATE')
DISTRICT = config('DISTRICT')

to = ['+919182787502', '+917013385235', '+919182920872', '+917207761909', '+919100562917']

while (True):
    time.sleep(1)
    if (slots(districtID(DISTRICT, stateID(STATE)))):
        teleMessage(API_ID, API_HASH, PHONE, to, f'Slot Available on https://www.cowin.gov.in/home for 18+ dose 1')