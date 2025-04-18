import psycopg2

connect = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="postgresql"
)

cursor = connect.cursor()

phone = input("Enter the phone number to search: ")

cursor.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
result = cursor.fetchall()

if result:
    for row in result:
        print("ID:",row[0],"Name:", row[1], "| Phone:", row[2])
else:
    print("No records found with this phone number.")

cursor.close()
connect.close()
