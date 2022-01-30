import random
import math

p = int(input("Введите первый множитель: "))
q = int(input("Введите второй множитель: "))
number = int(input("Введите число, которое нужно зашифровать: "))

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

if isPrime(p) == False or isPrime(q) == False:
    print("Число не является простым")

def function_euler():
    return (p - 1) * (q - 1)

def get_public_key():
    for e in range(100)[1:]:
        if isPrime(e) == True and function_euler() % e != 0 and e < function_euler():
            return p * q, e

print("Публичный ключ: ", get_public_key())

def get_private_key():
    for d in range(100)[6:]:
        if d * get_public_key()[1] % function_euler() == 1:
            return d, get_public_key()[0]

print("Приватный ключ: ", get_private_key())
print("Шифруем число: ", number)
crypt = number ** get_public_key()[1]
crypt %= get_public_key()[0]
print("Зашифрованное число: ", number, "равно: ", crypt)

# Расшифровываем с помощью личного ключа
print("Расшифровываем число ", crypt)
decrypt = crypt ** get_private_key()[0] % get_private_key()[1]
print("Расшифрованное число: ", decrypt)



