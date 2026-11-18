# Creating a tuple
browser_details = ("Chrome", 120, "Windows")

# Accessing elements
print("Browser:", browser_details[0])
print("Version:", browser_details[1])

# Tuple length
print("Total elements:", len(browser_details))

# Iterating
for detail in browser_details:
    print(detail)

# Tuple unpacking
browser, version, operating_system = browser_details

print(browser)
print(version)
print(operating_system)