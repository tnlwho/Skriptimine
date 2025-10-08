filename = 'persons.csv'

total = 0

phrase = input('Sisesta otsitav fraas (min. 2 märki): ')

if len(phrase.strip()) > 1:
    phrase = phrase.strip().lower()
    f = open(filename, 'r', encoding='utf-8')
    content = f.readlines()[1:] # Alates teisest reast
    f.close() #Close file
    for line in content: # Otsi rea kaupa
        line = line.strip() # Korrasta rida, eemalda reavahetus reast \n
        if phrase in line.lower():
            print(line)
            total = 1 #Suurenda loendurit
    print(f'{total} nime.')

else:
    print('Otsing on lühike')