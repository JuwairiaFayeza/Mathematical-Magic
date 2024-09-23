number=int(input("enter a number to check armstrong number or not"))
result= 0 
tempt= number
while tempt!= 0:
    digit= tempt% 10
    result= result+digit**3

    tempt= tempt//10
print(result)
if number==result:
    print("number is armstrong", number)
else : 
    print("it is not armstrong numer", number)