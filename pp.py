def decrypt_message(encrypted, key):
    return ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])

def brute_force_decrypt(encrypted):
    for key in [chr(i) for i in range(49, 58)] + [chr(i) for i in range(97, 123)]:  # ASCII characters for 1-9 and a-z
        decrypted = decrypt_message(encrypted, key)
        print("Key:", key, "| Decrypted message:", decrypted)

with open("enc", "r") as enc_file:
    encrypted = enc_file.read()

print("Brute forcing decryption for file 'enc':")
brute_force_decrypt(encrypted)
