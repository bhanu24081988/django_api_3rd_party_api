import requests
import json
URL="http://127.0.0.1:8000/"

data= {
        "employee_id": 34,
        "employee_name": "ajay",
        "gender": "male",
        "salary": 25000
    }
data=json.dumps(data)
data=requests.post(url=URL,data=data)
print(data.json())

