import random
from math import gcd

def Prime_Numbers(x, y):
    global P,Q
    prime_list = []
    for n in range(x, y):
        Check_Prime = True
        for num in range(2, n):
            if n % num == 0:
                Check_Prime = False
        if Check_Prime:
            prime_list.append(n)
    
    P_index = random.randint(0, len(prime_list)-1)
    P = prime_list[P_index]
    Q_index = random.randint(0, len(prime_list)-1)
    Q = prime_list[Q_index]    
    return P, Q

def Co_Prime(Phi):
    for i in range(2, Phi):
        if gcd(Phi,i) == 1:
            e = i
            break
    return e
    
def extended_Euclidean (e, Phi):
    for x in range(1,Phi):
        if((e%Phi)*(x%Phi) % Phi==1):
            return x
    raise Exception('The modular inverse does not exist.')

Prime_Numbers(1, 9999)
print("The prime numbers are", P,",",Q)
N = P * Q
print("The value of N is: ", N)
Phi = (P - 1) * (Q - 1)
print("The value of Phi is: ", Phi)
e = Co_Prime(Phi)
print("The value of e is: ", e)
d = extended_Euclidean (e, Phi)
print("The value of d is: ", d)
encodedMsg = 1234567
print(encodedMsg)
encryptedMsg = pow(encodedMsg, e, N)
print(encryptedMsg)
decryptedMsg = pow(encryptedMsg, d, N)
print(decryptedMsg)


def Prime_Number(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
        return True
    
def RSA_Algorithm(P, Q):
    N = P * Q
    Phi = (P - 1) * (Q - 1)
    e = Co_Prime(Phi)
    d = extended_Euclidean (e, Phi)
    return N, Phi, e, d

def Co_Prime(Phi):
    for i in range(2, Phi):
        if gcd(Phi,i) == 1:
            e = i
            break
    return e

def extended_Euclidean (e, Phi):
    for x in range(1,Phi):
        if((e%Phi)*(x%Phi) % Phi==1):
            return x
    raise Exception('The modular inverse does not exist.')

while True:
    P = int(input("Enter Number P: "))
    Q = int(input("Enter Number Q: "))
    if Prime_Number(P) & Prime_Number(Q):
        N, Phi, e, d = RSA_Algorithm(P,Q)
        print("The prime numbers are", P,",",Q)
        print("The value of N is: ", N)
        print("The value of Phi is: ", Phi)
        print("The value of e is: ", e)
        print("The value of d is: ", d)
        break
    else:
        print("One of your number is not Prime number please input numbers again..!")
        P = int(input("Enter Number P: "))
        Q = int(input("Enter Number Q: "))
        print("One of your number is not Prime number please input numbers again..!")
        