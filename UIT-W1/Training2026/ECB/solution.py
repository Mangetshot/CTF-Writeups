from Crypto.Cipher import AES

ciphertext = bytes.fromhex('a58fd383d77105ed4cec2ff0eb3e483dea0d8bf2d963ce6e61a7c875a8b4edea') # Chuyển hex về dạng bytes

for key_int in range(1_000_001):
    print(f"Current key attempt: {key_int}")
    key = key_int.to_bytes(16, 'big') # Chuyển integer về dạng bytes
    plaintext = AES.new(key, AES.MODE_ECB).decrypt(ciphertext)

    for digit in plaintext: # digit là các giá trị ASCII (0-127) tương ứng với từng byte trong plaintext
        if digit < 32 or digit > 126: #Ngoài khoảng kí tự ASCII có thể hiển thị (\n, DEL,...)
            break
    else: #Tất cả kí tự đều hiển thị được, đúng với format của flag
        print(f"Key found: {key_int}")
        print(f"Plaintext recovered: {plaintext}")
        break
