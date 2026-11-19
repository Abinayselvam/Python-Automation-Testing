import json

user = {
    "id": 101,
    "name": "Abinaya",
    "role": "Software Engineer",
    "active": True
}

json_data = json.dumps(user, indent=4)

print(json_data)