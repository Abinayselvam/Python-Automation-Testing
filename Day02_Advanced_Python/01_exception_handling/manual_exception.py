def validate_age(age):

    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Age validation successful")


try:
    validate_age(16)

except ValueError as error:
    print("Validation error:", error)