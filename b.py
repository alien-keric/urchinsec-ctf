def decrypt_caesar(ciphertext, key):
  """
  Decrypts a Caesar cipher using the provided key.

  Args:
      ciphertext: The encrypted message as a string.
      key: The key to use for decryption (a single character a-z, A-Z, or 1-9).

  Returns:
      The decrypted message as a string, or None if decryption fails.
  """
  try:
    # Convert key to its ASCII code
    key_code = ord(key)
  except TypeError:
    print(f"Invalid key type: {key}. Key must be a character.")
    return None

  decrypted = ''.join([
      chr(ord(char) ^ key_code) for char in ciphertext
  ])
  return decrypted

# Open the encrypted file
try:
  with open("enc", "r") as enc_file:
    ciphertext = enc_file.read()
except FileNotFoundError:
  print("Error: File 'enc' not found.")
  exit()

# Try all keys (a-z, A-Z, 1-9)
for key in range(ord('a'), ord('z') + 1):
  decrypted_text = decrypt_caesar(ciphertext, chr(key))
  if decrypted_text is not None:
    print(f"Decrypted with key '{chr(key)}': {decrypted_text}")

for key in range(ord('A'), ord('Z') + 1):
  decrypted_text = decrypt_caesar(ciphertext, chr(key))
  if decrypted_text is not None:
    print(f"Decrypted with key '{chr(key)}': {decrypted_text}")

for key in range(ord('1'), ord('9') + 1):
  decrypted_text = decrypt_caesar(ciphertext, chr(key))
  if decrypted_text is not None:
    print(f"Decrypted with key '{chr(key)}': {decrypted_text}")

print("Decryption attempts complete.")
