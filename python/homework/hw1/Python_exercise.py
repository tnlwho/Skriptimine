"""
1. Genereerib 20 juhuslikku täisarvu vahemikus 1-100. 
2. Salvestab need koos tänase kuupäevaga faili andmed.txt. 
3. Loeb failist need arvud uuesti sisse. 
4. Kasutab funktsiooni (enda loodud funktsiooni), mis arvutab: summa, keskmise ja suurima arvu. 
5. Kuvab tulemused ekraanile (funktsiooni tulemused + failist loetud arvud). 

"""

import random                      # moodul arvude genereerimiseks
from datetime import datetime      # moodul kuupäeva ja kellaaja jaoks


kuupaev = datetime.now().strftime(" %d.%m.%Y %H:%M:%S") # vormindatud kuupäev/kellaeg muutujasse
fail = 'andmed.txt'                                     # fail kuhu info salvestatakse andmed


# 1. Genereerib 20 juhuslikku täisarvu vahemikus 1-100.
arvud = []                                # tühi list juhuslike täisarvude jaoks

for i in range(20):
    random_arv = random.randint(1, 100)   # genereerib täisarvu
    arvud.append(random_arv)              # lisab listi kasutades append meetodit


f = open(fail, "w", encoding="utf-8") # avab faili kirjutamiseks
f.write(f"Kuupäev: {kuupaev}\n")      # kirjutab kuupäeva faili
f.write("Arvud: ")                    # kirjutab alguse arvude reale

for arv in arvud:
    f.write(str(arv) + " ")   # iga arvu järel tühik
f.write("\n")                 # rea lõppu reavahetus
f.close()                     # sulgeb faili

# Loetakse failist andmed uuesti sisse
f = open(fail, "r", encoding="utf-8") # avab faili lugemiseks
read_lines = f.readlines()            # loeme kõik read list
f.close()                             # sulgeb faili

arvud_failist = [] # tühi list, failist loetud arvude jaoks

for line in read_lines:
    if "Arvud:" in line:                  # kontrollib, et see on arvude rida
        line = line.replace("Arvud:", "") # eemaldab "Arvud:" teksti
        for a in line.split():            # jagame stringi tühikute järgi
            arvud_failist.append(int(a))  # string täisarvuks ja lisame listi

print(f"Failist loetud arvud:", arvud_failist) # Kuvab failist loetud arvud

# Funktsioon arvutuste jaoks
def arvutamine(arvud):
    """
    Funktsioon arvutab arvude summa, keskmise ja leiab suurima arvu.

    args:
        arvud (list): täisarvude list.

    returns:
        summa, keskmine ja suurim arv (kolm eraldi väärtust)
    """

    # Summa arvutamine
    summa = 0
    for arv in arvud:
        summa = summa + arv

    # Keskmise arvutamine
    keskmine = summa / len(arvud)

    # Suurima arvu leidmine
    suurim = arvud[0] 
    for arv in arvud:
        if arv > suurim:
            suurim = arv

    return summa, keskmine, suurim

summa, keskmine, suurim = arvutamine(arvud_failist)


# Kuvab tulemused ekraanile
print("Summa:", summa)
print("Keskmine:", keskmine)
print("Suurim arv:", suurim)