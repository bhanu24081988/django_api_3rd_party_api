import json
import requests


URL="http://127.0.0.1:8000/student/"

data={
    'roll':103,
    'name':'aman'
}
data={
    'id':3,
    'roll':103,
    'name' : 'akash singh'
   
}
json= json.dumps(data)

response = requests.put(url=URL,data=json)

json_response= response.json()

print(json_response)