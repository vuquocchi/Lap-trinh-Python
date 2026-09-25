# Hoạt động 4

# Biến global
so_luot_truy_cap = 0


# Hàm tăng biến global
def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1


# Hàm có biến local
def vi_du_bien_local():
    so_luot_truy_cap = 100
    print("Ben trong ham, bien local =", so_luot_truy_cap)


# Gọi hàm tăng lượt truy cập 2 lần
tang_luot_truy_cap()
tang_luot_truy_cap()

print("So luot truy cap (global):", so_luot_truy_cap)


# Gọi hàm có biến local
vi_du_bien_local()

print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)