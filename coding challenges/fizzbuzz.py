# Create a program that introducing a number it return a list that starts on 1 and ends with that number. 
# Every time a number in that list is divisible by 3 replace the number with "fizz". 
# Every time a number is divisible by 5 replace the number with "buzz".
# When a number is divisible between 3 and 5 at the same time replace with "fizzbuzz".
def fizzbuzz(n):
    arr = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("fizzbuzz")
        elif i % 3 == 0:
            arr.append("fizz")
        elif i % 5 == 0:
            arr.append("buzz")
        else:
            arr.append(i)
    return arr

target = 15
result = fizzbuzz(target)
print(result)
