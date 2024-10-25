arr = [2,3,4,5,5,5,5,5,5,7,9]
target = 5
def findFirst(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr)-1
    while left <= right:
        center = (left+right)//2
        if arr[center] == target and arr[center-1]<target:
            return center    
        elif arr[center] < target:
            left = center+1
        else:
            right = center-1 
    return -1
def findLast(arr, target):
    if arr[-1] == target:
        return len(arr)-1 
    left, right = 0, len(arr)-1
    while left <= right:
        center = (left+right)//2
        if arr[center] == target and arr[center+1]>target:
            return center    
        elif arr[center] > target:
            right = center-1
        else:
            left = center+1 
    return -1
def firstLast (arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]
    first = findFirst(arr, target)
    last = findLast(arr, target)
    return[first,last]

print(firstLast(arr, target))
