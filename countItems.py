def countItem(arr):
    hashi = {} 
    for i in arr:
        if i in hashi:
            hashi[i] += 1 
    return hashi

arr =[1,1,2,2,3,3,3,5,4,4,7,7,8,8,7]
print(countItem(arr))