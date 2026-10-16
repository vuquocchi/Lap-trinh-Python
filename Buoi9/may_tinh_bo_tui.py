
import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

bieu_thuc = tk.StringVar()

o_hien_thi = tk.Entry(
    cua_so,
    textvariable=bieu_thuc,
    font=("Arial", 18),
    justify="right",
    state="readonly"
)
o_hien_thi.grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=15, sticky="ew"
)


def them_ky_tu(ky_tu):
    bieu_thuc.set(bieu_thuc.get() + ky_tu)


def xoa_tat_ca():
    bieu_thuc.set("")


def tinh_ket_qua():
    phep_tinh = bieu_thuc.get()

    if phep_tinh == "":
        messagebox.showerror(
            "Loi", "Vui long nhap phep tinh."
        )
        return

    ky_tu_hop_le = "0123456789+-*/.() "

    for ky_tu in phep_tinh:
        if ky_tu not in ky_tu_hop_le:
            messagebox.showerror(
                "Loi", "Bieu thuc khong hop le."
            )
            return

    try:
        ket_qua = eval(
            phep_tinh,
            {"__builtins__": None},
            {}
        )
        bieu_thuc.set(str(ket_qua))

    except (SyntaxError, TypeError, ZeroDivisionError,
            OverflowError):
        messagebox.showerror(
            "Loi", "Phep tinh khong hop le."
        )


cac_nut = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for ten_nut, hang, cot in cac_nut:
    if ten_nut == "=":
        lenh = tinh_ket_qua
    else:
        lenh = lambda x=ten_nut: them_ky_tu(x)

    tk.Button(
        cua_so,
        text=ten_nut,
        font=("Arial", 14),
        width=5,
        height=2,
        command=lenh
    ).grid(
        row=hang,
        column=cot,
        padx=3,
        pady=3
    )

tk.Button(
    cua_so,
    text="C - Xoa tat ca",
    font=("Arial", 12),
    command=xoa_tat_ca
).grid(
    row=5,
    column=0,
    columnspan=4,
    padx=5,
    pady=10,
    sticky="ew"
)

cua_so.mainloop()
