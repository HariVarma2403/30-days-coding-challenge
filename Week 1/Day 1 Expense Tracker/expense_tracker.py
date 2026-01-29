import os

FILE_NAME = "expenses.txt"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, etc.): ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{amount},{category}\n")
    print("Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    total = 0
    print("\nYour Expenses:")
    with open(FILE_NAME, "r") as file:
        for line in file:
            amount, category = line.strip().split(",")
            print(f"{category}: ₹{amount}")
            total += float(amount)
    print(f"\nTotal Spending: ₹{total}\n")

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
