class Huzas:
    def __init__(self,huzas:int,ev:int,het:int,szam:int):
        self.huzas=huzas
        self.ev=ev
        self.het=het
        self.szam=szam
    
    def __str__(self):
        return (f"Húzás: {self.huzas}\n"
                f"Év: {self.ev}\n"
                f"Hét: {self.het}\n"
                f"Szám: {self.szam}\n"
                f"\n")