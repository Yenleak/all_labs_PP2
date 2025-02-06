def histogram(list):
    for i in list:
        for j in range(i):
            print("*",end="")
        print()

mylist = list(map(int , input("Numbers of list: ").split()))
histogram(mylist)