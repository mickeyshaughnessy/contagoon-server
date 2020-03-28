# This is a differentially private contagion score server 

from handlers import handle_api_request
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
