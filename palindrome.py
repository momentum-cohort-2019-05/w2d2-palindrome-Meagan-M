# reference example:

# sentence = "Making plots and visualizations is one of the most important tasks in data analysis."
# all_letters = "abcdefghijklmnopqrstuvwxyz"
# found_letters = []
# for letter in sentence.lower():
#     if letter in all_letters and letter not in found_letters:
#         found_letters.append(letter)
        
# print(found_letters)

# potentially a way to remove spacing and punctuation:

# def clean_text(text):
    # """
    # Given a text, return the text with no spaces or punctuation and all lowercased.
    # """
    # new_text = ""
    # text = text.lower()
    # for character in text:
    #     if character.isalpha():
    #         new_text = new_text + character
    # return new_text
    # found in: question of the day in string methods notebook
    

    # reverses the text
    # greeting = "Hello there!"
    # greeting[::-1]
    # '!ereht olleH'

import re
user_input = str(input("Enter a phrase or sentence to check if it is a palindrome. "))
print(user_input)

def is_palindrome(word):
    if word[0] == word[-1]:
        word = word[1:-1]
        print(word)
        if len(word) >= 2:
            is_palindrome(word)
        else:
            print("This is a palindrome.")
    else:
        print("This is not a palindrome.")

is_palindrome(user_input)



