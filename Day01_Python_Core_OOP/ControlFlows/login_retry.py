correct_username = "admin"
correct_password = "admin123"

max_attempts = 3
attempt = 1

while attempt <= max_attempts:

    print(f"\nLogin attempt: {attempt}")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break

    else:
        print("Invalid credentials")

    attempt += 1

else:
    print("Maximum login attempts exceeded")