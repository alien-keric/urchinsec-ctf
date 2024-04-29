message = 'urchinsec{fake_flag}' # message comes here
key = 'a' # key comes here
encrypted = ''.join([chr(ord(x) ^ ord(key)) for x in message])
with open("enc", "w") as enc:
    enc.write(encrypted)

print("encrypted")
