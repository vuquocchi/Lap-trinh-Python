# Bài tập 5.3

danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2}
]


# Sắp xếp điểm tăng dần
sap_xep_theo_diem = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"]
)


# Sắp xếp điểm giảm dần
sap_xep_giam_dan = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"],
    reverse=True
)


print("--- Tang dan ---")

for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])


print("--- Giam dan ---")

for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])