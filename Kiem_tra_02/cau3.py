import csv
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt



danh_sach = []

with open("sach.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for dong in reader:
        sach = {
            "ma": dong["MaSach"],
            "ten": dong["TenSach"],
            "gia": float(dong["Gia"]),
            "soluong": int(dong["SoLuong"])
        }

        danh_sach.append(sach)



tong_so_sach = len(danh_sach)

gia_trung_binh = sum(
    sach["gia"] for sach in danh_sach
) / tong_so_sach

sach_gia_cao_nhat = max(
    danh_sach,
    key=lambda sach: sach["gia"]
)

print("========== THỐNG KÊ SÁCH THƯ VIỆN ==========")

print("Tổng số đầu sách:", tong_so_sach)

print("Giá trung bình:", gia_trung_binh, "VNĐ")

print(
    "Sách có giá cao nhất:",
    sach_gia_cao_nhat["ten"]
)



plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False

ma_sach = [sach["ma"] for sach in danh_sach]

so_luong = [sach["soluong"] for sach in danh_sach]


plt.figure(figsize=(11, 6))

plt.bar(ma_sach, so_luong)

plt.title(
    "BIỂU ĐỒ SỐ LƯỢNG SÁCH TỒN KHO",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Mã sách", fontsize=12)
plt.ylabel("Số lượng tồn kho (cuốn)", fontsize=12)

for i, value in enumerate(so_luong):
    plt.text(
        i,
        value + 1,
        str(value),
        ha="center",
        fontsize=11
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig("bieudo.png", dpi=300)

plt.close()

print("Đã lưu biểu đồ thành công: bieudo.png")



sach_sap_het = []

for sach in danh_sach:
    if sach["soluong"] < 10:
        sach_sap_het.append(sach)


with open(
    "canh_bao_sach.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Mã sách",
        "Tên sách",
        "Giá",
        "Số lượng"
    ])

    for sach in sach_sap_het:
        writer.writerow([
            sach["ma"],
            sach["ten"],
            sach["gia"],
            sach["soluong"]
        ])

print("\n========== DANH SÁCH SÁCH SẮP HẾT ==========")

for sach in sach_sap_het:
    print(
        sach["ma"], "-",
        sach["ten"],
        "- Số lượng:", sach["soluong"]
    )

print("\nĐã xuất file cảnh báo: canh_bao_sach.csv")