g = int(input("Введите общее число g: "))
p = int(input("Введите общее число p: "))
a = int(input("Введите число для Алисы: "))
b = int(input("Введите число для Боба: "))

def get_number_Alice(a):
    return (g ** a) % p

def get_number_Bob(b):
    return (g ** b) % p

A = get_number_Alice(a)
B = get_number_Bob(b)

def get_parse_number_Alice(A):
    return (A ** b) % p

def get_parse_number_Bob(B):
    return (B ** a) % p

if get_parse_number_Alice(A) == get_number_Bob(B):
    print("Общее число, равно: ", get_parse_number_Alice(A))
