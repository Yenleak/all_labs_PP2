def check_palindrome(word):
    lower_word=word.lower()
    reverse_word = lower_word[::-1]
    flag = True
    if reverse_word == lower_word:
        flag = True
    else:
        flag = False
    if flag:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not palindrome")

word = str(input("word: "))
check_palindrome(word)