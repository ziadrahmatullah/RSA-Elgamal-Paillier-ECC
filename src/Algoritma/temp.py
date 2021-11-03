def egcd(num1, num2):
    if num2 == 0:
        return (num1, 1, 0)
    d, temp_x, temp_y = extendedEuclidean(num2, num1 % num2)
    x, y = temp_y, temp_x - int(num1 / num2) * temp_y
    return (d, x, y)

def modinv(a, b, n):
    d, x, y = extendedEuclidean(a, n)
    if b % d == 0:
        temp_x = (x * (b/d)) % n
        result = []
        for i in range(d):
            result.append((temp_x + i*(n/d)) % n)
        return result
    return []

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m