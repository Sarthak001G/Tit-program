#Write a program to print one of the words negative ,zero,or,positive,according to whether variable x is less than zero, zero, or greater thn zero, respectively
L =  (1,-2,0)
for i in range(len(L)) :
    if L[i] >= 0:
        print ('No is positive')
    elif L[i] <= 0:
        print ('No is negative')
    else :
        print ('No is 0')