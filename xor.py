encrypted = "" # encrypted message comes here
key = 'a' # key comes here
decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])

print(decrypted)
