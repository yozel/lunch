from lunch import place
from lunch.vehicles import Car, Motocycle
from lunch.people import Person, PersonPool


pool = PersonPool([
    Person('burak.donmez', vehicle=Motocycle()),
    Person('yasin.ozel', vehicle=Motocycle(allow_twoup=False)),

    Person('baran.demirci', vehicle=Motocycle()),
    Person('fatma.tosun'),

    Person('hande.sert'),
    Person('tarkan.dikmen'),

    Person('hakan.ozay', vehicle=Motocycle()),
    Person('can.cilingir', vehicle=Car()),

    Person('emre.yilmaz', vehicle=Car()),
    Person('halil.kaya'),
    Person('altay.inci'),
])

result = place(pool)

for i in result:
    print(i)
