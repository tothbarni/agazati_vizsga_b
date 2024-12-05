from Huzas import Huzas
def beolvas(fajlnev, huzas=[]):
    fajlom = open(fajlnev, "r", encoding="UTF-8")
    elso_sor = fajlom.readline()
    tobbi_sor = fajlom.readlines()
    
    for i in range(0, len(tobbi_sor), 1):
        sor = tobbi_sor[i].strip()
        sor_lista = sor.split("@")
        lotto = Huzas(int(sor_lista[0]), int(sor_lista[1]), int(sor_lista[2]), int(sor_lista[3]))
        huzas.append(lotto)
    fajlom.close()
    return huzas

def huzasok(lotto):
    print(f"A húzások száma: {lotto[-1].huzas}")

def atlag(lotto):
    db = 0
    osszeg = 0
    for i in range(0, len(lotto)):
        if lotto[i].het == 43:
            osszeg += lotto[i].szam 
            db += 1 
    return osszeg / db

def legn_huzas(lotto):
    legn:int = 0
    indexe:int = 0
    for i in range(0, len(lotto)):
        if (legn < lotto[i].szam) and (lotto[i].ev == 1990):
            legn = lotto[i].szam
            indexe = i
    print(f"Az első legnagyobb kihúzott szám értéke: {legn}, {lotto[indexe].ev}-ben, a {lotto[indexe].het}. héten húzták ki, ez volt a {lotto[indexe].huzas}. húzás.")