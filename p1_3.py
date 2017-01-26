# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc



s = 'gqljinzhwyncncfmrmawgb'
lst = list(s)
substrings = [] # list for substings from s
string = [lst[0]]#list that contain letters from s in alphabetical order
lst.remove(lst[0])
while len(lst) > 0:
    if lst[0] >= string[-1]:
        string.append(lst[0])
        lst.remove(lst[0])
    else:
        substrings.append("".join(string))
        string = [lst[0]]
        lst.remove(lst[0])
if len(string) > 0:
    substrings.append("".join(string))
    
max_length = 0
result = []
for i in substrings:
    if len(i) > max_length:
        max_length = len(i)
for j in substrings:
    if len(j) == max_length:
        result.append(j)

print("Longest substring in alphabetical order is: ", result[0])         

