diem = 6.5
tuoi = 20

# Điểm Khá: từ 6.5 đến dưới 8.0
dat_kha = diem >= 6.5 and diem < 8.0
print("Đạt loại Khá:", dat_kha)

# Chưa đủ 18 hoặc trên 60
ngoai_do_tuoi = tuoi < 18 or tuoi > 60
print("Chưa đủ 18 hoặc trên 60:", ngoai_do_tuoi)

# Phủ định điều kiện trên
print("Không thuộc trường hợp trên:", not ngoai_do_tuoi)