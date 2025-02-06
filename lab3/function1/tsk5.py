def permutation(word):
    for i in range(len(word)):
        for j in range(len(word)):
            print(word[j-i], end="")
        print()

word = str(input("Sozdi engiz: "))
permutation(word)