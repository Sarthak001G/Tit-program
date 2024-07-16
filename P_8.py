#Write a program to print a square multiplicationtable as shown below :
for row in range (1,10):
    for col in range (1,10):
        prod = row * col
        if prod < 10 :
            print (' ',prod , ' ', end = ' ')
        else :
            print (prod, ' ', end = ' ')
    print()    
