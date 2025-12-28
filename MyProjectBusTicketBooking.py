# Bus Ticket Booking System using Dictionary

routes = {
    "Pokhara": 40,
    "Chitwan": 35,
    "Kathmandu": 45
}

while True:
    print("\n1. View Routes")
    print("2. Book Seats")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for r in routes:
            print(r, "Seats left:", routes[r])

    elif choice == "2":
        route = input("Enter route name: ")
        seats = int(input("How many seats? "))

        if route in routes and seats <= routes[route]:
            routes[route] = routes[route] - seats
            print("Booking successful")
        else:
            print("Booking not possible")

    elif choice == "3":
        print("Thank you")
        break

    else:
        print("Invalid choice")
