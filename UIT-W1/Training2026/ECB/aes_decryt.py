from Crypto.Cipher import AES

ciphertext = bytes.fromhex('a58fd383d77105ed4cec2ff0eb3e483dea0d8bf2d963ce6e61a7c875a8b4edea')

for key_int in range(1_000_001):
    print(f"Current key attempt: {key_int}")
    key = key_int.to_bytes(16, 'big')
    plaintext = AES.new(key, AES.MODE_ECB).decrypt(ciphertext)

    for digit in plaintext:
        if digit < 32 or digit > 126: #Out of printable ASCII range
            break
    else:
        print(f"Key found: {key_int}")
        print(f"Plaintext recovered: {plaintext}")
        break
