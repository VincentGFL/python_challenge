class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    class_ = "Student"

    def testscore(self, test1, test2, test3):
        total = test1 + test2 + test3
        avg = total / 3
        return avg

jake = Student("Jake", 30)

print(jake.testscore(50, 40, 60))    


