import csv

# Helper function to load data from a CSV file
def load_data(filename):
    data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Helper function to save data to a CSV file
def save_data(filename, data, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Load data from CSV files
products = load_data('products.csv')
couriers = load_data('couriers.csv')
orders = load_data('orders.csv')

# Create order status list
order_status_list = ["Preparing", "Out for delivery", "Delivered"]

# Print main menu options
def print_main_menu():
    print("Main Menu:")
    print("1. Products Menu")
    print("2. Couriers Menu")
    print("3. Orders Menu")
    print("0. Exit")

# Print products menu options
def print_products_menu():
    print("Products Menu:")
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("0. Return to Main Menu")

# Print couriers menu options
def print_couriers_menu():
    print("Couriers Menu:")
    print("1. View Couriers")
    print("2. Add Courier")
    print("3. Update Courier")
    print("4. Delete Courier")
    print("0. Return to Main Menu")

# Print orders menu options
def print_orders_menu():
    print("Orders Menu:")
    print("1. View Orders")
    print("2. Add Order")
    print("3. Update Order Status")
    print("4. Update Order")
    print("5. Delete Order")
    print("0. Return to Main Menu")

# Main menu logic
def handle_main_menu():
    while True:
        print_main_menu()
        main_option = int(input("Enter your choice: "))

        if main_option == 0:
            save_data('products.csv', products, ['name', 'price'])
            save_data('couriers.csv', couriers, ['name', 'phone'])
            save_data('orders.csv', orders, ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
            break
        elif main_option == 1:
            handle_products_menu()
        elif main_option == 2:
            handle_couriers_menu()
        elif main_option == 3:
            handle_orders_menu()
        else:
            print("Invalid option. Please choose a valid menu option.")

# Products menu logic
def handle_products_menu():
    while True:
        print_products_menu()
        product_option = int(input("Enter your choice: "))
        
        
        if product_option == 0:
            break
        elif product_option == 1:
            view_products()
        elif product_option == 2:
            add_product()
        elif product_option == 3:
            update_product()
        elif product_option == 4:
            delete_product()

# Couriers menu logic
def handle_couriers_menu():
    while True:
        print_couriers_menu()
        courier_option = int(input("Enter your choice: "))

        if courier_option == 0:
            break
        elif courier_option == 1:
            view_couriers()
        elif courier_option == 2:
            add_courier()
        elif courier_option == 3:
            update_courier()
        elif courier_option == 4:
            delete_courier()
        

# Orders menu logic
def handle_orders_menu():
    while True:
        print_orders_menu()
        order_option = int(input("Enter your choice: "))

        if order_option == 0:
            break
        elif order_option == 1:
            view_orders()
        elif order_option == 2:
            add_order()
        elif order_option == 3:
            update_order_status()
        elif order_option == 4:
            update_order()
        elif order_option == 5:
            delete_order()

# View products
def view_products():
    print("Products List:")
    for i, product in enumerate(products):
        print(f"{i}: {product}")

# Add a new product
def add_product():
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    products.append({"name": name, "price": price})

# Update an existing product
def update_product():
    view_products()
    index = int(input("Enter product index to update: "))
    for key in products[index]:
        new_value = input(f"Enter new value for {key} (or press enter to keep current): ")
        if new_value:
            products[index][key] = new_value

# Delete a product
def delete_product():
    view_products()
    index = int(input("Enter product index to delete: "))
    del products[index]

######################## couriers#################
#view couriers
def view_couriers():
    print("Couriers List:")
    for i, courier in enumerate(couriers):
        print(f"{i}: {courier}")

# Add a new courier
def add_courier():
    name = input("Enter courier name: ")
    phone = input("Enter courier phone number: ")
    couriers.append({"name": name, "phone": phone})

# Update an existing courier
def update_courier():
    view_couriers()
    index = int(input("Enter courier index to update: "))
    for key in couriers[index]:
        new_value = input(f"Enter new value for {key} (or press enter to keep current): ")
        if new_value:
            couriers[index][key] = new_value

# Delete a courier
def delete_courier():
    view_couriers()
    index = int(input("Enter courier index to delete: "))
    del couriers[index]
##############################ORDERS########################
# View orders
def view_orders():
    print("Orders List:")
    for i, order in enumerate(orders):
        print(f"{i}: {order}")

# Add a new order
def add_order():
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone number: ")

    print("Products List:")
    for i, product in enumerate(products):
        print(f"{i}: {product}")
    items = input("Enter comma-separated list of product indices: ")

    print("Couriers List:")
    for i, courier in enumerate(couriers):
        print(f"{i}: {courier}")
    courier_index = int(input("Enter courier index: "))

    order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": courier_index,
        "status": "Preparing",
        "items": items
    }
    orders.append(order)

# Update the status of an existing order
def update_order_status():
    view_orders()
    order_index = int(input("Enter order index to update status: "))

    for i, status in enumerate(order_status_list):
        print(f"{i}: {status}")
    status_index = int(input("Enter status index: "))

    orders[order_index]['status'] = order_status_list[status_index]

# Update an existing order
def update_order():
    view_orders()
    order_index = int(input("Enter order index to update: "))
    for key in orders[order_index]:
        new_value = input(f"Enter new value for {key} (or press enter to keep current): ")
        if new_value:
            orders[order_index][key] = new_value

# Delete an order
def delete_order():
    view_orders()
    order_index = int(input("Enter order index to delete: "))
    del orders[order_index]

# Run the main application loop
handle_main_menu()
