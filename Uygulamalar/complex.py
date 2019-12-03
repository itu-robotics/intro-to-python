import math

a = input("Reel part: ")
b = input("Imajiner part: ")

a = int(a)
b = int(b)
komp = 1j
z = a + b * komp

print("Komplex Form: ", z)

r = math.sqrt(a**2 + b**2) # abs()
tetha = math.atan(b/a)

print(r, math.cos(tetha) , komp*math.sin(tetha))
