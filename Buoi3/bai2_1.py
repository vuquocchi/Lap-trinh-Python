# Duyet list bang for

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))