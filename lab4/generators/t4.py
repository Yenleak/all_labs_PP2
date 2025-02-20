def squares(a,b):
    for i in range(a,b+1):
        if i**2:
            yield i

a=int(input("a="))
b=int(input("b="))

print(f"Squares of numbers between {a} and {b}: ")
for j in squares(a,b):
    print(j)