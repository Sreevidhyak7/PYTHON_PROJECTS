
# BASIC RESTAURANT MANAGEMENT SYSTEM

# Restaurant Menu
menu = {
    1: {"name": "Burger", "price": 120},
    2: {"name": "Pizza", "price": 250},
    3: {"name": "Pasta", "price": 180},
    4: {"name": "Sandwich", "price": 100},
    5: {"name": "French Fries", "price": 80}
}

# Customer Order
order = {}

print("================================")
print("     WELCOME TO FOOD CORNER")
print("================================")

while True:

    print("\n1. Display Menu")
    print("2. Add Item to Order")
    print("3. View Order")
    print("4. Remove Item")
    print("5. Generate Bill")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    # Display Menu
    if choice == 1:

        print("\n----------- MENU -----------")

        for item_id, item in menu.items():
            print(item_id, ".", item["name"], "- Rs.", item["price"])

    # Add Item
    elif choice == 2:

        print("\nEnter the item number to order:")
        item_id = int(input("Item number: "))

        if item_id in menu:

            quantity = int(input("Enter quantity: "))

            if quantity > 0:

                if item_id in order:
                    order[item_id] += quantity

                else:
                    order[item_id] = quantity

                print("Item added successfully!")

            else:
                print("Quantity must be greater than zero.")

        else:
            print("Invalid item number!")

    # View Order
    elif choice == 3:

        if len(order) == 0:
            print("\nYour order is empty.")

        else:

            print("\n--------- YOUR ORDER ---------")

            total = 0

            for item_id, quantity in order.items():

                item_name = menu[item_id]["name"]
                price = menu[item_id]["price"]
                subtotal = price * quantity

                print(item_name, "x", quantity, "=", subtotal)

                total += subtotal

            print("------------------------------")
            print("Total Amount: Rs.", total)

    # Remove Item
    elif choice == 4:

        if len(order) == 0:
            print("\nYour order is empty.")

        else:

            print("\n--------- YOUR ORDER ---------")

            for item_id, quantity in order.items():
                print(item_id, ".", menu[item_id]["name"],
                      "x", quantity)

            remove_id = int(input("\nEnter item number to remove: "))

            if remove_id in order:
                del order[remove_id]
                print("Item removed successfully!")

            else:
                print("Item not found in your order.")

    # Generate Bill
    elif choice == 5:

        if len(order) == 0:
            print("\nNo items ordered!")

        else:

            print("\n================================")
            print("          FINAL BILL")
            print("================================")

            total = 0

            for item_id, quantity in order.items():

                item_name = menu[item_id]["name"]
                price = menu[item_id]["price"]
                subtotal = price * quantity

                print(item_name, "x", quantity,
                      "Rs.", subtotal)

                total += subtotal

            print("--------------------------------")
            print("Total Bill: Rs.", total)
            print("Thank you for visiting!")
            print("================================")

            order.clear()

    # Exit
    elif choice == 6:

        print("\nThank you for visiting FOOD CORNER!")
        break

    else:
        print("\nInvalid choice! Please try again.")
