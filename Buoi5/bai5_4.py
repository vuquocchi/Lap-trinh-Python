# continue: loc phan tu hop le trong danh sach

danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []

for so in danh_sach:
    if so <= 0:
        continue

    danh_sach_hop_le.append(so)

print("Cac so hop le (duong):", danh_sach_hop_le)