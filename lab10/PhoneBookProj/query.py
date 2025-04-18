import psycopg2

connect = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="postgresql"
)

cursor = connect.cursor()

name = input("Enter the name to search: ")

cursor.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
result = cursor.fetchall()

if result:
    for row in result:
        print("Name:", row[1], "| Phone:", row[2])
else:
    print("No records found.")

cursor.close()
connect.close()
