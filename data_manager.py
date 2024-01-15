import os

import requests
from pprint import pprint
APY_KEY = os.environ['APY_KEY_SHEETS']
API_URL = f"https://api.sheety.co/{APY_KEY}/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,):
        self.get_info = {}


    def get_data(self):
        respons = requests.get(API_URL)
        self.get_info = respons.json()['prices']
        return self.get_info


    def put_data(self):
        for city in self.get_info:
            param_id = {
                'price': {
                'city':city['city'],
                'iataCode': city['iataCode'],
                'lowestPrice':city['lowestPrice']
                }
            }
            respons = requests.put(url=f"{API_URL}/{city['id']}", json=param_id)








