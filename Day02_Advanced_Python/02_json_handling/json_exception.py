import json

invalid_json = '{"name": "Abinaya", "age": }'

try:
    data = json.loads(invalid_json)

except json.JSONDecodeError as error:
    print("Invalid JSON format")
    print("Error details:", error)