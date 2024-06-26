import random
from math import pow
a=random.randint(2,10)

def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)

def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c
#For asymetric encryption
def encryption(message,q,h,g):
    ct=[]
    k=gen_key(q)
    S=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(message)):
        ct.append(msg[i])
    print("g^k used= ",p)
    print("g^ak used= ",S)
    for i in range(0,len(ct)):
        ct[i]=S*ord(ct[i])
    return ct,p

def decryption(ct,p,key,q):
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt
    message=input("Enter message.")
q=random.randint(pow(10,20),pow(10,50))
g=random.randint(2,q)
key=gen_key(q)
h=power(g,key,q)
print("g used=",g)
print("g^a used=",h)
ct,p=encryption(message,q,h,g)
print("Original Message is :",msg)
print("Encrypted Maessage is : ",ct)
pt=decryption(ct,p,key,q)
d_msg=''.join(pt)
print("Decryted Message=",d_msg)
def gen_key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key