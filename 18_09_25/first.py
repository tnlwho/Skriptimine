# import
from datetime import datetime


name = 'taNel hÕimra' # String ehk Sõne
age = 38 # Täisarv (integer)
height = 1.86 # Ujuvkoma (float)

print(name, age, height) # Väljastab kolm väärtust

print(f'Kasutaja {name.title()} vanuses {age} ja pikkus {height} meetrit istub laua taga.')

print('kasutaja ' + name + ' vanuses ' + str(age) + ' ja pikkusega ' + str(height) )

# Arvutamine
birth_year = datetime.now().year - age
print(birth_year) 

name = name.title() #Korrasta nimi ja kasuta sama muutujat
print(name[1]) # Väljund: a
print(name[1:4]) # Väljund: ane
print(name[6:]) # Väljund: Eesnimi
print(name[:5]) # Väljund: Perekonnanimi 


place = input('Sisesta elukoht: ')
print(f'Sisestati: {place}')
if len(place) > 1 and len(place) <= 7:
    print(f'lühikese nimega koht {place.title()}')
elif len(place) > 7:
    print(f'pika nimega koht {place.title()}')
else:
    print('nimi liiga lühike')

# Väljasta muutujate andmetüübid
print(type(name))
print(type(age))
print(type(height))
print(type(place))