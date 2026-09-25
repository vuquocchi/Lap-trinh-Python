# Bài tập 1.1

# Hàm tìm ước số chung lớn nhất
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Hàm tìm bội số chung nhỏ nhất
def bscnn(a, b):
    return a * b // uscln(a, b)


# Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Hàm kiểm tra số hoàn thiện
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0

    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n

# Gọi hàm USCLN - 3 bộ dữ liệu
print("USCLN:")
print(uscln(24, 36))
print(uscln(15, 25))
print(uscln(18, 30))

# Gọi hàm BSCNN - 3 bộ dữ liệu
print("\nBSCNN:")
print(bscnn(4, 6))
print(bscnn(5, 10))
print(bscnn(12, 18))

# Kiểm tra số nguyên tố
print("\nKiểm tra số nguyên tố:")
print(kiem_tra_nguyen_to(29))
print(kiem_tra_nguyen_to(17))
print(kiem_tra_nguyen_to(20))

# Kiểm tra số hoàn thiện
print("\nKiểm tra số hoàn thiện:")
print(kiem_tra_so_hoan_thien(28))
print(kiem_tra_so_hoan_thien(6))
print(kiem_tra_so_hoan_thien(10))