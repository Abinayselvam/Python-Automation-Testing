try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


try:
    print("Executing operation")

    number = int("100")

except ValueError:
    print("Conversion failed")

else:
    print("Operation completed successfully")

finally:
    print("Cleanup operation completed")