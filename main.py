import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythondb")
mycursor=mydb.cursor()

## Insert Data into database
def InsertData(nameValue,passwordValue):
    try:
        mycursor.execute(f"insert into login (name,password) values('{nameValue}','{passwordValue}')")
        mydb.commit()
        print("Data Inserted Successfully")
    except Exception as e:
        print("Unable to insert the data !! Please try again later",e)

## Update Data into database
def UpdateData(idVal,nameValue):
    try:
        mycursor.execute(f"update login set name='{nameValue}' where id={idVal}")
        mydb.commit()
        print("Data Updated Successfully")
    except:
        print("Unable to update the data !! Please try again later")

## Delete Data into database
def DeleteData(idVal):
    try:
        mycursor.execute(f"delete from login where id={idVal}")
        mydb.commit()
        print("Data Deleted Successfully")
    except:
        print("Unable to Delete the data !! Please try again later")

## Fetch Data from database
def GetData():
    try:
        mycursor.execute("select * from login order by id desc")
        result=mycursor.fetchall()
        print(result)
    except:
        print("Unable to Delete the data !! Please try again later")


### Calling method to insert data

# InsertData('Deepak','Tiwari')

### Calling method to Update Data

# UpdateData(2,"Deepak")

### Calling method to delete the data 

# DeleteData(3)

### Calling method to delete the data

GetData()


# Closing the DB connection
mydb.close()

