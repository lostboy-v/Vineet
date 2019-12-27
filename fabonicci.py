 init = int(input("Enter Any Number"))  #let you to enter any number 

n1,n2 = 0,1          
count = 0

if init<0:                 
    print("Enter Positive Number")      #if number is 0 or below 0
elif init==1:
    print("Fabonicci Series is",init,":")

else:
    print("Fabonicci Series of ", init, ":")
    while count<init:                   # count must be smaller than entered number
        print(n1)                       # print(n1), which is 0, Start of fabonicci series will be 0 always
        nterm = n1 + n2                 
        n1 = n2
        n2 = nterm
        count = count + 1
