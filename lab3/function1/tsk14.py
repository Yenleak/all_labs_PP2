from random import randint
def guessthenumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num = randint(1,20)
    summ = 0
    flag = True
    while flag:
        mynum = int(input("Take a guess: "))
        summ+=1
        if mynum == num:
            print(f"Good job, {name}! You guessed my number in {summ} guesses!")
            break
        elif mynum > num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")
guessthenumber()

def randomator(start, end, length):
    arr=[randint(start, end)for i in range(length)]
    print(arr)
randomator(1,10,10)