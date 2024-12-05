import random
#2
def sorozat():
    szamok = []
    txt = ""
    for i in range(1, 9, 1):
        szamok.append(random.randint(-100, 860))
    for i in range(0, len(szamok)-1):
        print(szamok[i], end=";")
    print(szamok[len(szamok)-1])
    return szamok

def tizzel_oszthatoak_szama(szamok):
    db:int = 0
    for i in range(0, len(szamok)-1, 1):
        if(szamok[i] % 10 == 0):
            db += 1
    return db

def konzol_ir(db):
    print(f"Tízzel osztható számok száma: {db}")

def fajlba_ir(szamok):
    txt = ""
    for i in range(1, len(szamok)):
        txt += str(szamok[i]) + ";"
    txt += str(szamok[len(szamok)-1]) 
    f = open("vegeredmeny.txt", "a")
    f.write(txt)
    f.close()