"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""






s = "azcbobobegghakl"
count = 0
vowels = "aeiou"
for letter in s:
    if letter in vowels:
        count += 1
print("Number of vowels: ", count)     
