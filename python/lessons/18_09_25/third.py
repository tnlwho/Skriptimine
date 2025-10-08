place = input('Sisesta elukoht: ')
print(f'Sisestati: {place}')
if len(place) > 1 and len(place) <= 7:
    print(f'lühikese nimega koht {place.title()}')
elif len(place) > 7:
    print(f'pika nimega koht {place.title()}')
else:
    print('nimi liiga lühike')