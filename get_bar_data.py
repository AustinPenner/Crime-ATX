import requests
import json
from time import sleep

class GooglePlaces(object):
    def __init__(self, api_key):
        super(GooglePlaces, self).__init__()
        self.api_key = api_key


    def search_by_city_and_type(self, location, radius, types):
        endpoint_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.api_key
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])

        sleep(2)
        while 'next_page_token' in results:
            params['pagetoken'] = results['next_page_token']
            res = requests.get(endpoint_url, params = params)
            results =  json.loads(res.content)
            places.extend(results['results'])
            sleep(2)
            if len(places) > 40:
                break
        return places


if __name__ == "__main__":
    key_fp = '/home/ubuntu/keys/g_places_key.txt'
    with open(key_fp) as f:
        key = f.readline()

    api = GooglePlaces(key)
    bars = api.search_by_city_and_type("30.307, -97.763", "25000", "bar")
    print(len(bars))
    print(len(bars[0]))
    print(bars[0].keys())
    print(bars[0])
