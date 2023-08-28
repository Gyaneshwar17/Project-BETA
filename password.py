k=[]
print("Welcome To Password Generator: ")
a=int(input("-> Enter the count of small and big\n   alphabets u want in ur password : "))
b=int(input("-> Enter the count of number u want : "))
c=int(input("-> Enter the count of speical  u want : "))
print(f"Generating a strong password with {a} aphabets,{b} numbers ,{c} symbols...")
import random
for i in range(a):
    d=random.randint(65,123)
    k.append(chr(d))
for j in range(b):
    e=random.randint(48,58)
    k.append(chr(e))
for m in range(c):
    f=random.randint(33,49)
    k.append(chr(f))
random.shuffle(k)
print("This is your password :")
for o in k:
    print(o,end="")
