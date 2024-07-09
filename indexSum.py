from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int, memo: object={}) -> List[int]:
        if target in memo:
            return memo[target]
        if target == 0:
            return []  # Return an empty list instead of True
        if target < 0:
            return None      
        num_indices = {}  # Dictionary to store indices of each number
        for i, num in enumerate(nums):
            if num not in num_indices:
                num_indices[num] = [i]
            else:
                num_indices[num].append(i)
        for num in num_indices:
            r = target - num
            if r in num_indices:
                if r == num:
                    if len(num_indices[r]) >= 2:
                        memo[target] = [num_indices[r][0], num_indices[r][1]]
                        return memo[target]
                else:
                    memo[target] = [num_indices[num][0], num_indices[r][0]]
                    return memo[target]
        memo[target] = None
        return None

# Create an instance of Solution
sol = Solution()
# Call the twoSum method on the instance
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))


# def howSum(target, numbers, memo={}):
#     if target in memo:
#         return memo[target]  
#     if target == 0: 
#         return []  # Return an empty list instead of True
#     if target < 0:
#         return None
    
#     # unique = set(numbers)  # Convert numbers to a set to remove duplicates
#     for num in numbers:  # Iterate over unique elements
#         r = target - num
#         rr = howSum(r, numbers, memo)
#         if rr is not None:
#             # Check if num is not already present in rr
#             if num not in rr:
#                 index = numbers.index(num)
#                 if index not in rr:
#                     memo[target] = rr + [index]
#                     return memo[target]
  
#     memo[target] = None
#     return None

# print(howSum(30, [5, 13,20,10]))
# print(howSum(3546,[70,2500, 17]))