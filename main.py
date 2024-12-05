import ertekel
import sorozat
import hatoslotto
kek = "\033[34m"
sarga = "\033[33m"
szin_end = "\033[0m"
char = "*" * 24

print(f"{kek}\nI/A, B:{szin_end}")
ertekel.ora_ertekeles()

print(f"\n{sarga}{char}{szin_end}")

print(f"{kek}\nII/A, B, C:{szin_end}")
szamok = sorozat.sorozat()

print(f"{sarga}{char}{szin_end}")

print(f"{kek}\nII/D, E:{szin_end}")
db = sorozat.tizzel_oszthatoak_szama(szamok)
sorozat.konzol_ir(db)
sorozat.fajlba_ir(szamok)

print(f"{sarga}{char}{szin_end}")

print(f"{kek}\nIII/A, B:{szin_end}")
lotto = hatoslotto.beolvas("huzasok.txt", [])
hatoslotto.huzasok(lotto)

print(f"{sarga}{char}{szin_end}")

print(f"{kek}\nIII/C:{szin_end}\nA 43. héten húzott számok átlaga: {hatoslotto.atlag(lotto):.2f}")

print(f"{sarga}{char}{szin_end}")

print(f"{kek}\nIII/D:{szin_end}")
hatoslotto.legn_huzas(lotto)