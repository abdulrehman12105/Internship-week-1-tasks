# Define arrays for additional item categories
ssd_items = {"D1": "240 GB SSD", "D2": "480 GB SSD"}
ssd_prices = {"D1": 59.99, "D2": 119.99}

second_hdd_items = {"E1": "1 TB HDD", "E2": "2 TB HDD", "E3": "4 TB HDD"}
second_hdd_prices = {"E1": 49.99, "E2": 89.99, "E3": 129.99}

optical_drive_items = {"F1": "DVD/Blu-Ray Player", "F2": "DVD/Blu-Ray Re-writer"}
optical_drive_prices = {"F1": 50.00, "F2": 100.00}

os_items = {"G1": "Standard Version", "G2": "Professional Version"}
os_prices = {"G1": 100.00, "G2": 175.00}


# Function to display additional item menu and get user's choice
def display_additional_menu(items, prices, category):
    print(f"\n{category} Options:")
    for code, description in items.items():
        print(f"{code}: {description} - ${prices[code]:.2f}")

    additional_items = []
    while True:
        user_choice = input(f"Choose {category} to add (Enter item code, 'N' to finish): ").upper()
        if user_choice == 'N':
            break
        elif user_choice in items:
            additional_items.append(user_choice)
        else:
            print("Invalid choice. Please enter a valid item code.")

    return additional_items
# Initialize total_price
total_price = 0.0

# Function to update total price with additional items
def update_total_price(total_price, additional_items, items_prices):
    for item in additional_items:
        total_price += items_prices[item]
    return total_price


# Get user's choices for additional items
chosen_ssd = display_additional_menu(ssd_items, ssd_prices, "Solid State Drive")
chosen_second_hdd = display_additional_menu(second_hdd_items, second_hdd_prices, "Second Hard Disk Drive")
chosen_optical_drive = display_additional_menu(optical_drive_items, optical_drive_prices, "Optical Drive")
chosen_os = display_additional_menu(os_items, os_prices, "Operating System")

# Update total price with additional items
total_price = update_total_price(total_price, chosen_ssd, ssd_prices)
total_price = update_total_price(total_price, chosen_second_hdd, second_hdd_prices)
total_price = update_total_price(total_price, chosen_optical_drive, optical_drive_prices)
total_price = update_total_price(total_price, chosen_os, os_prices)

# Display the chosen additional items and updated total price
print("\nAdditional Chosen Items:")
if chosen_ssd:
    print("Solid State Drive:", ", ".join([ssd_items[item] for item in chosen_ssd]))
if chosen_second_hdd:
    print("Second Hard Disk Drive:", ", ".join([second_hdd_items[item] for item in chosen_second_hdd]))
if chosen_optical_drive:
    print("Optical Drive:", ", ".join([optical_drive_items[item] for item in chosen_optical_drive]))
if chosen_os:
    print("Operating System:", ", ".join([os_items[item] for item in chosen_os]))

print(f"\nUpdated Total Price: ${total_price:.2f}")
# Function to apply discounts based on the number of additional items
def apply_discount(total_price, additional_items):
    discount_percentage = 0.0

    if len(additional_items) == 1:
        discount_percentage = 5.0
    elif len(additional_items) >= 2:
        discount_percentage = 10.0

    if discount_percentage > 0:
        discount_amount = (discount_percentage / 100) * total_price
        total_price -= discount_amount
        return total_price, discount_amount
    else:
        return total_price, 0.0

# Apply discounts
total_price, discount_amount = apply_discount(total_price, chosen_ssd + chosen_second_hdd + chosen_optical_drive + chosen_os)

# Display the amount of money saved and the new price
print("\nDiscount Information:")
print(f"Amount of Money Saved: ${discount_amount:.2f}")
print(f"New Total Price after Discount: ${total_price:.2f}")