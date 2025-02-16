def ceaeasar_encrypt(plaintext, k):
    result = ""
    for char in plaintext:
        if char.isalpha():  
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char  
    return result

plaintext = "TRANTHILEGIANG"
k = 8
ciphertext = ceaeasar_encrypt(plaintext, k)
print("Ciphertext:", ciphertext)
