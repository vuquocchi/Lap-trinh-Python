import tkinter as tk
from tkinter import messagebox

danh_sach = []


def hien_thi_sach(ds):
    listbox.delete(0, tk.END)

    for sach in ds:
        dong = (
            f'{sach["ma"]} - {sach["ten"]} - '
            f'{sach["gia"]:g}d - SL: {sach["soluong"]}'
        )
        listbox.insert(tk.END, dong)


def them_sach():
    ma = entry_ma.get().strip()
    ten = entry_ten.get().strip()
    gia = entry_gia.get().strip()
    soluong = entry_soluong.get().strip()

    if ma == "" or ten == "":
        messagebox.showerror(
            "Loi", "Ma sach va ten sach khong duoc de trong!"
        )
        return

    try:
        gia = float(gia)
        soluong = int(soluong)

        if gia < 0 or soluong < 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Loi", "Gia va so luong phai la so hop le, khong am!"
        )
        return

    sach = {
        "ma": ma,
        "ten": ten,
        "gia": gia,
        "soluong": soluong
    }

    danh_sach.append(sach)

    hien_thi_sach(danh_sach)

    messagebox.showinfo("Thong bao", "Them sach thanh cong!")

    entry_ma.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_gia.delete(0, tk.END)
    entry_soluong.delete(0, tk.END)


def tim_kiem():
    tu_khoa = entry_timkiem.get().strip().lower()

    ket_qua = []

    for sach in danh_sach:
        if tu_khoa in sach["ten"].lower():
            ket_qua.append(sach)

    # Xóa kết quả cũ và hiển thị kết quả mới
    listbox.delete(0, tk.END)

    if len(ket_qua) == 0:
        messagebox.showinfo("Thong bao", "Khong tim thay sach!")
    else:
        hien_thi_sach(ket_qua)


cua_so = tk.Tk()
cua_so.title("QUAN LY SACH THU VIEN")
cua_so.geometry("650x550")

tk.Label(
    cua_so,
    text="QUAN LY SACH THU VIEN",
    font=("Arial", 18, "bold")
).pack(pady=15)

frame = tk.Frame(cua_so)
frame.pack(pady=10)

tk.Label(frame, text="Ma sach:").grid(row=0, column=0, padx=10, pady=5)
entry_ma = tk.Entry(frame, width=35)
entry_ma.grid(row=0, column=1)

tk.Label(frame, text="Ten sach:").grid(row=1, column=0, padx=10, pady=5)
entry_ten = tk.Entry(frame, width=35)
entry_ten.grid(row=1, column=1)

tk.Label(frame, text="Gia:").grid(row=2, column=0, padx=10, pady=5)
entry_gia = tk.Entry(frame, width=35)
entry_gia.grid(row=2, column=1)

tk.Label(frame, text="So luong:").grid(row=3, column=0, padx=10, pady=5)
entry_soluong = tk.Entry(frame, width=35)
entry_soluong.grid(row=3, column=1)

tk.Button(
    cua_so,
    text="Them sach",
    command=them_sach,
    bg="lightgreen",
    width=20
).pack(pady=10)

frame_tim = tk.Frame(cua_so)
frame_tim.pack(pady=10)

tk.Label(frame_tim, text="Tim kiem:").pack(side=tk.LEFT)

entry_timkiem = tk.Entry(frame_tim, width=30)
entry_timkiem.pack(side=tk.LEFT, padx=5)

tk.Button(
    frame_tim,
    text="Tim kiem",
    command=tim_kiem
).pack(side=tk.LEFT)

tk.Label(
    cua_so,
    text="DANH SACH SACH",
    font=("Arial", 12, "bold")
).pack(pady=5)

listbox = tk.Listbox(cua_so, width=75, height=12)
listbox.pack(pady=10)

cua_so.mainloop()