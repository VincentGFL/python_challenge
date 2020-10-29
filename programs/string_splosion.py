'''
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

'''

def string_splosion(str):
    if len(str) != 0:
        index = 0
        newstr = ""
        newstr2 = ""
        while index <= len(str)-1:
            newstr = "".join(str[:index+1]) 
            index += 1 
            newstr2 += newstr
        return newstr2

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))