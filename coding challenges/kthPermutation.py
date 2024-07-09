#n,k where n is integer and k is the permutation for ordering the integers

def kPerm(n,k):
    perm = []
    unused = list(range(1, n+1))
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i * fact[i-1]

    k -= 1
    while n > 0:
        part = fact[n]//n
        i = k//part
        perm.append(unused[i])
        unused.pop(i)
        n -= 1
        k %= part

    return ''.join(map(str, perm))

