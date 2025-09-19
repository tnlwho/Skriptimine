filename = '19_09_25/four_csv_files/Create-MyCSV-v.csv'
column = 0 #Veergu mida kokku liita
total = 0 #Veeru summa

with open(filename, 'r') as f:
    contents = f.readlines() #Loeb faili sisu muutujasse
    for line in contents: # Rea kaupa läbikäimine
        line = line.strip() # Eemalda tühikud ja reavahetus 
        parts = line.split(';') # Tükelda semikoolonist 
        if parts[column].isdigit(): # Kui veerus on numbrid
            total += int(parts[column])
    print(total) #Test



