import re

file = open("1984.txt")
text = file.read().lower()

key = int(input('Введите ключ '))
abc = 'марш'
decode_text = ''
c = 0
for sym in text:
    if sym.isalpha():
        decode_text += abc[(abc.find(sym) + key) % 33]
    else:
        decode_text += sym

monograms_text = {}
p = re.compile(r'[\w]{1}')
for i in p.findall(text):
    if i in monograms_text:
        monograms_text[i] += 1
    else:
        monograms_text[i] = 1

monograms_decode_text = {}
p = re.compile(r'[\w]{1}')
for i in p.findall(decode_text):
    if i in monograms_decode_text:
        monograms_decode_text[i] += 1
    else:
        monograms_decode_text[i] = 1

list_monograms_text = list(monograms_text.items())
list_monograms_text.sort(key=lambda i: i[1])

list_monograms_decode_text = list(monograms_decode_text.items())
list_monograms_decode_text.sort(key=lambda i: i[1])

bigram_text = {}
p = re.compile(r'[\w]{2}')
for i in p.findall(text):
    if i in bigram_text:
        bigram_text[str(i)] += 1
    else:
        bigram_text[str(i)] = 1

bigram_decode_text = {}
p = re.compile(r'[\w]{2}')
for i in p.findall(decode_text):
    if i in bigram_decode_text:
        bigram_decode_text[str(i)] += 1
    else:
        bigram_decode_text[str(i)] = 1

list_bigram_text = list(bigram_text.items())
list_bigram_text.sort(key=lambda i: i[1])

list_bigram_decode_text = list(bigram_decode_text.items())
list_bigram_decode_text.sort(key=lambda i: i[1])

for i in range(len(list_bigram_decode_text)):
    item1 = list_bigram_text.pop()
    item2 = list_bigram_decode_text.pop()
    if item2[1] == item1[1]:
        decode_text = decode_text.replace(str(item2[0]), str(item1[0]))
    else:
        break
print(decode_text)

for i in range(len(list_monograms_decode_text)):
    item1 = list_monograms_text.pop()
    item2 = list_monograms_decode_text.pop()
    if item2[1] == item1[1]:
        decode_text = decode_text.replace(str(item2[0]), str(item1[0]))
    else:
        break
decode_text
