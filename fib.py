string="""
def fib (n, memo={}):
    if n in memo:
        return memo[n]
    if n <=2: 
        return 1
    else:
        memo[n] = fib(n-1, memo)+fib(n-2, memo)
        return memo[n]
    
  """      
from timeit import timeit

timeit("fib(300)", setup=string, number=300000)
# print(fib(2))
# print(fib(100))
