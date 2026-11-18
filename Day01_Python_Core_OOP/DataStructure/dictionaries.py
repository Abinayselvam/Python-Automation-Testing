# Creating a dictionary
user = {
    "id": 101,
    "name": "Abinaya",
    "role": "Software Engineer",
    "is_active": True
}

# Accessing values
print("User ID:", user["id"])
print("Name:", user["name"])

# Access using get()
print("Role:", user.get("role"))

# Adding a new key
user["department"] = "Development"

# Updating a value
user["role"] = "Automation Engineer"

# Removing a key
user.pop("department")

# Display all keys
print(user.keys())

# Display all values
print(user.values())

# Display key-value pairs
for key, value in user.items():
    print(key, ":", value)