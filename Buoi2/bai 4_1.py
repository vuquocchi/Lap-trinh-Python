# Indexing & Slicing

cau = "Lap trinh Python rat thu vi"

print(cau[0])       # ky tu dau tien
print(cau[-1])      # ky tu cuoi cung
print(cau[4:10])    # tu vi tri 4 den truoc vi tri 10
print(cau[:8])      # tu dau den truoc vi tri 8
print(cau[11:])     # tu vi tri 11 den het
print(cau[::-1])    # dao nguoc chuoi

print(cau == cau[::-1])  # kiem tra palindrome