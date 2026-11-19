import json

test_data = {
    "test_environment": "QA",
    "browser": "Chrome",
    "users": [
        {
            "username": "admin",
            "password": "admin123"
        },
        {
            "username": "tester",
            "password": "test123"
        }
    ]
}

with open("test_data.json", "w", encoding="utf-8") as file:
    json.dump(test_data, file, indent=4)

print("JSON file created successfully")