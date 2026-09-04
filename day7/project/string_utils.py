def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


def is_palindrome(text):
    return text == text[::-1]


def count_words(text):
    return len(text.split())
from string_utils import reverse_string, count_vowels, is_palindrome, count_words

text = input("Enter a string: ")

print("Reverse:", reverse_string(text))
print("Vowels:", count_vowels(text))
print("Palindrome:", is_palindrome(text))
print("Words:", count_words(text))