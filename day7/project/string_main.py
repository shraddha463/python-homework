from string_utils import reverse_string, count_vowels, is_palindrome, count_words

text = input("Enter a string: ")

print("Reverse:", reverse_string(text))
print("Vowels:", count_vowels(text))
print("Palindrome:", is_palindrome(text))
print("Words:", count_words(text))
