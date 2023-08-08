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
    save_expense_to_file(expense)
    summarise_expenses(file_path, budget)
    prompt_continue()

def get_users_expense():
    print("Getting Users Expense")
    expense_name = input("Enter expense name: ")
    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            print(f"You've entered {expense_name}, {expense_amount}")
            break
        except ValueError:
            print("Please enter valid numbers for the expense amount.")


    expense_categories = [
        "🍔 Food", "🏠 House", "🚇 Transport", "💊 Health", "🚙 Car", "👕 Clothes", "🎉 Fun", "💸 Bills", "🐶 Pets", "🍴 Restaurants"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        while True:
            try:
                selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
                if 1 <= selected_index + 1 <= 10:  # Check if selected_index is within the range [1, 10]
                    break
                else:
                    print("Invalid category number. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 10.")
        

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Category does not exist. Please try again!")


def save_expense_to_file(expense):
    with open(file_path, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([expense.name, expense.category, expense.amount])

    print(f"Expense data saved to {file_path}.")
    print(f"Saving User Expense: {expense}")

def summarise_expenses(file_path, budget):
    print("Summarising User Expense")
    expenses: list[Expense] = []
    amount_by_category = {}
    with open(file_path, "r") as f:
        i = 0
        for line in f.readlines():
            if i == 0:
                i += 1
                continue
            name, category, amount = line.strip().split(",")
            amount = float(amount)
            line_expense = Expense(
                name=name,
                category=category,
                amount=amount,
            )
            print(line_expense)
            expenses.append(line_expense)
            print(expenses)

            if category in amount_by_category:
                amount_by_category[category] += amount
            else:
                amount_by_category[category] = amount

    print("What you have spent by Category")
    for category, amount in amount_by_category.items():
        print(f"{category}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent 💲{total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    current_date = datetime.now()
    _, total_days_in_month = calendar.monthrange(current_date.year, current_date.month)
    remaining_days = total_days_in_month - (current_date.day - 1)
    print("Remaining days in the current month:", remaining_days)

    daily_budget = remaining_budget / remaining_days

    if daily_budget >= 100:
        print(f"Budget per day: 💲{daily_budget:.2f}")
        print(f"You have 💲{remaining_budget:.2f} this month! 📅")
        print(f"\033[92m Wow well done for staying in budget! Maybe add some to your savings! 💰\033[0m")
    elif 0 < daily_budget <= 20:
        print(f"Budget per day: 💲{daily_budget:.2f}")
        print(f"You have 💲{remaining_budget:.2f} this month! 📅")
        print(f"\033[38;5;208mBe careful, you're running low on money 💵\033[0m")
    elif daily_budget <= 0:
        print(f"\033[91m You\'ve exceeded your budget!\033[0m 🚫")
    else:
        print(f"Budget per day: 💲{daily_budget:.2f}")
        print(f"You have 💲{remaining_budget:.2f} remaining this month! 📅")
        print(f"\033[92m Your spending is on track. Keep it up!\033[0m 💪")


def group_expenses_by_category(expenses):
    amount_by_category = {}
    for expense in expenses:
        amount = expense.amount
        category = expense.category
        if category in amount_by_category:
            amount_by_category[category] += amount
        else:
            amount_by_category[category] = amount
    return amount_by_category


def display_expenses_by_category(file_path):
    print("Getting Expenses by Category")
    expenses = []
    with open(file_path, "r") as csv_file:
        lines = csv_file.readlines()
        for line in lines:
            name, amount, category = line.strip().split(",")
            expense = Expense(
                name=name,
                category=category,
                amount=amount,
            )
            expenses.append(expense)

    exp_by_cat = group_expenses_by_category(expenses)
    
    print("Total Expenses by Category:")
    for category, total_amount in exp_by_cat.items():
        print(f"{category}: {total_amount}")


def adjust_budget():
    global budget  # Declare 'budget' as global to modify it in this function
    while True:
        try:
            new_budget = float(input("Enter the new budget: "))
            if new_budget >= 0:
                budget = new_budget
                print(f"Budget adjusted to: {budget:.2f} 💰📊")
                break
            else:
                print("Invalid input. Please enter a non-negative number for the new budget.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def prompt_continue():
    
    while True:
        choice = input("Do you want to perform another action? (y/n): ").lower()
        if choice == 'y':
            print("\nExpense Tracker Menu:")
            print("1. Add Expense 💸💰")
            print("2. View Expenses 👀📜")
            print("3. Adjust Budget 📊✏️")
            print("4. Exit Tracker 👋")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                get_users_expense()
            elif choice == "2":
                display_expenses_by_category(file_path)
            elif choice == "3":
                adjust_budget()
            elif choice == "4":
                print("Exiting Expense Tracker. Goodbye!👋😊")
                break
            else:
                print("Invalid choice. Please choose a valid option (1/2/3/4).")
        elif choice == 'n':
            print("Exiting Expense Tracker. Goodbye!👋😊")
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

if __name__ =="__main__":
    main()