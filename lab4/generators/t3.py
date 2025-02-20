def tf(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i

a=int(input())
print(f"Numbers divisible by 3 and 4 between 0 and {a}: ")
for j in tf(a):
    print(j)