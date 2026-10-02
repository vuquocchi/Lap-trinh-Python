danh_sach_sach = [
    {
        "ma_sach": "S001",
        "ten_sach": "Lap trinh Python",
        "tac_gia": "Nguyen Van A",
        "gia": 100000,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    },
    {
        "ma_sach": "S002",
        "ten_sach": "Lap trinh C++",
        "tac_gia": "Tran Van B",
        "gia": 120000,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    },
    {
        "ma_sach": "S003",
        "ten_sach": "Co so du lieu",
        "tac_gia": "Le Van C",
        "gia": 150000,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    },
    {
        "ma_sach": "S004",
        "ten_sach": "Lap trinh Java",
        "tac_gia": "Pham Van D",
        "gia": 130000,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    }
]

lich_su_muon = []


def hien_thi_danh_sach_sach():

    print("\n" + "=" * 90)

    print(
        f"{'Ma sach':<10}"
        f"{'Ten sach':<25}"
        f"{'Tac gia':<20}"
        f"{'Gia':<15}"
        f"{'Trang thai':<15}"
        f"{'Nguoi muon':<15}"
    )

    print("-" * 90)

    for sach in danh_sach_sach:

        print(
            f"{sach['ma_sach']:<10}"
            f"{sach['ten_sach']:<25}"
            f"{sach['tac_gia']:<20}"
            f"{sach['gia']:>10,} VND "
            f"{sach['trang_thai']:<15}"
            f"{sach['nguoi_muon']:<15}"
        )

    print("=" * 90)


def tim_sach_theo_ma(ma_sach):

    for sach in danh_sach_sach:

        if sach["ma_sach"] == ma_sach:
            return sach

    return None


def xem_sach_co_san():

    sach_co_san = [
        sach
        for sach in danh_sach_sach
        if sach["trang_thai"] == "Co san"
    ]

    if len(sach_co_san) == 0:

        print("-> Hien khong con sach nao co san.")

        return

    print("\nCAC SACH DANG CO SAN:")

    for sach in sach_co_san:

        print(
            f" {sach['ma_sach']} - "
            f"{sach['ten_sach']} - "
            f"{sach['tac_gia']}"
        )


def them_sach(ma_sach, ten_sach, tac_gia, gia):

    if tim_sach_theo_ma(ma_sach) is not None:

        print(
            f"-> Ma sach {ma_sach} da ton tai, "
            f"khong the them."
        )

        return

    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "tac_gia": tac_gia,
        "gia": gia,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    })

    print(
        f"-> Da them sach {ma_sach} thanh cong."
    )


def muon_sach(ma_sach, nguoi_muon):

    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:

        print(
            f"-> Khong tim thay sach {ma_sach}."
        )

        return

    if sach["trang_thai"] == "Dang muon":

        print(
            f"-> Sach {ma_sach} dang duoc muon, "
            f"khong the muon."
        )

        return

    sach["trang_thai"] = "Dang muon"

    sach["nguoi_muon"] = nguoi_muon

    lich_su_muon.append({
        "ma_sach": ma_sach,
        "ten_sach": sach["ten_sach"],
        "nguoi_muon": nguoi_muon
    })

    print(
        f"-> Cho {nguoi_muon} muon sach "
        f"{ma_sach} thanh cong."
    )


def tra_sach(ma_sach):

    sach = tim_sach_theo_ma(ma_sach)

    if sach is None:

        print(
            f"-> Khong tim thay sach {ma_sach}."
        )

        return

    if sach["trang_thai"] == "Co san":

        print(
            f"-> Sach {ma_sach} dang co san, "
            f"khong co nguoi muon."
        )

        return

    print(
        f"-> {sach['nguoi_muon']} tra sach "
        f"{ma_sach} thanh cong."
    )

    sach["trang_thai"] = "Co san"

    sach["nguoi_muon"] = ""


def thong_ke_muon_sach():

    if len(lich_su_muon) == 0:

        print(
            "-> Chua co luot muon sach nao."
        )

        return

    print("\nLICH SU MUON SACH:")

    for gd in lich_su_muon:

        print(
            f" {gd['ma_sach']} - "
            f"{gd['ten_sach']} - "
            f"{gd['nguoi_muon']}"
        )

    print(
        f"\n>>> TONG SO LUOT MUON: "
        f"{len(lich_su_muon)}"
    )


def nhap_so_nguyen(loi_nhac):

    while True:

        try:

            return int(input(loi_nhac))

        except ValueError:

            print(
                "-> Du lieu khong hop le, "
                "vui long nhap lai mot so nguyen."
            )


def hien_thi_menu():

    print("\n===== QUAN LY THU VIEN =====")

    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem sach dang co san")
    print("3. Them sach moi")
    print("4. Muon sach")
    print("5. Tra sach")
    print("6. Thong ke luot muon")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():

    while True:

        hien_thi_menu()

        lua_chon = input(
            "Nhap lua chon cua ban: "
        ).strip()


        if lua_chon == "1":

            hien_thi_danh_sach_sach()


        elif lua_chon == "2":

            xem_sach_co_san()


        elif lua_chon == "3":

            ma_sach = input(
                "Nhap ma sach moi: "
            ).strip().upper()

            ten_sach = input(
                "Nhap ten sach: "
            ).strip().title()

            tac_gia = input(
                "Nhap ten tac gia: "
            ).strip().title()

            gia = nhap_so_nguyen(
                "Nhap gia sach: "
            )

            them_sach(
                ma_sach,
                ten_sach,
                tac_gia,
                gia
            )


        elif lua_chon == "4":

            ma_sach = input(
                "Nhap ma sach can muon: "
            ).strip().upper()

            nguoi_muon = input(
                "Nhap ten nguoi muon: "
            ).strip().title()

            muon_sach(
                ma_sach,
                nguoi_muon
            )


        elif lua_chon == "5":

            ma_sach = input(
                "Nhap ma sach can tra: "
            ).strip().upper()

            tra_sach(ma_sach)


        elif lua_chon == "6":

            thong_ke_muon_sach()


        elif lua_chon == "0":

            print(
                "Cam on da su dung chuong trinh. "
                "Tam biet!"
            )

            break


        else:

            print(
                "-> Lua chon khong hop le, "
                "vui long chon lai."
            )


if __name__ == "__main__":

    chay_chuong_trinh()