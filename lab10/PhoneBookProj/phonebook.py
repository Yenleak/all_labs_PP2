import psycopg2

connect= psycopg2.connect(
    host= "localhost",
    database= "phonebook_db",
    user="postgres",
    password="postgresql"
)

cursor=connect.cursor()

name= input("Enter name: ")
phone=input("Enter phone: ")


cursor.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
connect.commit()

print("Data inserted successfully!!!!")

cursor.close()
connect.close()
