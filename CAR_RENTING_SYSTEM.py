#Car Renting System
# Global variables to store user's selections
user_data = {
    "Name": None,
    "ID": None,
    "E-Mail": None,
    "Rented car": None,
    "Rent period": None
}


def user():
    global user_data
    print (input("Please enter your name:"))
    print (input("Please enter your ID number:"))
    print (input("Please enter your e-mail address:")) 
    return car()

def delete_data():
    global user_data
    print("Are you sure you want to delete your existing selections? (YES/NO)")
    choice = input().lower()
    if choice == 'yes':
        user_data = {
            "Name": None,
            "ID": None,
            "E-Mail": None,
            "Rented car": None,
        }
        print("All data has been deleted!")
        return user()
    elif choice == 'NO' or 'no':
        print("Data deletion cancelled.")

def car():
    global user_data
    print("Which car do you want to rent?")
    print("1. GYH0501")
    print("2. NYO2098")
    print("3. XSR5896")
    print("4. Delete data")
    a = int(input("Choose your car: "))
    if a not in [1, 2, 3, 4]:
        print("Invalid choice! Try again.")
    elif a == 4:
        return delete_data()
    user_data["Rented car"] = a
    return renting_period()


def renting_period():
    print("Please state your renting period:")
    print("1. 3 Days")
    print("2. 5 Days")
    print("3. 1 Week")
    print("4. 2 Weeks")
    print("5. Delete Existing Data")  # Option to delete data
    a = int(input("Choose your option: "))
    if a == 1:
        print ("Your renting period is 3 days, please enjoy our service!")
    if a == 2:
        print ("Your renting period is 5 days, please enjoy our service")
    if a == 3:
        print ("Your renting period is 1 week, please enjoy our service")
    if a == 4:
        print ("Your renting period is 2 weeks, please enjoy our service")
    elif a == 5:
        return delete_data()
    else:
        print("Data doesn't exist")
    user_data["Rent period"] = a


# To start the booking system
user()