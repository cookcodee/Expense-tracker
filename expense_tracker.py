import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Description", "Amount"])

def add_transaction(transaction_type):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category: ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date.today(), transaction_type, category, description, amount])

    print("Transaction added successfully!")

def view_transactions():
    if not os.path.exists(FILE_NAME):
        print("No transactions found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nDate | Type | Category | Description | Amount")
        print("-" * 50)

        for row in reader:
            print(" | ".join(row))

def show_summary():
    total_income = 0
    total_expense = 0

    if not os.path.exists(FILE_NAME):
        print("No transactions found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            amount = float(row[4])

            if row[1] == "Income":
                total_income += amount
            else:
                total_expense += amount

    balance = total_income - total_expense

    print("\n----- Summary -----")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {balance}")

def main():
    create_file()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction("Income")
        elif choice == "2":
            add_transaction("Expense")
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()