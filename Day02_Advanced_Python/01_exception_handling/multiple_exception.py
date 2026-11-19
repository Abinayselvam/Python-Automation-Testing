try:
    numbers = [10, 20, 30]

    index = int(input("Enter index: "))

    print(numbers[index])

except ValueError:
    print("Invalid index. Enter a number.")

except IndexError:
    print("Index is outside the list range.")

except Exception as error:
    print("Unexpected error:", error)