# This is a differentially private contagion score server 

from utils import load_scorefield
import redis, json
from flask import Flask, request, Response

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

app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score():
    req = request.data
    print(req)
    return Response(response=json.dumps(str(req)), status=200, mimetype="application/json")

app.run(host="0.0.0.0", port=8010)
