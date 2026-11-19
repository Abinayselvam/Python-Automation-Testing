import json
import os
from pathlib import Path

from dotenv import load_dotenv


# Locate repository root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Load .env from repository root
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(ENV_FILE)

# Locate JSON test data
TEST_DATA_FILE = (
    PROJECT_ROOT
    / "Day02_Advanced_Python"
    / "02_json_handling"
    / "login_test_data.json"
)


def get_required_config(name):

    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Missing required configuration: {name}"
        )

    return value


def load_test_data(file_path):

    if not file_path.exists():
        raise FileNotFoundError(
            f"Test data file not found: {file_path}"
        )

    try:

        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON format: {error}"
        ) from error


def main():

    try:

        app_url = get_required_config("APP_URL")
        browser = get_required_config("BROWSER")

        test_data = load_test_data(TEST_DATA_FILE)

        print("Configuration loaded successfully")
        print("Application URL:", app_url)
        print("Browser:", browser)

        for test_case in test_data["test_cases"]:

            username = test_case.get("username", "")
            expected = test_case.get("expected", "")

            if not username:
                print("Skipping test case with empty username")
                continue

            print(
                f"Username: {username}, Expected: {expected}"
            )

    except (ValueError, FileNotFoundError) as error:
        print("Configuration error:", error)


if __name__ == "__main__":
    main()