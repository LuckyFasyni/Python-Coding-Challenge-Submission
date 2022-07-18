#convert fuel consumption
#in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
#In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.
#1 American mile = 1609.344 metres;
#1 American gallon = 3.785411784 litres.

def l100kmtompg(liters):
    g = liters/3.785411784
    m = 100/1.609344
    x = m/g
    return x

def mpgtol100km(miles):
    k = miles*1.609344
    l = 3.785411784
    y = 100*l/k
    return y

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))