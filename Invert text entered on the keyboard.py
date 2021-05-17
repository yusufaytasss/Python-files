from typing import Text


def flip_over(text):
    return text[::-1]
text = input("Enter a text :")
print(flip_over(text))