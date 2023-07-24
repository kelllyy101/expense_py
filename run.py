def main():
    print(f"Running Expense Tracker!")
    get_users_expense()
    save_expense_to_file()
    summarise_expense()

def get_users_expense():
    print("Getting Users Expense")
    expense_name = input("Enter expense name:")
    print()

def save_expense_to_file():
    print(f"Saving User Expense")


def summarise_expenses():
    print(f"Summarising User Expense")

if __name__ =="__main__":
    main()