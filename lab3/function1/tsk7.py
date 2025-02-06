def has_33(nums):
    n = len(nums)-1
    flag = True
    for i in range(n):
        if nums[i] == 3 and nums[i+1] == 3:
            flag = True
        else:
            flag = False
    if flag:
        print("True")
    else:
        print("False")


has_33([1, 3, 3])
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3])