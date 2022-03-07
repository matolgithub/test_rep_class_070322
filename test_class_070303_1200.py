class Cats:
    """Test example CATS"""
    name = ''
    years_old = 5

Murka = Cats()
Stepka = Cats()

Murka.name = 'Murka'
Murka.years_old = 3

Stepka.name = 'Stepka'
Stepka.years_old = 5


print(Cats.name)
print(Cats.years_old)
print(Cats.__dict__)
print(Cats.__dir__)
print(Cats.__doc__)
print(Murka.__dict__)