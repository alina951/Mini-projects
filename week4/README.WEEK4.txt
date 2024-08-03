

#####Overview#####

#####Client requirements######

This project is a simple command-line application for managing products, couriers, and orders.
 The application allows users to view, add, update, and delete products, couriers, and orders.
The data is stored in CSV files and is loaded into the application at startup and saved back to the files upon exit.

#####Features

View, add, update, and delete products
View, add, update, and delete couriers
View, add, update, and delete orders
Update the status of an order

#####Requirements

Python 3.x
csv module (part of Python's standard library)


######Files

products.csv: Stores product data with columns name and price
couriers.csv: Stores courier data with columns name and phone
orders.csv: Stores order data with columns customer_name, customer_address, customer_phone, courier, status, and items


###########CODE DESCRIPTION#########

HELPER FUNCTIONS FOR DATA PERSISTENCE

1:load_data(filename)
responsible for loading data from a CSV file and returning it in a suitable format (e.g., a list of dictionaries).

2:save_data(filename, data, fieldnames) 
This function for saving data to a file. 
It would save data to the specified filename, using fieldnames to define the columns if the data is in tabular form.

####MAIN CODE#################
These lines call the load_data function three times, loading data from three CSV files: products.csv, couriers.csv, and orders.csv.
The returned data from each call is stored in three variables: products, couriers, and orders.

load Data:
products = load_data('products.csv')  
couriers = load_data('couriers.csv')
orders = load_data('orders.csv')

This line defines a list called order_status_list which contains three possible statuses for orders: "Preparing", "Out for delivery", and "Delivered".
This list can be used to track the status of orders, possibly updating the status of each order in the orders data.

Oder status list:
order_status_list = ["Preparing", "Out for delivery", "Delivered"]

####MENU FUNCTIONS#############:

print main menu options
print product menu options
print couriers menu options
print order menu options


######## Main Application Loop################

The main loop of the application is responsible for handling user input 
and navigating through the different menus: products, couriers, and orders.
 It operates in an infinite loop, allowing the user to interact with the application until they choose to exit.

1. **Main Menu Display**: 
    - The loop begins by displaying the main menu options, prompting the user to make a selection.

2. **Main Menu Options**:
    If the user selects `0`, indicating they want to exit the application, the loop breaks, 
    and the program saves all data back to the CSV files before terminating.
    
  If the user selects `1`, `2`, or `3`, they are taken to the respective submenu (Products Menu, Couriers Menu, or Orders Menu).

3. **Submenus**:
    - Once in a submenu, the user is presented with a set of options specific to that category (viewing, adding, updating, or deleting records).
    
    - The user can navigate within each submenu by selecting the desired option. 
    
    - After completing an action (e.g., adding a product, updating an order), the user can choose to return to the main menu or continue interacting with the submenu.

4. **Data Manipulation**:
    - Depending on the user's selection, the program performs various data manipulation tasks such as viewing records, adding new entries, updating existing records, or deleting entries.

5. **Input Handling**:
    - The program prompts the user for input where necessary, such as when adding or updating records. 
    
    - Input validation is applied to ensure the entered data is appropriate and correctly formatted.

6. **Error Handling**:
    - Error handling mechanisms are in place to catch exceptions that may occur during file operations or data manipulation. 
    
    - If an error occurs, an appropriate error message is displayed, and the user is prompted to continue or take corrective action.

7. **Persistence**:
    - Data changes made during the session are stored in memory and persisted to the respective CSV files when the user chooses to exit the application.

8. **User-Friendly Interface**:
    - The interface provides clear and concise menus, making it easy for the user to navigate and perform desired actions.

Overall, the main loop provides a user-friendly and interactive experience for managing products, couriers, and orders within the application,
 ensuring efficient data handling and manipulation.



SUMMARY

This application allows users to manage products, couriers, and orders via a command-line interface.
 The data is persistently stored in CSV files, which are loaded at the start and saved upon exiting the program. 
 The user navigates through various menus to view, add, update, and delete entries in each category.

