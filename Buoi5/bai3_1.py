# Vòng lặp for – range() & duyệt List/Tuple/Dict/String

# for voi range()
for i in range(1, 6):
    print(i)

# for duyet List
diem_so = [8.5, 7.0, 9.2, 6.5]

for diem in diem_so:
    print("Diem:", diem)

# for duyet Tuple
toa_do = (3, 5)

for gia_tri in toa_do:
    print(gia_tri)

# for duyet Dictionary
diem_mon = {
    "Toan": 8.0,
    "Ly": 7.5
}

for mon, diem in diem_mon.items():
    print(mon, "-", diem)

# for duyet String
ten = "Python"

for ky_tu in ten:
    print(ky_tu)