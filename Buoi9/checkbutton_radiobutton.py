
import tkinter as tk

# Tao cua so
cua_so = tk.Tk()
cua_so.title("Checkbutton va Radiobutton")
cua_so.geometry("350x400")

# Hoat dong 1: Checkbutton
tk.Label(
    cua_so,
    text="Chon so thich cua ban:",
    font=("Arial", 12)
).pack(pady=10)

bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()

tk.Checkbutton(
    cua_so, text="Doc sach", variable=bien_doc_sach
).pack(anchor="w", padx=30)

tk.Checkbutton(
    cua_so, text="The thao", variable=bien_the_thao
).pack(anchor="w", padx=30)

tk.Checkbutton(
    cua_so, text="Am nhac", variable=bien_am_nhac
).pack(anchor="w", padx=30)


def xem_lua_chon():
    print("Doc sach:", bien_doc_sach.get())
    print("The thao:", bien_the_thao.get())
    print("Am nhac:", bien_am_nhac.get())


tk.Button(
    cua_so,
    text="Xem lua chon",
    command=xem_lua_chon
).pack(pady=10)

# Hoat dong 2: Radiobutton
tk.Label(
    cua_so,
    text="Chon loai tai khoan:",
    font=("Arial", 12)
).pack(pady=10)

bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

tk.Radiobutton(
    cua_so,
    text="Ca nhan",
    variable=bien_loai_tai_khoan,
    value="ca_nhan"
).pack(anchor="w", padx=30)

tk.Radiobutton(
    cua_so,
    text="Doanh nghiep",
    variable=bien_loai_tai_khoan,
    value="doanh_nghiep"
).pack(anchor="w", padx=30)


def xem_loai_tai_khoan():
    nhan_ket_qua.config(
        text="Ban da chon: " + bien_loai_tai_khoan.get()
    )


tk.Button(
    cua_so,
    text="Xac nhan",
    command=xem_loai_tai_khoan
).pack(pady=5)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()
