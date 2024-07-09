
def canSum (target, numbers,memo={}):
    if target in memo:
        return memo[target]  
    if target == 0: 
        return True
    if target < 0:
        return False
    
    for num in numbers:
        r = target - num
        if (canSum(r, numbers, memo)==True):
            memo[target]=True
            return True
  
    memo[target]=False
    return False

print(canSum(300,[150]))
