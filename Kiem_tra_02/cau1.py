danh_sach = []

# a.
def them_sach(danh_sach, ma, ten, gia, soluong):
    sach = {
        "ma": ma,
        "ten": ten,
        "gia": gia,
        "soluong": soluong
    }

    danh_sach.append(sach)
    print("Them sach thanh cong!")


# b.
def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua = []

    for sach in danh_sach:
        if tu_khoa.lower() in sach["ten"].lower():
            ket_qua.append(sach)

    return ket_qua


# c.
def tong_gia_tri_kho_sach(danh_sach):
    tong = 0

    for sach in danh_sach:
        tong += sach["gia"] * sach["soluong"]

    return tong


# d.
them_sach(danh_sach, "S001", "Lap trinh Python co ban", 95000, 40)
them_sach(danh_sach, "S002", "Cau truc du lieu va giai thuat", 120000, 6)
them_sach(danh_sach, "S003", "Nhap mon tri tue nhan tao", 150000, 25)


while True:
    print("\n===== QUAN LY SACH THU VIEN =====")
    print("1. Them sach")
    print("2. Tim kiem theo ten")
    print("3. Xem tong gia tri kho sach")
    print("4. Thoat")

    chon = input("Nhap lua chon: ")

    if chon == "1":
        ma = input("Nhap ma sach: ")
        ten = input("Nhap ten sach: ")

        try:
            gia = float(input("Nhap gia sach: "))
            soluong = int(input("Nhap so luong: "))

            if not ma.strip() or not ten.strip():
                print("Ma sach va ten sach khong duoc de trong!")
            elif gia < 0 or soluong < 0:
                print("Gia va so luong khong duoc am!")
            else:
                them_sach(danh_sach, ma, ten, gia, soluong)

        except ValueError:
            print("Gia va so luong phai la so hop le!")

    elif chon == "2":
        tu_khoa = input("Nhap ten sach can tim: ")
        ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)

        if len(ket_qua) == 0:
            print("Khong tim thay sach!")

        else:
            print("\n===== KET QUA TIM KIEM =====")
            for sach in ket_qua:
                print(
                    sach["ma"], "-",
                    sach["ten"], "-",
                    sach["gia"], "d - SL:",
                    sach["soluong"]
                )

    elif chon == "3":
        tong = tong_gia_tri_kho_sach(danh_sach)
        print("Tong gia tri kho sach:", tong, "VND")

    elif chon == "4":
        print("Thoat chuong trinh!")
        break

    else:
        print("Lua chon khong hop le!")