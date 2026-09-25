# Hoạt động 2

def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")


# 1. Dùng toàn bộ giá trị mặc định
gioi_thieu("An")


# 2. Ghi đè giá trị tuổi
gioi_thieu("Binh", 20)


# 3. Dùng tham số từ khóa, bỏ qua tuổi
gioi_thieu("Chi", lop="CNTT01")


# 4. Dùng toàn bộ tham số từ khóa
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)