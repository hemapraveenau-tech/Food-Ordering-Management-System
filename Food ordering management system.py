restaurant_list = [
    "Dominos",
    "KFC",
    "Burger King"
]

food_item_list = [
    "Pizza",
    "Burger",
    "Fries"
]

cart_list = []
order_list = []

user_list = [
    "User1",
    "User2",
    "User3"
]


while True:

    print("\n================================")
    print("     FOOD ORDERING MANAGEMENT")
    print("             SYSTEM")
    print("================================")

    print("1.OWNER")
    print("2.USER")
    print("3.EXIT")

    choice = input("Select role: ")


    if choice == "1":

        while True:

            print("\n------ OWNER PANEL ------")
            print("1. Dashboard")
            print("2. Manage Restaurants")
            print("3. Manage Food Items")
            print("4. View Orders")
            print("5. Manage Users")
            print("6. Reports")
            print("7. Logout")

            owner_choice = input("Enter choice: ")

            if owner_choice == "1":

                print("\n------ DASHBOARD ------")
                print("Restaurants:", len(restaurant_list))
                print("Food Items:", len(food_item_list))
                print("Orders:", len(order_list))
                print("Users:", len(user_list))

            elif owner_choice == "2":

                print("\n1. Add Restaurant")
                print("2. Delete Restaurant")
                print("3. View Restaurants")

                r_choice = input("Enter choice: ")


                if r_choice == "1":

                    restaurant = input(
                        "Enter restaurant name: "
                    )

                    if restaurant in restaurant_list:

                        print("Restaurant already exists!")

                    else:

                        restaurant_list.append(restaurant)

                        print("Restaurant added successfully!")


                elif r_choice == "2":

                    restaurant = input(
                        "Enter restaurant to delete: "
                    )

                    if restaurant in restaurant_list:

                        restaurant_list.remove(restaurant)

                        print("Restaurant deleted!")

                    else:

                        print("Restaurant not found!")


                elif r_choice == "3":

                    print("\n------ RESTAURANTS ------")

                    for restaurant in restaurant_list:

                        print(restaurant)


                else:

                    print("Invalid choice!")

            elif owner_choice == "3":

                print("\n1. Add Food Item")
                print("2. Delete Food Item")
                print("3. View Food Items")

                f_choice = input("Enter choice: ")


                if f_choice == "1":

                    food = input(
                        "Enter food item: "
                    )

                    if food in food_item_list:

                        print("Food item already exists!")

                    else:

                        food_item_list.append(food)

                        print("Food item added successfully!")


                elif f_choice == "2":

                    food = input(
                        "Enter food item to delete: "
                    )

                    if food in food_item_list:

                        food_item_list.remove(food)

                        print("Food item deleted!")

                    else:

                        print("Food item not found!")


                elif f_choice == "3":

                    print("\n------ FOOD ITEMS ------")

                    for food in food_item_list:

                        print(food)


                else:

                    print("Invalid choice!")

            elif owner_choice == "4":

                print("\n------ ORDERS ------")

                if len(order_list) == 0:

                    print("No orders available!")

                else:

                    for order in order_list:

                        print(order)

            elif owner_choice == "5":

                print("\n------ USERS ------")

                for user in user_list:

                    print(user)


            elif owner_choice == "6":

                print("\n------ REPORTS ------")

                print("Total Restaurants:",
                      len(restaurant_list))

                print("Total Food Items:",
                      len(food_item_list))

                print("Total Orders:",
                      len(order_list))

                print("Total Users:",
                      len(user_list))


   
            elif owner_choice == "7":

                print("Owner logged out!")

                break


            else:

                print("Invalid choice!")


    elif choice == "2":

        while True:

            print("\n------ USER PANEL ------")

            print("1. Browse Restaurants")
            print("2. View Menu")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Place Order")
            print("6. Track Order")
            print("7. Order History")
            print("8. Logout")

            user_choice = input("Enter choice: ")

            if user_choice == "1":

                print("\n------ RESTAURANTS ------")

                for restaurant in restaurant_list:

                    print(restaurant)

            elif user_choice == "2":

                print("\n------ FOOD MENU ------")

                for food in food_item_list:

                    print(food)

            elif user_choice == "3":

                print("\n------ FOOD MENU ------")

                for i, food in enumerate(food_item_list, 1):

                    print(i,".", food)

                food_number = int(input("Enter food number: "))

                if food_number >= 1 and food_number <= len(food_item_list):

                    food = food_item_list[food_number - 1]

                    cart_list.append(food)

                    print(food, "added to cart!")

                else:

                    print("Invalid food number!")
                
            elif user_choice == "4":

                print("\n------ CART ------")

                if len(cart_list) == 0:

                    print("Cart is empty!")

                else:

                    for food in cart_list:

                        print(food)

            elif user_choice == "5":

                if len(cart_list) == 0:

                    print("Cart is empty!")

                else:

                    for food in cart_list:

                        order_list.append(food)

                    cart_list.clear()

                    print("Order placed successfully!")


            elif user_choice == "6":

                if len(order_list) == 0:

                    print("No orders available!")

                else:

                    print("Your order is being prepared.")


            elif user_choice == "7":

                print("\n------ ORDER HISTORY ------")

                if len(order_list) == 0:

                    print("No orders yet!")

                else:

                    for order in order_list:

                        print(order)

            elif user_choice == "8":

                print("User logged out!")

                break


            else:

                print("Invalid choice!")


    elif choice == "3":

        print(
            "Thank you for using "
            "Food Ordering Management System!"
        )

        break


    else:

        print("Invalid choice!")

