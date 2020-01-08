import requests
import json
from time import sleep
from pymongo import MongoClient
import pprint

class YelpFusion(object):
    def __init__(self, api_key):
        super(YelpFusion, self).__init__()
        self.api_key = api_key


    def search_by_location_and_type(self, latitude, longitude, radius, limit, categories, collection):
        endpoint_url = 'https://api.yelp.com/v3/businesses/search'
        headers = {'Authorization': 'Bearer {}'.format(self.api_key)}
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'radius': radius,
            'categories': categories,
            'sort_by': 'distance',
            'limit': limit
        }
        res = requests.get(endpoint_url, params = params, headers=headers)
        results =  json.loads(res.content)
        collection.insert_many(results['businesses'])

        n_businesses = results['total']
        print(f'Number of businesses: {n_businesses}')

        n_requests = 1
        while n_requests*limit < n_businesses and n_requests*limit < 1000:
            params['offset'] = n_requests * limit
            res = requests.get(endpoint_url, params = params, headers=headers)
            results =  json.loads(res.content)
            collection.insert_many(results['businesses'])

            with open('request_count.txt', 'w+') as f_page:
                f_page.write('Number of businesses total: {}\nNumber of businesses pulled: {}'.format(n_businesses, params['offset'] + len(results['businesses'])))

            n_requests += 1


if __name__ == "__main__":
    key_fp = '/home/ubuntu/keys/yelp_key.txt'
    with open(key_fp) as f:
        key = f.readline().rstrip()

    client = MongoClient()
    db = client['bars_and_crime']
    bars = db['bars']

    api = YelpFusion(key)
    api.search_by_location_and_type(30.378, -97.679, 15000, 50, "bars", bars)
