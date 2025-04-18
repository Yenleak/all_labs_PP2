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
        cursor.execute("INSERT INTO phonebook (name, phone) VALUES(%s , %s)" , row)


connect.commit()
print("CSV data uploaded successfully!!!")
cursor.close()
connect.close()