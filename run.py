from expense import Expense
import csv
import os
from datetime import datetime
import calendar

file_path = "expenses.csv"
budget = 1500 

def main():
    print(f"Running Expense Tracker!")
    expense = get_users_expense()
    file_path = "expenses.csv"
    budget = 1500
    save_expense_to_file(expense)
    summarise_expenses(file_path, budget)

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
    with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Expense Name", "Category", "Amount"])

    # Write the expense data to the CSV file
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense.name, expense.category, expense.amount])
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(expense_name, expense_amount, expense_category)

    print(f"Expense data saved to {file_path}.")
    print(f"Saving User Expense: {expense}")

def summarise_expenses(file_path, budget):
    print("Summarising User Expense")
    expenses: list[Expense] = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense (
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("What you have spent by Category")
    for key, amount in amount_by_category.items():
        print(f"{key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent {total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"You have {remaining_budget:.2f} this month!")

    current_date = datetime.now()
    _, total_days_in_month = calendar.monthrange(current_date.year, current_date.month)
    remaining_days = total_days_in_month - current_date.day
    return remaining_days
    print("Remaining days in the current month:", remaining_days)

    daily_budget = remaining_budget / remaining_days
    print(f"Budget per day: ${daily_budget:.2f}")
      

if __name__ =="__main__":
    main()