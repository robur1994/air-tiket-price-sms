import requests

# API_URL = "https://api.tequila.kiwi.com/"
# API_KEY = "djlSwQKnfF53GOP_jjrEtF-cW8VbRPeW"


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date




    # def search_city_price(self, city_cod):
    #     self.departure_airport_code = city_cod
    #     headers = {
    #         "apikey": API_KEY,
    #     }
    #
    #     PARAM_SHEARCH = {
    #         'fly_from': 'LON',
    #         'fly_to': city_cod,
    #         'date_from': '15/01/2024',
    #         'date_to': '14/02/2024'
    #     }
    #     respons = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=headers, params=PARAM_SHEARCH)
    #     respons.raise_for_status()
    #     data = respons.json()['data']
    #     self.departure_airport_code = city_cod
    #     self.departure_city = data[0]['cityTo']
    #     self.price = data[0]['price']
    #     for city in data:
    #         if self.price > city['price']:
    #             self.price = city['price']
    #     return self.price
    #
    #
    #



