browsers = ["Chrome", "Firefox", "Edge", "Safari"]

for browser in browsers:
    print("Testing browser:", browser)

#using range
#it is excluded 6
for number in range(1, 6):
    print(number)


#practice 2
test_cases = [
    "Valid Login",
    "Invalid Login",
    "Forgot Password",
    "Logout"
]

for index, test_case in enumerate(test_cases, start=1):
    print(f"Test Case {index}: {test_case}")


    #break loop
    test_cases = ["Login", "Register", "Payment", "Logout"]

for test_case in test_cases:

    if test_case == "Payment":
        print("Payment test found. Stopping execution.")
        break

    print("Executing:", test_case)

    #continue
test_cases = [
    "Login",
    "",
    "Register",
    "",
    "Logout"
]

for test_case in test_cases:

    if test_case == "":
        continue

    print("Executing:", test_case)