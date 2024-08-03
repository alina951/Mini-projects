# # import csv

# # # open people.csv and read as string
# # with open('week3/scr/ford_escort.csv','r') as file:
# #   reader = csv.reader(file, delimiter=',')
# #   for row in reader:
# #     print(row)

# # import json

# # # Assuming the menu_items.json file is in the same directory as this script
# # with open('C:/Users/44784/Downloads/menu_items.json', 'r') as file:
# #     data = json.load(file)

# # Print the resulting Python object
# # print(data)
# # import json

# # # #import json

# # # Load the JSON data from the file
# # with open('import json

# # # Load the JSON data from the file
# # with open('menu_items.json', 'r') as file:
# #     data = json.load(file)

# # # Access the list of menu items (adjust this according to your actual JSON structure)
# # menu_items = data['menu_items']

# # # Iterate through the items and print the "id" of each item
# # for item in menu_items:
# #     print(item['id'])
# # ', 'r') as file:
# #     data = json.load(file)

# # # Access the list of menu items (adjust this according to your actual JSON structure)
# # menu_items = data['menu_items']

# # # Iterate through the items and print the "id" of each item
# # for item in menu_items:
# #     print(item['id'])

# # import json

# # # Load the JSON data from the file
# # with open('C:/Users/44784/Downloads/menu_items.json', 'r') as file:
# #     data = json.load(file)

# # # Access the list of menu items (adjust this according to your actual JSON structure)
# # menu_items = data['menu_items']

# # # Iterate through the items and print the "id" of each item
# # for item in menu_items:
# #     print(item['id'])
#  #A list of all the vehicles owned by the company
# # vehicles = [
# #     {
# #         'make': 'Skoda',
# #         'model': 'Octavia',
# #         'engine': 1.4,
# #         'mileage': 16100,
# #     },
# #     {
# #         'make': 'Toyota',
# #         'model': 'Corolla',
# #         'engine': 1.6,
# #         'mileage': 32900,
# #     },{
# #         'make': 'Cannondale',
# #         'model': 'Synapse 3',
# #         'mileage': 640,
# #     }
# # ]

# # def print_report(vehicle):
    
# #     try :
# #     # Calculate carbon emissions for a vehicle based on engine size and mileage
# #         emissions = vehicle['engine'] * vehicle['mileage'] / 100
# #     except:
# #         emissions = 0
# #     # Print all details for a single vehicle
# #     print(f"MAKE     : {vehicle['make']}")
# #     print(f"MODEL    : {vehicle['model']}")
# #     if ["engine"] in vehicles:
# #         print(f"engine:{vehicle["engine"]} liters")
# #     elif ["engine"] not in vehicle:
# #         print( "engine: None")
# #     print(f"ENGINE   : {vehicle['engine']} litres")
# #     print(f"MILEAGE  : {vehicle['mileage']} miles")
# #     print(f"EMISSIONS: {emissions} cubic litres")
# #     print(f"")

# # # Generate a report for all vehicles in the fleet
# # for vehicle in vehicles:
# #     print_report(vehicle)

# class vechile:
#       def_init_(self, speed, colour )
#       self.speed= speed
#       self.colour = colour
#       speed = speed( )
# def
#   print(" created speed ")
#   print (" colour")
class Vehicle:
    def __init__(self, max_speed, color):
        self.max_speed = max_speed
        self.color = color

    def __str__(self):
        return f"Vehicle with max speed: {self.max_speed} km/h and color: {self.color}"

# Instantiate the Vehicle class
car = Vehicle(200, 'blue')

# Print out the attributes
print(f"Max Speed: {car.max_speed} km/h")
print(f"Color: {car.color}")

# Alternatively, use the __str__ method
print(car)
# #############################################
# class Vehicle:
#     def __init__(self, max_speed, color):
#         self.max_speed = max_speed
#         self.color = color

#     def change_max_speed(self, new_speed):
#         self.max_speed = new_speed

#     def change_color(self, new_color):
#         self.color = new_color

#     def __str__(self):
#         return f"Vehicle with max speed: {self.max_speed} km/h and color: {self.color}"

# # Instantiate the Vehicle class
# car = Vehicle(180, 'Red')

# # Print the initial attributes
# print("Initial state:")
# print(f"Max Speed: {car.max_speed} km/h")
# print(f"Color: {car.color}")

# # Update the max speed
# car.change_max_speed(200)

# # Update the color
# car.change_color('Blue')

# # Print the updated attributes
# print("\nUpdated state:")
# print(f"Max Speed: {car.max_speed} km/h")
# print(f"Color: {car.color}")

# # Alternatively, use the __str__ method
# print("\nUsing __str__ method:")
# print(car)


