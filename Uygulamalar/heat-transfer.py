msg = input("1. Madde: ") # 10,1,75

kutle = msg.split(",")[0]
ozisi = msg.split(",")[1]
sicaklik = msg.split(",")[2]

m1 = int(kutle)
c1 = int(ozisi)
t1 = int(sicaklik)

msg = input("2. Madde: ")

kutle = msg.split(",")[0]
ozisi = msg.split(",")[1]
sicaklik = msg.split(",")[2]


m2 = int(kutle)
c2 = int(ozisi)
t2 = int(sicaklik)

td = ((m1*c1*t1)+(m2*c2*t2)) / (m1*c1 + m2*c2)

print("Denge Sicakligi:", td)
