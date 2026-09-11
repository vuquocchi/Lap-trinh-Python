# Them/sua/xoa

sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

sinh_vien["lop"] = "CNTT01"

sinh_vien["diem_tb"] = 9.0

print(sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})

print(sinh_vien)