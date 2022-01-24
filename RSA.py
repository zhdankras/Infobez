import rsa
key = rsa.newkeys(3000) # Создать случайный ключ
privateKey = key [1] # личный ключ
publicKey = key [0] # открытый ключ
message = 'Text'
print('Before encrypted:', message)
message = message.encode()
cryptedMessage = rsa.encrypt(message, publicKey)
print('After encrypted:\n',cryptedMessage)
message = rsa.decrypt(cryptedMessage, privateKey)
message = message.decode()
print('After decrypted:',message)

