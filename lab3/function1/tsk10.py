def soz(list):
    nwlist=[]
    for i in list:
        if i not in nwlist:
            nwlist.append(i)
    return nwlist
mylist= list(map(int, input("Numbers of list: ").split()))
print(soz(mylist))