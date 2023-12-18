# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://himamounikag.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF0wgrCabZu1d7RG5g9uJ-38GYyM2sVOlxVcfLqRMVoJXl_s6KMa1F8BVFQbbT7Im3oS0AI5gqdrC6p61rWhP4fI0-4teC4XFQfH8n4CcsOcWupRhnrY9Hmn_A-nZmeKutgDEOqUPs26Kitl_GXEbZ4dVWnyyVUr2YcQ0tyJVg0igQ=550C5A06"

    auth = HTTPBasicAuth("tech2hima@gmail.com", API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "AB"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)