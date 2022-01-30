import random, math 

def isPrime(n):
    k = round(math.log2(n))
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
 
    t = int(n - 1)
    s = 0
    while t % 2 == 0:
        t /= 2
        s += 1
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, int(t), n)
        if x == 1 or x == n - 1:
            continue
        for i in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        if x != n - 1:
            return False
    return True

print(isPrime(3))