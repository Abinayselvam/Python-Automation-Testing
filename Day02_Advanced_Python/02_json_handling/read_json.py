import json

with open(
    "Day02_Advanced_Python/02_json_handling/test_data.json",
    "r",
    encoding="utf-8"
) as file:

    test_data = json.load(file)

print("Environment:", test_data["test_environment"])
print("Browser:", test_data["browser"])

for user in test_data["users"]:
    print("Username:", user["username"])