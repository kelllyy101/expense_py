from expense import Expense
import csv
import os


def main():
    print(f"Running Expense Tracker!")
    expense = get_users_expense()
    print(expense)
    save_expense_to_file(expense)
    summarise_expenses()

def get_users_expense():
    print("Getting Users Expense")
    expense_category = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_category}, {expense_amount}")

    expense_categories = [
        "🍔 Food", "🏠 House", "🚇 Trasport", "💊 Health", "🚙 Car", "👕 Clothes", "🎉 Fun", "💸 Bills", "🐶 Pets", "🍴 Restaurants"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input("Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_category, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Category does not exist. Please try again!")

        break


def save_expense_to_file(expense):
     file_path = "expenses.csv"

    # Check if the file exists, and if not, create the file and write the header row
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Expense Name", "Category", "Amount"])

    # Write the expense data to the CSV file
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense.name, expense.category, expense.amount])

    print(f"Expense data saved to {file_path}.")
    print(f"Saving User Expense: {expense}")

def summarise_expenses():
    print(f"Summarising User Expense")

if __name__ =="__main__":
    main()