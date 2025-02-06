def check_prime(number):
    if number < 2 :
        return False
    for i in range(2,int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

def filter_list(list):
    new_list = []
    for n in list:
        if check_prime(n):
            new_list.append(n)
    return new_list

analiz = list(map(int, input("Enter numbers: ").split()))
print(filter_list(analiz))