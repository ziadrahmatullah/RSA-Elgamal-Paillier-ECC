from util import *

def generateKeyR(p, q, e):
    n = p*q
    phi = (p-1) * (q-1)
    if (gcd(phi, e) != 1):
        return TypeError
    d = modinv(e,1, phi)[0]
    # d = multiplicativeInverse(e, 1, phi)[0]
    return {
        "public": (e, n),
        "private": (d, n)
    }

def encryptR(publicKey, plainText):
    e, n = publicKey
    encoded = encode(plainText)
    result = [modexp(char, e, n) for char in encoded]
    return result

def decryptR(privateKey, cipherText):
    d, n = privateKey
    result = [str(modexp(int(char), int(d), n)) for char in cipherText]
    result = decode(result)
    return ''.join(result)

key  = generateKeyR(47 , 71, 79)
print(key["public"])
print(key["private"])
text = "HELLO ALICE, Apa yang terjadi?"
ciphertext = encryptR(key["public"], text)
print(ciphertext)
plaintext = decryptR(key["private"], ciphertext)
print(plaintext)