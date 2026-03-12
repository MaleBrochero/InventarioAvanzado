# Inventory list
inventory = []
# Total value accumulator
total_inventory_value = 0
# Data input
try:

    # Create a menu that asks the user which action to perform
    menu = input(f"""Please select the number of the operation you want to perform:
                1. Add product
                2. Show inventory
                3. Calculate statistics
                4. Exit \n""")
    
    while menu == "1" or "2" or "3":

        if menu == "1":  # Add product
            product_name = input("Please enter the product name: ")
            price = float(input("Please enter the product price: "))
            quantity = int(input("Please enter the product quantity: "))
            total_cost = price * quantity  # Operation
            total_inventory_value = total_inventory_value + total_cost  # Accumulator

            product = {
                "Product_name": product_name,  # Dictionary
                "Unit_price": price,
                "Quantity": quantity,
                "Calculated_total_cost": total_cost
            }
            inventory.append(product)

        elif menu == "2":  # Show inventory
            for product in inventory:
                print(product)

        elif menu == "3":  # Calculate statistics
            number_of_registered_products = len(inventory)
            print(f"""Number of products in inventory: {number_of_registered_products}
Total inventory value: {total_inventory_value}""")

        elif menu == "4":  # Exit
            print("End")
            break

        else:
            print("Wrong input, please try again")

        menu = input(f"""Please select the number of the operation you want to perform:
        1. Add product
        2. Show inventory
        3. Calculate statistics
        4. Exit \n""")
    
    print("Program finished")

except ValueError:
    print("Invalid input, please try again")

