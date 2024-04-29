with open("enc", "r") as enc_file:
    encrypted = enc_file.read()

key = 'a'  # key comes here
decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])

print(decrypted)
