'''
Given a string containing lowercase letters (a-z) and numbers,
determine whether the string contains more numbers, more
letters, or an equal number of both. If the string contains an
invalid character (not a-z or 0-9) it should be ignored. If no
numbers or letters are present, the default response should be
“equal”. 

countstring("abc123") -> "equal"
countstring("hello123") -> "letters"
countstring("sdf12345") -> "numbers"
countstring("1£2$aAbBcC") -> "letters"
countstring("ASD£!((") -> "equal"

'''

def countstring(string):
    letter = 0
    number = 0

    for index in string:
        if index.isalpha():
            letter += 1
        elif index.isalnum():
            number += 1
        continue
        
    if letter == 0 or number == 0:
        return "equal"
    elif letter > number:
        return "letters"
    elif number > letter:
        return "number"
    else:
        return "equal"


print(countstring("abc123"))
print(countstring("hello123"))
print(countstring("sdf12345"))
print(countstring("1£2$aAbBcC"))
print(countstring("ASD£!(("))
