"""
def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)

print(added_number + 20)
"""
#----------------------------------
#name = input("Please enter your name: ")
#homework = int(input("Please enter your homework score /25: "))
#assessment = int(input("Please enter your assessment score /50: "))
#exam = int(input("Please enter your final exam score /100: "))

def grade(name, homework, assessment, exam):
    finalgrade = round(((homework + assessment + exam) / 175)* 100, 2)
    #return finalgrade

    if finalgrade >= 70:
        return (name + ", You scored A!" + " " + str(finalgrade)+ "%")
    elif finalgrade < 70 and finalgrade > 60:
        return (name + ", You scored B!" + " " + str(finalgrade)+ "%")
    elif finalgrade < 60 and finalgrade > 50:
        return (name + ", You scored C!" + " " + str(finalgrade)+ "%")
    elif finalgrade < 50 and finalgrade > 40:
        return (name + ", You scored D!" + " " + str(finalgrade)+ "%")
    else:
        return (name + "You have failed" + " " + str(finalgrade)+ "%")
    
print(grade("David", 12, 45, 40))