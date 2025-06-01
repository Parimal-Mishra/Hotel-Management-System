import mysql.connector as mys

print("-------------------------⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳-------------------------")
print("⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳ HOTEL MANAGEMENT SYSTEM ⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳")
print("-------------------------⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳-------------------------\n")
print("-------------------------⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳-------------------------")
print("⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳ Hotel TAJ ⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳")
print("-------------------------⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳-------------------------\n")

us=input("Enter Username for establishing Connection : ")
pw=input("\nEnter Password for establishing Connection : ")
db=input("\nEnter Database Name : ")
mycon=mys.connect(host="localhost",user=us,passwd=pw,database=db)

if mycon.is_connected():
    print("\n---------------------- Connection Succesfully Established --------------------\n")
    mycs=mycon.cursor()
    
#---------------------------------------------------------------------------
#Function To Add Customer Details
    def Cust_Details():
        create_table="Create Table if not exists Customer_Details(C_ID INT PRIMARY KEY,C_NAME VARCHAR(25) NOT NULL,C_ADDRESS VARCHAR(50) UNIQUE KEY,C_AGE INT NOT NULL,C_COUNTRY VARCHAR (15) NOT NULL,C_P_NO INT NOT NULL,C_EMAIL VARCHAR(50))"
        mycs.execute(create_table)
        cust_id=int(input("\nEnter Customer Id : "))
        cust_name=input("Enter Customer Name : ")
        cust_address=input("Enter Customer Address : ")
        cust_age=int(input("Enter Customer Age : "))
        cust_country=input("Enter Customer Country : ")
        cust_phoneno=int(input("Enter Customer Phone no. : "))
        cust_email=input("Enter Customer Email : ")
        insert="Insert Into Customer_Details values({0},'{1}','{2}',{3},'{4}',{5},'{6}')".format(cust_id,cust_name,cust_address,cust_age,cust_country,cust_phoneno,cust_email)
        mycs.execute(insert)
        mycon.commit()
        print("\n NEW CUSTOMER DETAILS ADDED \n")
        
    #----------------------------------------------------------------------------
    # Function to add a Booking
    
    def Book_Room(cust_id,customer_name, check_in, check_out, room_type):
        query = "Create table if not exists Bookings(C_ID INT PRIMARY KEY,C_NAME VARCHAR(30) NOT NULL, CHECK_IN DATE NOT NULL, CHECK_OUT DATE NOT NULL, ROOM_TYPE VARCHAR(10) NOT NULL)"
        mycs.execute(query)
        sql = "INSERT INTO Bookings VALUES({0}, '{1}', '{2}', '{3}', '{4}')".format(cust_id,customer_name, check_in, check_out, room_type)
        mycs.execute(sql)
        mycon.commit()
        print("Booking Added Successfully!")
                                                                                                            
#----------------------------------------------------------------------------
# Function to Display Customer Details
                                                                                                            
    def Display_Customer_Details():
        mycs.execute("SELECT * FROM Customer_Details LEFT JOIN Bookings USING(C_ID, C_NAME)")
        bookings = mycs.fetchall()
    
        if not bookings:
            print("\nNo Customer Details or Bookings found.")
        else:
            for booking in bookings:
                print("\n" + "="*60)
                print("Customer ID        :", booking[0])
                print("Customer Name      :", booking[1])
                print("Customer Address   :", booking[2])
                print("Customer Age       :", booking[3])
                print("Customer Country   :", booking[4])
                print("Customer Phone No. :", booking[5])
                print("Customer Email     :", booking[6])
                print("Check-In Date      :", booking[7] if booking[7] else "Not Booked")
                print("Check-Out Date     :", booking[8] if booking[8] else "Not Booked")
                print("Room Type          :", booking[9] if booking[9] else "Not Booked")
                print("="*60)

#-----------------------------------------------------------------------------
# Function to Update Customer Details

    def Update_Customer_Details():
        cust_id = int(input("\nEnter Customer ID to update details: "))
        mycs.execute("SELECT * FROM Customer_Details WHERE C_ID = {}".format(cust_id))
        data = mycs.fetchone()
        if not data:
            print("No such customer found.")
            return
        
        print("\nCurrent Details:")
        print("Customer Name:", data[1])
        print("Customer Address:", data[2])
        print("Customer Age:", data[3])
        print("Customer Country:", data[4])
        print("Customer Phone Number:", data[5])
        print("Customer Email:", data[6])
        
        print("\nEnter new details (leave blank to keep current value):")
        cust_name = input("New Name: ") or data[1]
        cust_address = input("New Address: ") or data[2]
        cust_age = input("New Age: ")
        cust_age = int(cust_age) if cust_age else data[3]
        cust_country = input("New Country: ") or data[4]
        cust_phoneno = input("New Phone Number: ")
        cust_phoneno = int(cust_phoneno) if cust_phoneno else data[5]
        cust_email = input("New Email: ") or data[6]

        query = """UPDATE Customer_Details SET 
                    C_NAME = %s, C_ADDRESS = %s, C_AGE = %s, 
                    C_COUNTRY = %s, C_P_NO = %s, C_EMAIL = %s 
                   WHERE C_ID = %s"""
        values = (cust_name, cust_address, cust_age, cust_country, cust_phoneno, cust_email, cust_id)
        mycs.execute(query, values)
        mycon.commit()
        print("\nCustomer details updated successfully.")
        
#-----------------------------------------------------------------------------
# Function to Delete Customer Details

    def Delete_Customer_Details():
        cust_id = int(input("\nEnter Customer ID to delete: "))
        mycs.execute("SELECT * FROM Customer_Details WHERE C_ID = {}".format(cust_id))
        data = mycs.fetchone()
        if not data:
            print("No such customer exists.")
            return

        confirm = input("Are you sure you want to delete this customer? (yes/no): ").lower()
        if confirm == 'yes':
            mycs.execute("DELETE FROM Rent WHERE C_ID = {}".format(cust_id))
            mycs.execute("DELETE FROM Bookings WHERE C_ID = {}".format(cust_id))
            mycs.execute("DELETE FROM Customer_Details WHERE C_ID = {}".format(cust_id))
            mycon.commit()
            print("Customer and all associated records deleted successfully.")
        else:
            print("Deletion cancelled.")


#-----------------------------------------------------------------------------
# Function to Calculate Room Rent
    
    def Calculate_Room_Rent():
        no_of_days = 0
        rent = 0
        c_name=""
        cust_id = int(input("\nEnter Customer ID : "))

        mycs.execute("Select C_ID,C_NAME,DATEDIFF(CHECK_OUT,CHECK_IN),ROOM_TYPE FROM Bookings Where C_ID={}".format(cust_id))
        rent = mycs.fetchall()
        if not rent:
                     print("No Such Record Found.")
        else:
            for i in rent:
                if i[3] == "Royal":
                    no_of_days = i[2]
                    rent = no_of_days * 10000
                elif i[3] == "Elite":
                    no_of_days = i[2]
                    rent = no_of_days * 5000
                elif i[3] == "Delux":
                    no_of_days = i[2]
                    rent = no_of_days * 3500
                elif i[3] == "Budget":
                    no_of_days = i[2]
                    rent = no_of_days * 2500
                    c_name = i[1]
            print("\nYour Total Room Rent is Rs.",rent)
        mycs.execute("Create Table if not exists Rent(C_ID INT PRIMARY KEY,C_NAME VARCHAR(25) NOT NULL,BILL_AMOUNT INT NOT NULL)")

        query = "Insert Ignore into Rent values({0}, '{1}', {2})".format(cust_id,c_name,rent)
        mycs.execute(query)
        mycon.commit()
        return rent
    
#-----------------------------------------------------------------------------
# Function to Generate Bill
    
    def Generate_Bill():
        cust_id = int(input("\nEnter Customer ID : "))
        mycs.execute("Select * FROM Rent Where C_ID={}".format(cust_id))
        bill = mycs.fetchone()
        print("---------------------------------- BILL --------------------------------")
        print("------------------------------- HOTEl TAJ ------------------------------")
        if not bill:
            print("No Such Record Found.")
        else:
            print("\nCustomer ID : ",bill[0])
            print("\nCustomer Name : ",bill[1])
            print("\nTotal amount : ",bill[2])
        print("\n------------------------------ THANK YOU -------------------------------")
        
#-----------------------------------------------------------------------------
# Function To Exit
    
    def Exit():
        mycon.close()

        print("\n-------------------- THANK YOU PLEASE VISIT AGAIN ----------------------")
        
#-------------------------------------------------------------------------------
# Main Menu
    
    while True:
        print("\n\t 1. ENTER CUSTOMER DETAILS")
        print("\t 2. BOOKING RECORDS")
        print("\t 3. DISPLAY CUSTOMER DETAILS")
        print("\t 4. UPDATING CUSTOMER DETAILS")
        print("\t 5. DELETING CUSTOMER DETAILS")
        print("\t 6. CALCULATING ROOM RENT")
        print("\t 7. GENERATE BILL")
        print("\t 8. EXIT")
        choice=int(input("\n\nEnter Your Choice : "))
        
        if choice == 1:
            Cust_Details()

        elif choice == 2:
            customer_id = int(input("\nEnter Customer ID : "))
            customer_name = input("Enter customer name: ")
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")
            print("Rooms Avaialable : ")
            print (" 1. Royal ----&gt; 10000 Rs./Night ")
            print (" 2. Elite ----&gt; 5000 Rs./Night ")
            print (" 3. Delux ----&gt; 3500 Rs./Night ")
            print (" 4. Budget ----&gt; 2500 Rs./Night ")
            room_type = input("Enter room type: ")
            Book_Room(customer_id, customer_name, check_in, check_out, room_type)

        elif choice == 3:
            Display_Customer_Details()

        elif choice == 4:
            Update_Customer_Details()

        elif choice == 5:
            Delete_Customer_Details()

        elif choice == 6:
            total_rent = Calculate_Room_Rent()

        elif choice == 7:
            Generate_Bill()

        elif choice == 8:
            Exit()
            break
else:
    print("\nCONNECTION NOT ESTABLISHED PLEASE CHECK USERNAME , PASSWORD , DATABASE")
