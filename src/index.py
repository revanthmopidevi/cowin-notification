from decouple import config

from telegram.telegram import teleMessage
from cowin.cowin import *

# Telegram Message Details
API_ID = config('API_ID')
API_HASH = config('API_HASH')
PHONE = config('PHONE')
TO = config('TO')
# Vaccination Location Details
STATE = config('STATE')
DISTRICT = config('DISTRICT')

while (True):
    if (slots(districtID(DISTRICT, stateID(STATE)))):
        teleMessage(API_ID, API_HASH, PHONE, TO, 'Slot Available')