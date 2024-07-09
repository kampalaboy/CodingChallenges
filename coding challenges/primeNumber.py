

def primerMultiply(n: int):
    prime_factors = []
    
    def is_prime(num):
        if num <= 1:
            return False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                return False
        return True
    
    # Unique Prime Factors
    # for i in range(2, n + 1):
    #     if n % i == 0 and is_prime(i):
    #         prime_factors.append(i)

    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            while n % i == 0:
                prime_factors.append(i)
                n //= i
        i += 1

    return prime_factors

print(primerMultiply(2000))
