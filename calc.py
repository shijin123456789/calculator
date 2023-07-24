
from add_num import add

from sub_num import subtract
print("Calculator Program")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '3':
        print("Exiting the program...")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice. Please try again.")
