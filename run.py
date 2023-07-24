def main():
    print(f"Running Expense Tracker!")
    get_users_expense()
    save_expense_to_file()
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

def save_expense_to_file():
    print(f"Saving User Expense")

def summarise_expenses():
    print(f"Summarising User Expense")

if __name__ =="__main__":
    main()