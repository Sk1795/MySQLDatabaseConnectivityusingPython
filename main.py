import mysql.connector
con = mysql.connector.connect(host="localhost", port="3306", user="root", password="Saurabh@123", database='pythontest')
print(con)

#function to create table.
def create_table():
 #creating cursor 
 mycursor=con.cursor()
 #creating a table
 mycursor.execute("create table customer (cust_id int, cust_name varchar(20),mobile varchar(10),city varchar(20))")
 print("created") 
 mycursor.close()
#function to insert value in the table
def insert_table():
#creating cursor
 mycursor=con.cursor()
#inserting into table
 id=input("Enter cust id: ")
 nm=input("Enter name: ")    
 mobile=input("Enter mobile: ")
 city=input("Enter city: ")
 sql= "insert into customer values('"+ id+"','"+ nm+"','"+ mobile+"','"+ city+"')"
 print(sql)
 mycursor.execute(sql)
 con.commit()

#Function to display all record from table
def display_table():

#creating cursor 
 mycursor=con.cursor()
 print ("display from")

#Display a table
 mycursor.execute("select * from customer")
 myresult=mycursor.fetchall()

 for x in myresult:
  print(x)

#Function for delete the records
def delete1_table():
 mycursor=con.cursor() 
 id= input("Enter id to be deleted: ")
 sql="delete from customer where cust_id= "+id
 mycursor.execute(sql)
 con.commit()

#Menu driven application for database connectivity for cutomer data

print("1 create table")
print("2 insert value in table" )
print("3 display all records" )
print("4 delete records")
print("5 update records")
print("6 display perticuler")
choice=int(input("enter choice:"))

if choice == 1:
  create_table()
if choice== 2:
  print("inserting")
  insert_table()
if choice == 3:
    print("displaying") 
    display_table()
if choice ==4:
 delete1_table()   


