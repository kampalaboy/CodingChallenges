using System;
using System.Collections.Generic;
using System.Numerics;

// Dictionary for memoization
Dictionary<int, BigInteger> memo = new Dictionary<int, BigInteger>();

BigInteger Fib(int n)
{
    // Check if already calculated
    if (memo.ContainsKey(n))
    {
        return memo[n];
    }
    
    // Base cases
    if (n <= 2)
    {
        return 1;
    }
    
    // Calculate and store result
    memo[n] = Fib(n - 1) + Fib(n - 2);
    return memo[n];
}

try
{   int n = 300;
    BigInteger result = Fib(n);
    Console.WriteLine($"The {n}th Fibonacci number is:" );
    Console.WriteLine(result);

}
catch (Exception ex)
{
    Console.WriteLine($"An error occurred: {ex.Message}");
}