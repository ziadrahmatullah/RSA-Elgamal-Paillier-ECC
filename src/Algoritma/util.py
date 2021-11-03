import math

def gcd( a, b ):
		while b != 0:
			c = a % b
			a = b
			b = c
		return a

def isPrime(num):
    factors = 0
    if (num == 1 or num == 0):
        return False
    if (num < 4):
        return True
    for x in range(1, math.ceil(math.sqrt(num))+1):        
        difference = num/x
        if (difference).is_integer():
            factors += 1
            if (factors == 2):
                return False
    return True

def findGcdUp(a):
	b = a
	while(gcd(a,b)!=1 or not isPrime(b)):
		b += 1
	return b

def findGcdDwon(a):
	b = a
	while(gcd(a,b)!=1 or not isPrime(b)):
		b -= 1
	return b

def lcm(a, b):
    return a * b / gcd(a, b)

def egcd(num1, num2):
    if num2 == 0:
        return (num1, 1, 0)
    d, temp_x, temp_y = egcd(num2, num1 % num2)
    x, y = temp_y, temp_x - int(num1 / num2) * temp_y
    return (d, x, y)

def modinv(a, b, n):
    d, x, y = egcd(a, n)
    if b % d == 0:
        temp_x = (x * (b/d)) % n
        result = []
        for i in range(int(d)):
            result.append((temp_x + i*(n/d)) % n)
        return result
    return []

def modexp( base, exp, modulus ):
		return pow(base, exp, modulus)

def encode(text):
    result = [ord(char) for char in text]
    return result

def decode(text):
    newText = [chr(int(char)) for char in text]
    return ''.join(newText)

# TODO kasih saran key pailier