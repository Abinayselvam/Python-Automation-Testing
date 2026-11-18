status_code = 200

if status_code == 200:
    print("Request successful")

elif status_code == 404:
    print("Resource not found")

elif status_code == 500:
    print("Internal server error")

else:
    print("Unexpected response")



#practice2
username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid username or password")