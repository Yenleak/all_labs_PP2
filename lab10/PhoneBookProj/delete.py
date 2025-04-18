import psycopg2

connect = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="postgresql"
)

cursor = connect.cursor()

name = input("Enter the name to delete: ")

cursor.execute("DELETE FROM phonebook WHERE name = %s", (name,))
connect.commit()

print(f"{cursor.rowcount} record(s) deleted.")

cursor.close()
connect.close()
