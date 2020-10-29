<<<<<<< HEAD
  #word = input("Enter a word: ")

=======
>>>>>>> b50c481f30a8b292a055fb0ce52fb4b1c03ef34a
def wordconjugation(word):
    sub_list = list()
    with open("programs\wordbank.txt", "r") as readfile:
        for line in readfile:
            line = line.rstrip()
            if line in word and len(line) >= 2:
                sub_list.append(line)
        return sub_list

                
    
print(wordconjugation("awesomeness"))
print(wordconjugation("something"))
print(wordconjugation("disproportionate"))