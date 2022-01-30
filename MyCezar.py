al = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюябвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input("Введите текст: ") 
key = int(input("Введите ключ: "))

def encrypt():
    encrypt = str()
    for letter in text.lower():
        position = al.find(letter)
        if letter in al:
            encrypt = encrypt + al[position + key]
        else:
            encrypt = encrypt + letter
    
    return encrypt

def get_dict_monogram(s = None):
    mono = dict()
    for i in s:
        mono[i] = s.count(i)
    
    return mono

def get_dict_bigram(s):
    bigram = dict()
    s = [s[i:i+2] for i in range(0, len(s), 2)]
    for i in s:
        bigram[i] = s.count(i)
    
    return bigram

print("Зашифрованный текст: ", encrypt())
print("Монограммы в не зашифрованном тексте: ", get_dict_monogram(text))
print("Монограммы в зашифрованном тексте: ", get_dict_monogram(encrypt()))
print("Биграммы в не зашифрованном тексте: ", get_dict_bigram(text)) 
print("Биграммф в зашифрованом тексте: ", get_dict_bigram(encrypt()))