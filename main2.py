#activity 2

#to find factor of numbers

def factor(number):
    print("the factors of number are")
    for i in range(1,number+1):
        if number %i ==0:
            print(i)

 #taking user input
number= int(input("enter number to find factors"))  
factor (number)        