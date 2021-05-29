import requests
from datetime import date

headers = {
    "accept": "application/json",
    "Accept-Language": "hi_IN",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

def stateID(state_name):
    states = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states', headers=headers).json()['states']
    for state in states:
        if state['state_name'] == state_name:
            return state['state_id']
    return -1

def districtID(district_name, state_id):
    if state_id == -1:
        return -1
    districts = requests.get(f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}', headers=headers).json()['districts']
    for district in districts:
        if district['district_name'] == district_name:
            return district['district_id']
    return -1

def slots(district_id):
    if district_id == -1:
        return False
    year = date.today().year
    month = date.today().month
    day = date.today().day + 1 
    date_value = f'{day}' + '-' + f'{month}' + '-' + f'{year}'
    slots = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={date_value}', headers=headers).json()['sessions']
    if len(slots) == 0:
        return False
    for slot in slots:
        if slot['min_age_limit'] == 18:
            return True
    return False