from util import *
import random

def lFunction(x, n):
    return (x-1)/n

def generateKeyP(p, q):
    n = p*q
    l = lcm(p-1, q-1)
    g = random.randint( 0, pow(n,2)-1)
    u = modinv( lFunction( modexp(g,int(l), pow(n,2) ) ,n) ,1,  n)[0]
    return{
        'publicKey' : (g,n),
        'privateKey' : (l, u,n)
    }

def encryptP(publicKey, plainText):
    encoded = encode(plainText)
    g, n = publicKey
    r = n
    n2 = pow(n,2)
    while(gcd(r,n) != 1):
        r = random.randint(0, n-1)
    result = [modexp(modexp(g, char, n2)*modexp(r,n,n2),1,n2) for char in encoded]
    return result

def decryptP(privateKey, cipherText):
    l, u, n = privateKey
    n2 = pow(n,2)
    lFunct = [lFunction(modexp(char, int(l), n2),n) for char in cipherText]
    result = [modexp(int(char)*int(u), 1, n) for char in lFunct]
    result = decode(result)
    return result

# P*Q harus diatas 256
# key = generateKeyP(17, 19)
# print(key)
# text = "HELLO ALICE, Apa yang terjadi?"
# ciphertext = encryptP(key['publicKey'], text)
# print(ciphertext)
# plaintext = decryptP(key['privateKey'], ciphertext)
# print(plaintext)