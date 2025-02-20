from datetime import datetime
a=datetime.now()
print(f"Now: {a}")
print(f"without microsecond: {a.replace(microsecond=0)}")