

def evenFilter(arr):
    evens = []
    for num in arr:
        if num%2 == 0:
            evens.append(num)
    return evens

arr =[1,2,4,5,6,0,3]      
print(evenFilter(arr))