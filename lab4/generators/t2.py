def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield str(i)
n=int(input("n= "))
print(f"Even numbers between 0 and {n}: ")
print(",".join(even(n)))
