import random

def miller_rabin():
    global n
    import math
    n = random.randint(1, 1000)
    print(n)
    k = round(math.log2(n))
    if n == 2 or n == 3:
        print('простое')
        return True
    if n < 2 or n % 2 == 0:
        print('составное')
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
                print('составное')
                return False
            if x == n - 1:
                break
        if x != n - 1:
            print('составное')
            return False
    print('простое')
    return True

miller_rabin()
            