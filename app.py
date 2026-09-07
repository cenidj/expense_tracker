
expenses = []

menu = [
    "1. Add expense",
    "2. View expenses",
    "3. Show total spent",
    "4. Show spending by category",
    "5. Exit"
]

while True:
    print("\n=== Personal Expense Tracker ===\n")
    for option in menu:
        print(option)

    choice = input("Choose an option: ")

    if choice == "5":  # Exit
        break

    if choice == "1":  # Add expense
        try:
            expense_description = input("What do you spent money on? ")
            expense_category = input("What category? ")
            expense_amount = float(input("How much? "))
            current_expense = {
                "description": expense_description,
                "amount": expense_amount,
                "category": expense_category
            }
            expenses.append(current_expense)
            print("Expense added correctly!")
        except:
            print("Error adding the expense.")

    elif choice == "2":  # View expenses
        print("\n=== Expenses list ===")
        for index, expense in enumerate(expenses):
            print(
                f"{index + 1}. ${expense["amount"]}     | {expense["category"]}     | {expense["description"]}")

    elif choice == "3":  # Show total spent
        total_spent = 0
        for expense in expenses:
            total_spent += expense["amount"]
        print(f"Total spent ${total_spent:.2f}")

    elif choice == "4":  # Show spending by category
        category_count = {}

        for expense in expenses:
            if expense["category"] in category_count:
                category_count[expense["category"]] += expense["amount"]
            else:
                category_count[expense["category"]] = expense["amount"]

        for category, amount in category_count.items():
            print(f"{category}:      ${amount:.2f}")
