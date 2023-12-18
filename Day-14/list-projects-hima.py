# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://himamounikag.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0wgrCabZu1d7RG5g9uJ-38GYyM2sVOlxVcfLqRMVoJXl_s6KMa1F8BVFQbbT7Im3oS0AI5gqdrC6p61rWhP4fI0-4teC4XFQfH8n4CcsOcWupRhnrY9Hmn_A-nZmeKutgDEOqUPs26Kitl_GXEbZ4dVWnyyVUr2YcQ0tyJVg0igQ=550C5A06"

auth = HTTPBasicAuth("tech2hima@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output[0]["name"]

print(name)