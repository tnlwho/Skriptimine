age = input('Sisesta vanus: ')
age = int(age)
if age < 1 or age > 122:
    print('vanus vales vahemikus (lubatud on 1-122)')
elif age < 18:
    print('alaealine')
elif age < 65:
    print('tööealine')
elif age < 100:
    print('pensionär')
else:
    print('pikaealine')