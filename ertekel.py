#1
kek = "\033[34m"
kek_end = "\033[0m"

def ora_ertekeles():
    nap:str = input("Hét napja: ")
    tant:str = input("Óra neve: ")
    ertekeles:int = int(input("Értékelés (0-5): ")) 
    while (ertekeles > 5) or (ertekeles <= 0):
        if (ertekeles > 5):
            ertekeles:int = int(input("5 pont feletti értékelés nem elfogadható!"))
        elif (ertekeles < 0):
            ertekeles:int = int(input("Az értékelés nem lehet negatív!"))
    print(f"{kek}\nI/C:{kek_end}")
    print(f"Köszönjük az értékelést!\nÖsszefoglaló: {nap}, {tant}, {ertekeles}")