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
