browsers = ["Chrome", "Firefox", "Edge", "Safari"]

supported_browsers = ["Chrome", "Firefox", "Edge"]

for browser in browsers:

    if browser not in supported_browsers:
        print(f"Skipping unsupported browser: {browser}")
        continue

    print(f"Starting automation on {browser}")

    if browser == "Edge":
        print("Critical browser issue found. Stopping execution.")
        break

    print(f"Automation completed on {browser}")