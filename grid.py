def gridTravel(m,n,memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m ==1 and n==1:
        return 1
    if m ==0 or n==0:
        return 0
    
    memo[(m,n)]=gridTravel(m-1,n, memo)+gridTravel(m,n-1,memo)
    # if m < n:
    #     m, n = n, m  # Ensure m is greater than or equal to n
    # reduced_m = m // ratio # Reduce the number of rows
    # memo[(m,n)] = gridTravel(reduced_m, n, ratio, memo) ** ratio 
  
    return memo[(m,n)]


print (gridTravel(3,3))