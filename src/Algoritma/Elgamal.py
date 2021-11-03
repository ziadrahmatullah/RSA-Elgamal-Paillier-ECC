import random
from util import *

def generateKeyG(p , g, x):
    y = modexp(g, x, p)
    return {
		'publicKey': (p,g,y), 
		'privateKey': (p,x)
	}

def encryptG(publicKey, sPlaintext):
		m = encode(sPlaintext)
		p , g, y = publicKey
		cipher_pairs = []
		for i in m:
				k = random.randint( 0, p )
				a = modexp( g, k, p)
				b = (i*modexp( y, k, p)) % p
				cipher_pairs.append( [a, b] )
		encryptedStr = ""
		for pair in cipher_pairs:
				encryptedStr += str(pair[0]) + ' ' + str(pair[1]) + ' '
		return encryptedStr

def decryptG(privateKey, cipher):
		plaintext = []
		p, x = privateKey
		cipherArray = cipher.split()
		if (not len(cipherArray) % 2 == 0):
				return "Malformed Cipher Text"
		for i in range(0, len(cipherArray), 2):
				a = int(cipherArray[i])
				b = int(cipherArray[i+1])
				s = modexp( a, x, p )
				plain = (b*modexp( s, p-2, p)) % p
				plaintext.append( plain )
		decryptedText = decode(plaintext)
		return decryptedText

# key = generateKeyG(2357, 2, 1751)
# print(key["publicKey"])
# print(key["privateKey"])
# text = "HELLO ALICE, Apa yang terjadi?"
# ciphertext = encryptG(key['publicKey'], text)
# print(ciphertext)
# print(decryptG(key['privateKey'], ciphertext))

