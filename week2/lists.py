arr1 = [100,"Brad",-10,1,10.4,3,4,70,24,-9, "Hello", "How"]
arr2 = [100,-10,1,3,4,70,24,-9]
arr3 = [100,-10,1,3,10,4,70,24,-9]
arr4 = [[1,2,3],[4,5,6]]
arr5 = [[1,4],[2,5],[3,6]]

#1
arr2 = [x for x in arr1 if isinstance(x, int)]  # сандардан басқаларын шығармаймыз
print("arr2:", arr2)

# 2
arr4 = [[1, 2, 3], [4, 5, 6]]
arr5 = [[arr4[j][i] for j in range(len(arr4))] for i in range(len(arr4[0]))]
print("arr5:", arr5)

# 3
arr3 = arr2.copy()
arr3.insert(4, 10)  # 10 санын 4-индекске қоямыз
print("arr3:", arr3)

