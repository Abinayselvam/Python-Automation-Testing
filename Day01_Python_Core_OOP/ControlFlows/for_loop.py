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