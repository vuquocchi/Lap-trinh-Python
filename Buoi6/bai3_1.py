# Bài tập 3.1 - *args

def tinh_tong(*args):
    tong = 0

    for so in args:
        tong += so

    return tong


print(tinh_tong(1, 2, 3))

print(tinh_tong(5, 10, 15, 20, 25))

print(tinh_tong())