import csv

filename = 'persons.csv'

phrase = input('Sisesta otsitav fraas (min. 2 märki): ')

if len(phrase) > 1:
    with open(filename, 'r', encoding='utf-8') as f:
        content = csv.reader(f, delimiter=';')
        print(content) 
        for row in content:
            
            phrase = phrase.lower() # Tee väiketähtedeks
            first = row[0].lower() # Eesnimi väiketähtedeks
            last = row[1].lower() # Perenimi väiketähetedeks
            if phrase in first or phrase in last: 
                print(';'.join(row)) # List stringiks
                total += 1

        print(f, 'Leiti {total} nime.')
else:
    print('Otsitav fraas on liiga lühike') 


"""
Täiendus: Näita mitu nime leiti. Leiti xx nime

"""