# Операция деления по модулю является хеш-функцией.
input_text = input("Введите текст: ")

print("Исходное значение: ", input_text)

def get_hash():
    new_text = str()
    for symbol in range(len(input_text)):
        if symbol % 7 == 0:
            new_text += input_text[symbol]
        
    return new_text

print("HASH для введенного текста: ", get_hash())
