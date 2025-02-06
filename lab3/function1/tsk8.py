def spy_game(nums):
    new_list = [0,0,7]
    flag = True
    for n in nums:
        if n == new_list[0]:
            new_list.pop(0)
        if not new_list:
            return True
    return False

        
    
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0])) 