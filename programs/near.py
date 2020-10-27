def near(string1, string2):
    if list(set(string1)) == list(set(string2)):
        return True
    else:
        return False

print(near("reset", "rest"))
print(near("dargoon", "dargon"))
print(near("eave", "leave"))
print(near("sleet", "lets"))