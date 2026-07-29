from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}



def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return get_date(prompt, allow_default)
        


def get_amount(prompt):
    try:
        amount = float(input("Enter the amount:"))
        if amount < 0:
            raise ValueError("Amount must be a non-negative non-zero number.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount(prompt)

def get_category(prompt, categories):
    category = input("Enter the category ('I' for Income, 'E' for Expense): ").upper()
    if category in categories:
        return categories[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category(prompt, categories)



def get_description(prompt):
    return input("Enter a description (optional): ")




