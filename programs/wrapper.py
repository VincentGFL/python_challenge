def decoration(func):
    def function_upper(string1):
        return string1.upper()
    return function_upper

@decoration
def string_upper(string):
    return string

print(string_upper("poggers"))