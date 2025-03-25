def hashing(s):
    

    for i in s :
        if ((ord(i) >= 65 and ord(i) <= 91) or (ord(i) >= 97 and ord(i) <= 123)):
             print(chr(ord(i)+1), end = "")
        else:
            print (chr(ord(i)),end = "")

       
s = input("enter:-") 
hashing(s)
        