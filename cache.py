from flask import Flask, request, Response
import requests
import json

# Time spent, about 20 minutes.
# August 1st, 2017 10AM to 10:18AM
# Tim w/ 1257 & 1228

# Turns out jsonify doesn't like lists.  +50 minutes.
# Changed to json.dumps and setting content heading fixed it.

# Pass through headers from TBAPIv3 + 5 minutes
# Ben w/ 5549

baseURL = 'http://www.thebluealliance.com/api/v3/'

tbaRoutes = {}  # All of your TBA data, gonna eat up your memory, doesn't honor cache.

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def tbaCachePath(path):
    # print(path)
    if path not in tbaRoutes:
        requestUrl = (baseURL + path)
        response = requests.get(requestUrl, headers={'X-TBA-Auth-Key': request.headers['X-TBA-Auth-Key']})
        tbaRoutes[path] = (response.json())

        # print("serving " + path + " from TBA")
        # print(type(response.json()))
        return Response(json.dumps(response.json()), mimetype="application/json; charset=\"utf-8\"")
    else:
        # print(type(tbaRoutes[path]))
        # print("serving " + path + " from CACHE")
        return Response(json.dumps(tbaRoutes[path]), mimetype="application/json; charset=\"utf-8\"")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)