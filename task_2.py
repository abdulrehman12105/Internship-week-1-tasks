# Arrays to store item information
item_codes = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]
descriptions = ["Compact Case", "Tower Case", "8 GB RAM", "16 GB RAM", "32 GB RAM", "1 TB HDD", "2 TB HDD", "4 TB HDD",
                "240 GB SSD", "480 GB SSD", "1 TB Second HDD", "2 TB Second HDD", "4 TB Second HDD",
                "DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer", "Standard OS", "Professional OS"]
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Basic set of components cost
basic_components_cost = 200.00

# Function to display items and get user choice
def get_user_choice(category):
    print(f"\n{category} Options:")
    for i in range(len(item_codes)):
        print(f"{item_codes[i]} - {descriptions[i]} (${prices[i]:.2f})")
    user_choice = input(f"Choose {category} (Enter item code): ").upper()
    while user_choice not in item_codes:
        print("Invalid item code. Please try again.")
        user_choice = input(f"Choose {category} (Enter item code): ").upper()
    return user_choice

# Function to calculate and display the total price
def calculate_and_display_total(case, ram, hdd):
    total_price = basic_components_cost
    total_price += prices[item_codes.index(case)]
    total_price += prices[item_codes.index(ram)]
    total_price += prices[item_codes.index(hdd)]
    print("\nChosen Items:")
    print(f"Case: {case} - {descriptions[item_codes.index(case)]} (${prices[item_codes.index(case)]:.2f})")
    print(f"RAM: {ram} - {descriptions[item_codes.index(ram)]} (${prices[item_codes.index(ram)]:.2f})")
    print(f"Main HDD: {hdd} - {descriptions[item_codes.index(hdd)]} (${prices[item_codes.index(hdd)]:.2f})")
    print(f"Total Price: ${total_price:.2f}")

# Function to allow the user to add additional items
def add_additional_items():
    additional_items = []
    while True:
        choice = input("Do you want to add additional items? (yes/no): ").lower()
        if choice != "yes":
            break
        else:
            item_choice = get_user_choice("Additional Item")
            additional_items.append(item_choice)
    return additional_items

# Main program
print("Welcome to the Online Computer Shop!")
case_choice = get_user_choice("Case")
ram_choice = get_user_choice("RAM")
hdd_choice = get_user_choice("Main HDD")

calculate_and_display_total(case_choice, ram_choice, hdd_choice)

additional_items = add_additional_items()

if additional_items:
    for item in additional_items:
        basic_components_cost += prices[item_codes.index(item)]
    print("\nAdditional Items:")
    for item in additional_items:
        print(f"{item} - {descriptions[item_codes.index(item)]} (${prices[item_codes.index(item)]:.2f})")
    print(f"New Total Price: ${basic_components_cost:.2f}")

print("Thank you for shopping with us!")
