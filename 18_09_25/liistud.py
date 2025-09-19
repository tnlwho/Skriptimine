places = [] # Tühi list

places.append('Kehtna')
places.append('Rapla')
places[1:1] = ['Tallinn', 'Pärnu'] # Lisa Kehtna ja Rapla vahele
places.extend(['Viljandi', 'Tartu', 'Rapla']) # Lisab lõppu
places.insert(2, 'Are') # Lisab Tallinna ja Pärnu vahele


print(places)

#Kustutamine 
places.remove('Rapla') # Esimene leitud
places.pop(6) # Viimase kustutamine 
del places[2]
print(places)

# Lisa Rapla lõppu ja peale Pärnut
places.extend(['Rapla'])
places.insert(5, 'Pärnu')
print(places)

place = places[-1] # muutuja saab väärtuseks listi viimase elemendi

index = places.index(place) # Mitmes element on Rapla (ainult üks)
count = places.count(place) # Mitu Raplat on listis
print(index, count) # Väljund 3 2

if place in places: 
    print(f'{place} on nimekirjas.')

# Koopia nimekirjas
list_copy = places.copy()
list_list = list(places)

print(places)
print(list_copy)
print(list_list)

list_copy.sort() # A-Z
list_list.sort(reverse=True) # Z-A

print() 
print(list_copy)
print(list_list)

new_sorted_list = sorted(places, reverse=False) # A-Z
print(new_sorted_list)

# Tühjenda listi sisu
new_sorted_list.clear()

# Väljasta listi places viimane element ilma [-1] kasutamata
# print(places[len(places)-1])

# Väljasta konsooli elemendi Pärnu kesmine täht trükitähena
print(places[-2][2].upper())