# Khai bao & truy xuat

sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print(sinh_vien["ho_ten"])
print(sinh_vien.get("diem_tb"))
print(sinh_vien.get("lop", "Chua co"))