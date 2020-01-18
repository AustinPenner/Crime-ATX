import requests
import json
from time import sleep
from pymongo import MongoClient
import pprint

class YelpFusion(object):
    """Get search results from the Yelp Fusion API: https://www.yelp.com/developers/documentation/v3"""

    def __init__(self, api_key):
        """Initialize an API search object with a specified API key"""
        super(YelpFusion, self).__init__()
        self.api_key = api_key


    def search_by_location_and_type(self, lat, lng, radius, limit, categories, collection):
        """
        Return a new Point representing the difference of self and other.

        Parameters
        ----------
        lat (float): Latitude of search point
        lng (float): Longitude of search point
        radius (int): Radius of search
        limit (int): Max number of reults to retrieve
        categories (str): Type of business
        collection (Collection): mongodb collection to receive results
        """
        endpoint_url = 'https://api.yelp.com/v3/businesses/search'
        headers = {'Authorization': 'Bearer {}'.format(self.api_key)}
        params = {
            'latitude': lat,
            'longitude': lng,
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
    client = MongoClient()
    db = client['bars_and_crime']
    bars = db['bars']

    key_fp = '/home/ubuntu/keys/yelp_key.txt'
    with open(key_fp) as f:
        key = f.readline().rstrip()
    search_radius = 15000
    search_limit = 50
    search_points = [[30.387, -97.803],
                 [30.378, -97.679],
                 [30.291, -97.759],
                 [30.206, -97.822],
                 [30.251, -97.694]]

    api = YelpFusion(key)
    for point in search_points:
        lat, lng = point
        api.search_by_location_and_type(lat, lng, search_radius,
                                        search_limit, "bars", bars)
