# Que:-Write aprogram that finds an element's index in a tuple WITHOUT using index()?
tuple1 = ('a','p','p','l','e')
char = input ("Enter a single letter without quotes:")
if char in tuple1 :
    count = 0
    for a in tuple1 :
        if a != char :
            count +=1
        else : 
            print (char, "is NOT in ", tuple1)
           