#word = input("Enter a word: ")

def wordconjugation(word):
    with open("wordbank.txt", "r") as readfile:
        for line in readfile:
            if word in line:
                return word
                #return True
                
    
print(wordconjugation("awesomeness"))