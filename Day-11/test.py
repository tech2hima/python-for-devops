import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_response = response.json()

for i in range(len(complete_response)):
    print (complete_response[i]["user"]["login"])