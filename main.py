expenses = []

def add_expenses(expenses, amount, category, description):
  expenses.append({
    "amount": amount,
    "category": category,
    "description": description
  })

def generate_report(expenses):
  for expense in expenses:
    print(f"Amount: {expense['amount']}")
    print(f"Category: {expense['category']}")
    print(f"Description: {expense['description']}")
while True:

  print("Choose an option:")
  print("1. Add expense")
  print("2. Generate report")
  print("3. Show report for category")
  print("4. Exit")
  choice = input()


  if choice == "1":
    amount = input("Amount: ")
    category = input("Category: ")
    description = input("Description: ")
    add_expenses(expenses, amount, category, description)
  elif choice == "2":
    generate_report(expenses)
  elif choice == "3":
    category = input("Category: ")
    for expense in expenses:
      if expense["category"] == category:
        print(f"Amount: {expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
  elif choice == "4":
    break
