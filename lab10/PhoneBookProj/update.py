import psycopg2
import csv

connect= psycopg2.connect(
    host= "localhost",
    database= "phonebook_db",
    user="postgres",
    password="postgresql"
)

cursor=connect.cursor()

with open(r'C:\Users\User\Desktop\LAB_PP2\labs\lab10\PhoneBookProj\data.csv', 'r') as f:
    reader= csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) < 2:
            continue  
    name = row[0]
    phone = row[1]
    cursor.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))



connect.commit()
print("Data updated successfully!!!")
cursor.close()
connect.close()