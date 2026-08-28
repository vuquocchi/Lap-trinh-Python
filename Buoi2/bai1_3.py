# so sanh 3 cach dinh dang chuoi()

ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(
    ho_ten, nam_sinh, diem_tb
))

print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" %
      (ho_ten, nam_sinh, diem_tb))