"""
Luua etteantud kasutajatele kasutajanimi ja e-posti aadress
Kasutajanimi:
    eesnimi.perenimi
    eesnimes eemalda tühi ja/või sidekriips Mari Liis, Mari-Liis --> https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
    eemaldada rõhumärgid ja täpitähed (äöüõ jt)
    kasutajanimi on läbivalt väikeste tähtedega

E-post:
    kasutajanimi@asutus.com

Kellele:
    Sündinud 1990-1999 k.a

Uue faili sisu on:
    Eesnimi.Perenimi;Isikukood;Kasutajanimi;E-post
    Eesnimi;Perenimi;Sünniaeg;Sugu;Isikukood <--- Originaal

"""

import csv
import unicodedata

source = 'persons.csv' # Olemasolev fail

destination = 'accounts.csv' # Uus fail

header = 'Eesnimi.Perenimi;Isikukood;Kasutajanimi;Epost' # Uue faili päis

domain = '@asutus.com' 

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

# print(strip_accents('aöõüšž'))

with open(source, 'r', encoding='utf-8') as f:
   with open(destination, 'w', encoding='utf-8') as d:
      content = csv.reader(f, delimiter=';') 
      d.write(header + '\n')
      next(content)


      for row in content:
         date = row[2] # Kuupäev eraldi muutujasse
         # print(date)
         year = int(date.split('.')[2]) # V6ta aasta kuupäevast ja tee täisarv 
         #print(year)

         if year >= 1990 and year <= 1999:
            first_name = row[0]
            last_name = row[1]

            # Eemalda nimest sidekriipsud ja tühikud
            first_name = first_name.replace(' ','')
            first_name = first_name.replace('-','')

            # Kasutajanime loomine
            username = '.'.join([first_name, last_name]).lower()
            username = strip_accents(username) # Eemaldab täpitähed
            #username = username.replace(' ','')
            #username = username.replace('-','')

            # E-posti loomine
            email = username + domain
            #print(row[0], first_name, last_name, username, email)

            # Uus rida
            new_line = ';'.join(row[:2] + [row[-1], username, email])
            d.write(new_line + '\n')

            print(new_line)