def res(n):
    for i in range(n,-1,-1):
        yield i

n=int(input())
for j in res(n):
    print(j)