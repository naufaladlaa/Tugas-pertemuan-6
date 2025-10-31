nama = []
nim = []
uts = []
uas = []
total = []

data = int(input("Berapa Data : "))

for i in range(data):
    print("Data ke - " +str(i+1))
    nama.append(input("Masukan Nama Anda : "))
    nim.append(input("Masukan NIM anda : "))
    uts.append(int(input("Masukan nilai UTS anda : ")))
    uas.append(int(input("Masukan nilai UAS anda : ")))
    print("=====================================================")
    
for i in range(data):
    total.append((uts[i] + uas[i])/2)
    

print(f"{'NAMA':<15}{'NIM':<12}{'UTS':<10}{'UAS':<10}{'TOTAL':<10}")
print("=====================================================")
for i in range(data):
    inte = int(total[i])
    print(f"{nama[i]:<15}{nim[i]:<12}{uts[i]:<10}{uas[i]:<10}{inte:<10}")
print("=====================================================")