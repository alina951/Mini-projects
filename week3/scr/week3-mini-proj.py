# Function to load data from files
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
        return [item.strip() for item in data]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

# Function to save data to files
def save_data(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + '\n')

# Function to display main menu options
def display_main_menu():
    print("\nMAIN MENU OPTIONS:")
    print("0: Exit")
    print("1: Manage Products")
    print("2: Manage Couriers")
    print("3: Manage Orders")

# Function to display product menu options
def display_product_menu():
    print("\nPRODUCT MENU OPTIONS:")
    print("0: Return to Main Menu")
    print("1: View Products")
    print("2: Add New Product")

# Function to display courier menu options
def display_courier_menu():
    print("\nCOURIER MENU OPTIONS:")
    print("0: Return to Main Menu")
    print("1: View Couriers")
    print("2: Add New Courier")

# Function to display order menu options
def display_order_menu():
    print("\nORDER MENU OPTIONS:")
    print("0: Return to Main Menu")
    print("1: View Orders")
    print("2: Add New Order")

# Load initial data from files
products = load_data('products.txt')
couriers = load_data('couriers.txt')
#print(couriers)
#print(products)
orders = []

# Main loop
while True:
    display_main_menu()
    user_input = input("Enter your choice: ")

    if user_input == '0':
        # Save data and exit
        save_data(products, 'products.txt')
        save_data(couriers, 'couriers.txt')
        print("Exiting the application. Goodbye!")
        break

    elif user_input == '1':
        # Products menu
        while True:
            display_product_menu()
            user_input = input("Enter your choice: ")

            if user_input == '0':
                break

            elif user_input == '1':
                print("\nPRODUCTS:")
                if products:
                    for product in products:
                        print(product)
                else:
                    print("No products available.")

            elif user_input == '2':
                product_name = input("Enter new product name: ")
                products.append(product_name)
                print("Product added successfully!")

            else:
                print("Invalid input! Please enter a valid choice.")

    elif user_input == '2':
        # Couriers menu
        while True:
            display_courier_menu()
            user_input = input("Enter your choice: ")

            if user_input == '0':
                break

            elif user_input == '1':
                print("\nCOURIERS:")
                if couriers:
                    for courier in couriers:
                        print(courier)
                else:
                    print("No couriers available.")

            elif user_input == '2':
                courier_name = input("Enter new courier name: ")
                couriers.append(courier_name)
                print("Courier added successfully!")

            else:
                print("Invalid input! Please enter a valid choice.")

    elif user_input == '3':
        # Orders menu
        while True:
            display_order_menu()
            user_input = input("Enter your choice: ")

            if user_input == '0':
                break

            elif user_input == '1':
                print("\nORDERS:")
                if orders:
                    for order in orders:
                        print(order)

                else:
                    print("No orders available.")

            elif user_input == '2':
                customer_name = input("Enter customer name: ")
                customer_address = input("Enter customer address: ")
                customer_phone = input("Enter customer phone number: ")

                new_order = {
                    'customer_name': customer_name,
                    'customer_address': customer_address,
                    'customer_phone': customer_phone
                }
                orders.append(new_order)
                print("Order added successfully!")

            else:
                print("Invalid input! Please enter a valid choice.")
