"""poschodia=0
ludia=0
while ludia<10:
    ludia=int(input("zadaj počet ľudi: "))
    ludia+=ludia
print(ludia)"""


"""x=2
while x > 10:
    x=x+3
print(x)"""

"""poschodie=0
while poschodie<7:
    poschodie +=1
    print("výťah je na ",poschodie, "poschodí")
print("výťah zastavil")"""

"""osoby=0
hmotnost=0
while hmotnost<400:
    osoby +=1
    vaha=int(input("zadaj váhu: "))
    hmotnost+=vaha
    print("počet osôb je:", osoby, "celkova hmotnost je:", hmotnost)
print("hmotnosť výťahu je prekročená ")"""

import random
cislo=random.randint(1,10)
tip=0
while tip!=x:
    tip=int(input("hadaj čislo: "))
    if tip > cislo:
        print("číslo je menšie ")
    else:
        print("číslo je väčšie ")
print("uhadol si")
