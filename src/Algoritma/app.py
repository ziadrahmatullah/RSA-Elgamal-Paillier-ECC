from Elgamal import *
from Paillier import *
from RSA import *

x = 0
while(x!=5):
    print("="*50)
    print("Selamat Datang di Cryptography")
    print("Pilih Algoritma yang diinginkan : ")
    print("1. RSA")
    print("2. Elgamal")
    print("3. Paillier")
    print("4. ECC")
    print("5. Exit")
    x = int(input("Enter 1/2/3/4 : "))
    if (x == 1):
        a = 0
        while(a != 4):
            print("="*50)
            print("Pilih kegiatan RSA : ")
            print("1. Enkripsi")
            print("2. Dekripsi")
            print("3. Pembangkitan Kunci")
            print("4. Back")
            a = int(input("Enter 1/2/3/4 : "))
            if(a == 1):
                print("="*50)
                e = int(input("e : "))
                n = int(input("n : "))
                plain = str(input("Plaintext : "))
                encrypted = encryptR((e,n), plain)
                for i in encrypted:
                    print(i, end =" ")
                print("\n")
            elif(a==2):
                print("="*50)
                d = int(input("d : "))
                n = int(input("n : "))
                chiper = list(map(int,input("Chipertext : ").strip().split()))[:n]
                decrypted = decryptR((d,n), chiper)
                print(decrypted)
                print("\n")
            elif(a == 3):
                print("="*50)
                p = int(input("p : "))
                q = int(input("q : "))
                e = int(input("e : "))
                key = generateKeyR(p,q,e)
                print(key)
                print("\n")
            elif(a==4):
                break
            else:
                print("Wrong Type")
    elif(x == 2):
        b = 0
        while(b != 4):
            print("="*50)
            print("Pilih kegiatan Elgamal : ")
            print("1. Enkripsi")
            print("2. Dekripsi")
            print("3. Pembangkitan Kunci")
            print("4. Back")
            b = int(input("Enter 1/2/3/4 : "))
            if(b == 1):
                print("="*50)
                p = int(input("p : "))
                g = int(input("g : "))
                y = int(input("y : "))
                plain = str(input("Plaintext : "))
                encrypted = encryptG((p,g,y), plain)
                print(encrypted)
                print("\n")
            elif(b==2):
                print("="*50)
                p = int(input("p : "))
                x = int(input("x : "))
                chiper = str(input("Chipertext : "))
                # chiper = list(map(int,input("Chipertext : ").strip().split()))[:n]
                decrypted = decryptG((p,x), chiper)
                print(decrypted)
                print("\n")
            elif(b == 3):
                print("="*50)
                p = int(input("p : "))
                g = int(input("g : "))
                x = int(input("x : "))
                key = generateKeyG(p,g,x)
                print(key)
                print("\n")
            elif(b==4):
                break
            else:
                print("Wrong Type")
    elif (x == 3):
        c = 0
        while(c!=4):
            print("="*50)
            print("Pilih kegiatan Paillier : ")
            print("1. Enkripsi")
            print("2. Dekripsi")
            print("3. Pembangkitan Kunci")
            print("4. Back")
            c = int(input("Enter 1/2/3/4 : "))
            if(c == 1):
                print("="*50)
                g = int(input("g : "))
                n = int(input("n : "))
                plain = str(input("Plaintext : "))
                encrypted = encryptP((g,n), plain)
                for i in encrypted:
                    print(i, end =" ")
                print("\n")
            elif(c==2):
                print("="*50)
                l = int(input("l : "))
                u = int(input("u : "))
                n = int(input("n : "))
                chiper = list(map(int,input("Chipertext : ").strip().split()))[:n]
                decrypted = decryptP((l,u,n), chiper)
                print(decrypted)
                print("\n")
            elif(c == 3):
                print("="*50)
                p = int(input("p : "))
                q = int(input("q : "))
                key = generateKeyP(p,q)
                print(key)
                print("\n")
            elif(c==4):
                    break
            else:
                print("Wrong Type")
    elif(x==4):
        d = 0
        while(d!=1):
            print("="*50)
            print("Not Implemented")
            print("1. Back")
            d = int(input("Enter 1 : "))
        if(d != 1):
            print("Wrong Type")
    else:
        print("Wrong Type")
