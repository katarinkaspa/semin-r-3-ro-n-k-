for i in range (1,11):
    print(i)

N= int(input("zadaj číslo:"))
for m in range (1,N+1):
    print(m)

N=int(input("zadaj číslo:" ))
for r in range (1,N+1):
    print(r, end=",")

Y=int(input("zadaj číslo:"))
for n in range (1,11):
    if n == 10:
        print(n, end=".")
    else:
        print(n, end= ",")

Z=int(input("zadaj číslo:"))
for z in range (5,Z+1,2):
    print(z, end=",")
