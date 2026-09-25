# Bài tập 1.2

# Hàm không trả về giá trị
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return


# Hàm trả về nhiều giá trị
def chia_lay_thuong_du(a, b):
    return a // b, a % b


# Gọi hàm in lời chào
in_loi_chao("An")
in_loi_chao("Binh")
in_loi_chao("Chi")


# Gọi hàm chia lấy thương và dư
thuong, du = chia_lay_thuong_du(17, 5)

print(f"Thuong: {thuong}, du: {du}")


# Thử thêm 2 bộ dữ liệu
thuong, du = chia_lay_thuong_du(20, 3)
print(f"Thuong: {thuong}, du: {du}")

thuong, du = chia_lay_thuong_du(25, 4)
print(f"Thuong: {thuong}, du: {du}")