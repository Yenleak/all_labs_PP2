from datetime import date , timedelta
x=date.today()
y=timedelta(5)

print(f"Current date: {x}")
print(f"5 days before currend date: {x-y}")