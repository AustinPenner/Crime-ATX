from pymongo import MongoClient

client = MongoClient()

db = client['bars_and_crime']
bars = db['bars']

def mongo_to_dict(doc):
    d = {}
    val = doc['_id']
    for k, v in val.items():
        if type(v) is dict:
            for k2, v2 in v.items():
                if type(v2) is dict:
                    for k3, v3 in v2.items():
                        d[k3] = v3
                elif type(v2) is not list:
                    d[k2] = v2
        else:
            d[k] = v
    return d


result = bars.aggregate( 
                [{"$group": 
                      { "_id": {"id": "$id", "alias": "$alias", "name": "$name",
                                "review_count": "$review_count", "rating": "$rating",
                                "coordinates": "$coordinates", "location": "$location"}}}]
        )

for item in result:
    py_dict = mongo_to_dict(item)
    with open('bar_data.csv', 'a') as f:
        vs = '\t'.join(str(x) for x in py_dict.values())
        f.write(f'{vs}\n')
