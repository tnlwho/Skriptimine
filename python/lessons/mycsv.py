filename = 'Create-MyCSV-v.csv'
column = 0 #Veergu mida kokku liita
total = 0 #Veeru summa

with open(filename, 'r') as f:
    content = f.readlines() #Loeb faili sisu muutujasse
    print(content)