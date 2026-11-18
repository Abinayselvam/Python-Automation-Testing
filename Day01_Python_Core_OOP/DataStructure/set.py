# Creating a set
browsers = {"Chrome", "Firefox", "Edge", "Chrome"}

print(browsers)

# Adding an element
browsers.add("Safari")

# Removing an element
browsers.remove("Edge")

# Safe removal
browsers.discard("Opera")

# Checking an element
print("Chrome available:", "Chrome" in browsers)

# Total unique elements
print("Total browsers:", len(browsers))




manual_testing = {"Login", "Register", "Logout"}
automation_testing = {"Login", "Search", "Payment"}

# Common test cases
print(manual_testing.intersection(automation_testing))

# All unique test cases
print(manual_testing.union(automation_testing))

# Test cases only in manual testing
print(manual_testing.difference(automation_testing))