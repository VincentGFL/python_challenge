total = 0

isbn_code = input("Please enter the first 12 digit of the ISBN seperate with space: ")
isbn = isbn_code.split()

for i in range (len(isbn)):
    if i%2 == 0:
        total += int(isbn[i])
    else:
        total += int(isbn[i])*3
digit_12 = 10 - (total%10)
print(digit_12) 