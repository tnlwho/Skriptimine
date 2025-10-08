# Lihtne funktsioon
def welcome():
    """"Väljastab staatilise tervitusteksti"""
    print('Tere, kuidas läheb?')

welcome()


# 2 Dünaamiline funktsioon
def welcome_name(name):
    """Tagastab tervitussõnumi koos nimega."""
    return f'Tere, {name}'
print()
welcome()
print(welcome_name('Jack Sparrow')) # prindib funktsioonist

roosa_manna = welcome_name('Roosa Manna') # teeb muutujaks ja väljastab muutuja
print(roosa_manna)

# Jagamine
def division(number1,number2):
    """
    Teostab kahe arvu jagamist.

    Args:
        Number1 (float): Jagatav arv
        Number2 (float): Jagaja (ei tohi olla null)

    Returns:
        float: Jagatise väärtus
    """
    if number2 != 0:
        return number1 / number2
    return -1

a = 10
b = 2

print(division(a,b))
print(division(b,-1))

print()
# funktsioon tutvustus
def introduce(name, age=65):
    """
    Loob lihtsa tutvustava lause.

    :param name: Isiku nimi
    :type name: str
    :param age: Isiku vanus (vaikimisi 65)
    :type age: int
    :return: Tekstiline tutvustus vormis
            'Tema on <nimi> ja ta on <vanus> aastane!'
    :rtype: str
    """
    return f'Tema on {name} ja ta on {age} aastane!'

print(introduce('Jaak Varblane'))
print(introduce('Korsi Mihkel','35'))
print(introduce(1234,4321))


#Ülesanne
print()
"""
ÜLESANNE: Loo list viie nimega. Väljasta viie nime tervitus.

"""
names = ['Mati Karu', 'Kati Karu', 'Jaak Varblane', 'Mihkel Kors', 'Kadi Kask']

def welcome_name(name):
    return f'Tere, {name} kuidas läheb?'

for name in names:
    print(welcome_name(name))