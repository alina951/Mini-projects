def main_menu():
    print("Main Menu:")
    print("0. Return to main menu")
    print("1. View products")
    print("2. Add new product")
    print("3. Update existing product")
    print("4. Delete product")
    print("5. Exit")

def view_products(products):
    if not products:
        print("No products available.")
    else:
        print("Products list:")
        for i, product in enumerate(products):
            print(f"{i}. {product}")

def add_product(products):
    product_name = input("Enter the new product name: ")
    products.append(product_name)
    print(f"Product '{product_name}' added.")

def update_product(products):
    if not products:
        print("No products available to update.")
    else:
        view_products(products)
        try:
            index = int(input("Enter the index of the product to update: "))
            if 0 <= index < len(products):
                new_name = input("Enter the new product name: ")
                products[index] = new_name
                print(f"Product at index {index} updated to '{new_name}'.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def delete_product(products):
    if not products:
        print("No products available to delete.")
    else:
        view_products(products)
        try:
            index = int(input("Enter the index of the product to delete: "))
            if 0 <= index < len(products):
                removed_product = products.pop(index)
                print(f"Product '{removed_product}' deleted.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    products = []
    while True:
        main_menu()
        choice = input("Please enter your choice: ")
        
        if choice == '0':
            print("Returning to main menu...")
            continue
        elif choice == '1':
            view_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            update_product(products)
        elif choice == '4':
            delete_product(products)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
