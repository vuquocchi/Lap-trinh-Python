# 2.1
import pandas as pd
import os

duong_dan = os.path.join(
    os.path.dirname(__file__),
    "diem_sinh_vien.csv"
)

df = pd.read_csv(duong_dan)

print("5 dong dau tien:")
print(df.head())

print("Kich thuoc:", df.shape)

print("Ten cac cot:", df.columns.tolist())

# 2.2
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

print("Diem trung binh theo mon:")
print(diem_trung_binh_mon)

print("Diem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())

# 2.3
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)

print("Diem trung binh tung sinh vien:")
print(diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]

sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)

print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)