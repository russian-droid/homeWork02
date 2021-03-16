"""
codeWars Kata codewars.com

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""

str = 'Hello world'
vowel = 0

for x in str:
    if x in "aeoiu":
    # another way: if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u': 
        #vowel = vowel + 1
        vowel += 1
    else: 
        pass
print (vowel)
