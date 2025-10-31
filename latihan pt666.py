number = []
angka = int(input("Masukan berapa saja angkanya : "))

for i in range(angka):
    item = int(input("Masukan angkanya : "))
    number.append(item)
    
jum = 0

for a in number:
    jum = jum + a
    
print(number)
print(jum)