  #word = input("Enter a word: ")

def wordconjugation(word):
    with open("wordbank.txt", "r") as readfile:
        for line in readfile:
            #print(line)
            if word in line:
                #return list(word)
                print(line)
                return word.partition(word)
                #return True
                
    
print(wordconjugation("awesomeness"))