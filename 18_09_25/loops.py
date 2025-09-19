import random 

names = ['Mati', 'Kati', 'Roosa', 'Manna']

# Väljasta listis olevad nimed nime kaupa eraldi real.
for name in names:
    print(name)
print()

print('Uus rida')
#for x range(len(names)):
 #   print(names[x], random.randint(1, 45))
#print()

#Lihtsalt numbrid
for x in range(1, 5):
    print(x, end=' | ')

print('\n') #kaks reavahet


for x in range(0, 10, 2): # Nullist kümneni (üheksa), kasvab paaris arv
    print(x, end=' | ')

print('\n')


# While loop
x = 0
while x < len(names):
    print(names[x])
    x += 1 # x = x + 1
print(x)


print('\n')

print('Ülesanne: ')
names = ['Mati', 'Kati', 'Roosa', 'Manna']
ages = []
for nr, name in enumerate(names, start=1):
    ages.append(random.randint(18, 36))
    print(f'{nr}. {name}, {ages[nr-1]}')
print() 
