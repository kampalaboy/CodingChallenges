def howSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]  
    if target == 0: 
        return []  # Return an empty list instead of True
    if target < 0:
        return None
    
    unique = set(numbers)  # Convert numbers to a set to remove duplicates
    for num in unique:  # Iterate over unique elements
        r = target - num
        rr = howSum(r, numbers, memo)
        if rr is not None:
            # Check if num is not already present in rr
            if num not in rr:
                memo[target] = rr + [num]
                return memo[target]
  
    memo[target] = None
    return None

print(howSum(30, [5, 13,20,10]))
print(howSum(3546,[70,2500, 17]))