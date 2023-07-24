from expense import Expense

def main():
    print(f"Running Expense Tracker!")
    expense = get_users_expense()
    print(expense)
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


def save_expense_to_file():
    print(f"Saving User Expense")

def summarise_expenses():
    print(f"Summarising User Expense")

if __name__ =="__main__":
    main()