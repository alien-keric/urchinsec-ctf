def decrypt_message(encrypted, key):
    return ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])

def brute_force_decrypt(encrypted):
    for key in [chr(i) for i in range(32, 127)]:  # ASCII characters from space to ~
        decrypted = decrypt_message(encrypted, key)
        print("Key:", key, "| Decrypted message:", decrypted)

with open("enc", "r") as enc_file:
    encrypted = enc_file.read()

print("Brute forcing decryption for file 'enc':")
brute_force_decrypt(encrypted)
