g = int(input("Введите общее число g: "))
p = int(input("Введите общее число p: "))

def get_number_Alice(a):
    return (g ** a) % p

def get_number_Bob(b):
    return (g ** b) % p

print("Число Элис: ", get_number_Alice(23))
print("Число Боба: ", get_number_Bob(12))
print(get_number_Alice(23) == get_number_Bob(12))