import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_MUC_CHI = ["Ăn uống", "Di chuyển", "Mua sắm", "Hóa đơn", "Giải trí", "Sức khỏe", "Học tập", "Khác"]
DANH_MUC_THU = ["Lương", "Thưởng", "Trợ cấp", "Đầu tư", "Thu nhập khác"]


class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý chi tiêu cá nhân")
        self.geometry("780x650")
        self.minsize(720, 590)
        self.resizable(True, True)
        db.tao_bang_neu_chua_co()
        self._tao_style()
        self._tao_giao_dien()
        self.tai_lai_danh_sach()

    def _tao_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", rowheight=27, font=("Segoe UI", 9), background="white", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"), background="#E8EEF8")
        style.configure("TCombobox", padding=4)
        style.configure("TEntry", padding=4)

    def _tao_giao_dien(self):
        tk.Label(self, text="QUẢN LÝ CHI TIÊU CÁ NHÂN", font=("Segoe UI", 16, "bold"),
                 fg="#173B67").pack(pady=(12, 8))

        khung_nhap = tk.LabelFrame(self, text=" Thêm / cập nhật giao dịch ", padx=12, pady=8,
                                   font=("Segoe UI", 9, "bold"))
        khung_nhap.pack(fill="x", padx=14, pady=5)

        self.var_ngay = tk.StringVar(value=date.today().strftime("%Y-%m-%d"))
        self.var_loai = tk.StringVar(value="Chi")
        self.var_dm = tk.StringVar(value=DANH_MUC_CHI[0])
        self.var_tien = tk.StringVar()
        self.var_ghichu = tk.StringVar()

        tk.Label(khung_nhap, text="Ngày (YYYY-MM-DD):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(khung_nhap, textvariable=self.var_ngay, width=19).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        tk.Label(khung_nhap, text="Loại giao dịch:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.combo_loai = ttk.Combobox(khung_nhap, textvariable=self.var_loai, values=["Thu", "Chi"],
                                       state="readonly", width=16)
        self.combo_loai.grid(row=0, column=3, sticky="w", padx=5, pady=5)
        self.combo_loai.bind("<<ComboboxSelected>>", self._doi_loai)

        tk.Label(khung_nhap, text="Danh mục:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.combo_dm = ttk.Combobox(khung_nhap, textvariable=self.var_dm, values=DANH_MUC_CHI,
                                     state="readonly", width=17)
        self.combo_dm.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        tk.Label(khung_nhap, text="Số tiền (VNĐ):").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        ttk.Entry(khung_nhap, textvariable=self.var_tien, width=19).grid(row=1, column=3, sticky="w", padx=5, pady=5)

        tk.Label(khung_nhap, text="Ghi chú:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(khung_nhap, textvariable=self.var_ghichu, width=57).grid(row=2, column=1, columnspan=3,
                                                                          sticky="ew", padx=5, pady=5)
        tk.Button(khung_nhap, text="＋  Thêm giao dịch", command=self.them, bg="#287A43", fg="white",
                  activebackground="#1E6335", relief="flat", font=("Segoe UI", 9, "bold"),
                  padx=14, pady=7).grid(row=3, column=0, columnspan=4, pady=(8, 3))
        khung_nhap.columnconfigure(3, weight=1)

        khung_ds = tk.LabelFrame(self, text=" Danh sách giao dịch ", padx=8, pady=8,
                                 font=("Segoe UI", 9, "bold"))
        khung_ds.pack(fill="both", expand=True, padx=14, pady=7)
        cot = ("id", "ngay", "loai", "danh_muc", "so_tien", "ghi_chu")
        self.bang = ttk.Treeview(khung_ds, columns=cot, show="headings", selectmode="browse")
        headers = [("id", "ID", 42), ("ngay", "Ngày", 92), ("loai", "Loại", 60),
                   ("danh_muc", "Danh mục", 115), ("so_tien", "Số tiền (VNĐ)", 125),
                   ("ghi_chu", "Ghi chú", 210)]
        for key, title, width in headers:
            self.bang.heading(key, text=title)
            self.bang.column(key, width=width, anchor="center" if key in ("id", "ngay", "loai") else "w")
        self.bang.pack(side="left", fill="both", expand=True)
        scroll = ttk.Scrollbar(khung_ds, orient="vertical", command=self.bang.yview)
        scroll.pack(side="right", fill="y")
        self.bang.configure(yscrollcommand=scroll.set)
        self.bang.bind("<<TreeviewSelect>>", self.chon_giao_dich)

        khung_nut = tk.Frame(self)
        khung_nut.pack(fill="x", padx=14, pady=(3, 5))
        tk.Button(khung_nut, text="Cập nhật giao dịch", command=self.sua, bg="#2457A6", fg="white",
                  relief="flat", padx=12, pady=8).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Xóa giao dịch", command=self.xoa, bg="#B42318", fg="white",
                  relief="flat", padx=12, pady=8).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Làm mới", command=self.lam_moi, bg="#E8EEF8", fg="#173B67",
                  relief="flat", padx=12, pady=8).pack(side="left", padx=5)
        tk.Button(khung_nut, text="📊 Thống kê biểu đồ", command=self.thong_ke, bg="#E6A23C", fg="white",
                  activebackground="#CF8D25", relief="flat", font=("Segoe UI", 9, "bold"),
                  padx=15, pady=8).pack(side="right", padx=5)

        self.lbl_tong = tk.Label(self, text="", fg="#52657D", font=("Segoe UI", 9))
        self.lbl_tong.pack(anchor="e", padx=20, pady=(0, 8))

    def _doi_loai(self, _event=None):
        ds = DANH_MUC_THU if self.var_loai.get() == "Thu" else DANH_MUC_CHI
        self.combo_dm["values"] = ds
        if self.var_dm.get() not in ds:
            self.var_dm.set(ds[0])

    def _du_lieu_form(self):
        ngay = self.var_ngay.get().strip()
        try:
            datetime.strptime(ngay, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Ngày phải đúng định dạng YYYY-MM-DD, ví dụ 2026-11-06.")
        loai = self.var_loai.get()
        danh_muc = self.var_dm.get().strip()
        ghi_chu = self.var_ghichu.get().strip()
        try:
            tien = float(self.var_tien.get().replace(",", "").replace(" ", ""))
        except ValueError:
            raise ValueError("Số tiền phải là một số hợp lệ.")
        if tien <= 0:
            raise ValueError("Số tiền phải lớn hơn 0.")
        if not danh_muc:
            raise ValueError("Vui lòng chọn danh mục.")
        return ngay, loai, danh_muc, tien, ghi_chu

    def them(self):
        try:
            db.them_giao_dich(*self._du_lieu_form())
            self.tai_lai_danh_sach()
            self.lam_moi()
            messagebox.showinfo("Thành công", "Đã thêm giao dịch.")
        except ValueError as e:
            messagebox.showerror("Dữ liệu không hợp lệ", str(e))

    def sua(self):
        selected = self.bang.selection()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Hãy chọn giao dịch cần cập nhật trong danh sách.")
            return
        try:
            id_gd = int(self.bang.item(selected[0], "values")[0])
            db.sua_giao_dich(id_gd, *self._du_lieu_form())
            self.tai_lai_danh_sach()
            self.lam_moi()
            messagebox.showinfo("Thành công", "Đã cập nhật giao dịch.")
        except ValueError as e:
            messagebox.showerror("Dữ liệu không hợp lệ", str(e))

    def xoa(self):
        selected = self.bang.selection()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Hãy chọn giao dịch cần xóa.")
            return
        values = self.bang.item(selected[0], "values")
        if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa giao dịch #{values[0]}?"):
            db.xoa_giao_dich(int(values[0]))
            self.tai_lai_danh_sach()
            self.lam_moi()

    def lam_moi(self):
        self.var_ngay.set(date.today().strftime("%Y-%m-%d"))
        self.var_loai.set("Chi")
        self._doi_loai()
        self.var_dm.set(DANH_MUC_CHI[0])
        self.var_tien.set("")
        self.var_ghichu.set("")
        self.bang.selection_remove(self.bang.selection())

    def chon_giao_dich(self, _event=None):
        selected = self.bang.selection()
        if not selected:
            return
        values = self.bang.item(selected[0], "values")
        self.var_ngay.set(values[1])
        self.var_loai.set(values[2])
        self._doi_loai()
        self.var_dm.set(values[3])
        self.var_tien.set(str(values[4]).replace(",", ""))
        self.var_ghichu.set(values[5])

    def tai_lai_danh_sach(self):
        rows = db.lay_tat_ca_giao_dich()
        self.bang.delete(*self.bang.get_children())
        for r in rows:
            self.bang.insert("", "end", values=(r["id"], r["ngay"], r["loai"], r["danh_muc"],
                                                  f'{r["so_tien"]:,.0f}', r["ghi_chu"]))
        summary = db.tong_hop_thang()
        self.lbl_tong.config(text=(f"Tổng thu tháng này: {summary['tong_thu']:,.0f} VNĐ     "
                                   f"Tổng chi: {summary['tong_chi']:,.0f} VNĐ     "
                                   f"Số dư: {summary['so_du']:,.0f} VNĐ     |     "
                                   f"Tổng số giao dịch: {len(rows)}"))

    def thong_ke(self):
        rows = db.thong_ke_theo_danh_muc(None, "Chi")
        if not rows:
            messagebox.showinfo("Chưa có dữ liệu", "Chưa có khoản chi nào để thống kê.")
            return
        labels = [r["danh_muc"] for r in rows]
        values = [r["tong"] for r in rows]
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(labels, values, color="cornflowerblue")
        ax.set_title("THỐNG KÊ CHI TIÊU THEO DANH MỤC")
        ax.set_xlabel("Danh mục")
        ax.set_ylabel("Tổng số tiền (VNĐ)")
        ax.ticklabel_format(axis="y", style="plain")
        ax.tick_params(axis="x", labelrotation=20)
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    UngDungChiTieu().mainloop()