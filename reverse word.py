def reverse_word(word):
    reversed_word=""


    for char in reversed(word):
        reversed_word+=char

    return reversed_word

user_word=input("enter the word:")
result=reverse_word(user_word)

print("reversed_word:",result)
