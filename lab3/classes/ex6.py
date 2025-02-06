class Prime:
    def __init__(self, number):
        self.numbers = number

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_prime_numbers(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

my_list = list(map(int ,input("enter numbers: ").split()))
prime_filter = Prime(my_list)
print(prime_filter.filter_prime_numbers())