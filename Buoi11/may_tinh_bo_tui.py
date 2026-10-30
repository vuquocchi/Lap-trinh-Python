def tinh_toan(a, phep_tinh, b):

    if phep_tinh == "+":
        return a + b

    elif phep_tinh == "-":
        return a - b

    elif phep_tinh == "*":
        return a * b

    elif phep_tinh == "/":

        if b == 0:
            return "Loi: khong the chia cho 0"

        return a / b

    else:
        return "Phep tinh khong hop le"


def main():

    print("===== MAY TINH BO TUI =====")

    while True:

        bieu_thuc = input(
            "Nhap bieu thuc (vd: 5 + 3), "
            "hoac 'thoat' de dung: "
        ).strip()

        if bieu_thuc.lower() == "thoat":
            print("Tam biet!")
            break

        try:

            a_str, phep_tinh, b_str = bieu_thuc.split()

            a = float(a_str)
            b = float(b_str)

            ket_qua = tinh_toan(a, phep_tinh, b)

            print("Ket qua:", ket_qua)

        except ValueError:

            print(
                "Dinh dang khong hop le. "
                "Vi du dung: 5 + 3"
            )


if __name__ == "__main__":
    main()