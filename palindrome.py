def isPalidrome(x):
    reversedNumber = 0
    number = x 
    
    while number > 0:
        digit = number % 10
        reversedNumber = reversedNumber * 10 + digit
        number //= 10
    if reversedNumber == x:
        return True
    return reversedNumber, False 

x = int(input("x="))
rr = isPalidrome(x)
print(rr)
# print(6789//10)