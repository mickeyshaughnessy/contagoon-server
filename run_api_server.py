# This is a differentially private contagion score server 

from utils import load_scorefield
import redis
from server import handle_api_request

redis = redis.StrictRedis()

""" Requests are POSTed as json in the form:
```
{
    "geo" : {<geo_data},
    "private_id_data" : {<id_data>},
}
```

The geo_data object currently only supports lat/lon pairs ie ```
```
{
  "lat" : <query_lattitude>,
  "lon" : <query_longitude>
}
```
"""
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score():
    req = request.data
    print(req)
    resp = handle_api_request(req)
    return Response(response=json.dumps(str(resp)), status=200, mimetype="application/json")

app.run(host="0.0.0.0", port=8010)
