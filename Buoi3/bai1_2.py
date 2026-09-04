# Cac phuong thuc thuong dung

ten_sv = ["An", "Binh", "Chi"]

ten_sv.append("Dung")       # them vao cuoi
ten_sv.insert(1, "Em")      # chen vao vi tri 1
print(ten_sv)

ten_sv.remove("Chi")        # xoa theo gia tri

pop_ra = ten_sv.pop()       # xoa va lay ra phan tu cuoi
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.sort()               # sap xep tang dan
print(ten_sv)

ten_sv.reverse()            # dao nguoc thu tu hien tai
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"])  # noi them mot list khac
print(ten_sv)