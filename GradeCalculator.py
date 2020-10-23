maths = int(input("Please enter the Maths grade: "))
chem = int(input("Please enter the Chemistry grade: "))
phy = int(input("Please enter the Physics grade: "))
total = maths + chem + phy 
percent = total/3

def cal():
    if percent >= 70:
        return "A"
    elif percent >=60:
        return "B"
    elif percent >=50:
        return "C"
    elif percent >=40:
        return "D"
    else:
        return "You failed"
print ("Your percentage score is: " + str(round(percent)) + "%")
print ("You scored a grade of: " + cal())

        