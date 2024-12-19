car = []


#CREATE 
#Create user
class Create:
    def func_CreateData(user):

        # Get the sql connection
        connection = dbConn.getConnection()
                
        name = input("Enter name:")
        id = input("Enter ID:")
        email = input("Enter email")

        try:
           query = "Insert Into User(Name, ID, email) Values(?,?)" 
           cursor = connection.cursor()

           # Execute the sql query
           cursor.execute(query, [name, id, email])

           # Commit the data
           connection.commit()
           print("User created successfully")

        except:
             print("Something wrong, please check")

        finally:
           # Close the connection
           connection.close()

#Create car
class Create:
    def func_CreateData(car):

        # Get the sql connection
        connection = dbConn.getConnection()
        car = ["GYH0501", "NYO2098", "XSR5896"]
        for (x) in car:
            print (x)
        try:
           query = "Insert car plate number, refer to the list above:" 
           cursor = connection.cursor()

           # Execute the sql query
           cursor.execute(query, [car])

           # Commit the data
           connection.commit()
           print("Car rented successfully")

        except:
             print("Something wrong, please check")

        finally:
           # Close the connection
           connection.close()


#READ
class Read:
    def func_ReadData(user):   
        # Get the sql connection
        connection = dbConn.getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from User')

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))


#UPDATE
class Update:
    def func_UpdateData(user):
        # Get the SQL connection
        connection = dbConn.getConnection()

        id = input('Enter your Id = ')
    
        try:
           # Fetch the data which needs to be updated
           sql = "Select * From Employee Where Id = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('Name\t\t ID\t\t\t email')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
           print('-------------------------------------------')
           print('Enter New Data To Update User Record ')
           name = input("Enter new name:")
           id = input("Enter new ID:")
           email = input("Enter new email:")
           car = input("Enter new car plate number:")
           query = "Update Employee Set Name = ?, ID =?, Car = ?, Where age =?" 
        except:
            print("Something went wrong, please check")
        finally:
            connection.close()


#DELETE
class Delete:
    def func_DeleteData(user):
        # Get the SQL connection
        connection = dbConn.getConnection()

        id = input("Enter your ID:")
    
        try:
           # Get record which needs to be deleted
           sql = "Select * From Employee Where Id = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('Name\t\t ID\t\t\t Email')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
           print('-------------------------------------------')
           confirm = input('Are you sure to delete this record (Y/N)?')

           # Delete after confirmation
           if confirm == 'Y':
               deleteQuery = "Delete From User Where Id = ?"
               cursor.execute(deleteQuery,[id])
               connection.commit()
               print('Data deleted successfully!')
           else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()

#MENU
def menu():
    while True:
        print("\Car Rental System")
        print("1. Create user")
        print("2. Add rental car")
        print("3. Read All car")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            func_CreateData(user)
        elif choice == "2":
            func_CreateData(car)
        elif choice == "3":
            func_ReadData(user)
        elif choice == "4":
            func_UpdateData(user)
        elif choice == "5":
            func_DeleteData(user)
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("ERROR404, please try again.")

# Run the system
if __name__ == "__main__":
    menu()