import redis, time
from datetime import date

redis = redis.StrictRedis()

""" Requests are POSTed as json in the form:
```
{
    "location_type": <"latlon" or string ip>
    "api_key" : <your_api_key>,
    "location" : <(lat,lon) or string ip> or None,
    "locations" : <list of latlons or list of string ips> or None
}

"""

def handle_api_request(req):
    _type = req.get("type")
    day = date.today()
    resp = {}
    # do actual logic here
    return resp # dict
