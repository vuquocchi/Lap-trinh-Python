import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QListWidget, QVBoxLayout,
    QHBoxLayout, QMessageBox
)


class UngDungToDo(QWidget):
    def __init__(self):
        super().__init__()

        # Danh sach luu (noi_dung, da_hoan_thanh)
        self.danh_sach_cong_viec = []

        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        self.setWindowTitle("Ghi chu cong viec - PyQt")
        self.resize(420, 420)

        # Tieu de
        tieu_de = QLabel("GHI CHU CONG VIEC")
        tieu_de.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        # O nhap cong viec
        self.o_nhap_cong_viec = QLineEdit()
        self.o_nhap_cong_viec.setPlaceholderText(
            "Nhap cong viec moi..."
        )

        # Nut them
        nut_them = QPushButton("Them")
        nut_them.clicked.connect(self.them_cong_viec)

        hang_nhap = QHBoxLayout()
        hang_nhap.addWidget(self.o_nhap_cong_viec)
        hang_nhap.addWidget(nut_them)

        # Danh sach cong viec
        self.danh_sach_hien_thi = QListWidget()

        # Nut danh dau hoan thanh
        nut_hoan_thanh = QPushButton("Danh dau hoan thanh")
        nut_hoan_thanh.clicked.connect(
            self.danh_dau_hoan_thanh
        )

        # Nut xoa
        nut_xoa = QPushButton("Xoa cong viec")
        nut_xoa.clicked.connect(self.xoa_cong_viec)

        hang_nut = QHBoxLayout()
        hang_nut.addWidget(nut_hoan_thanh)
        hang_nut.addWidget(nut_xoa)

        # Bo cuc chinh
        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(tieu_de)
        layout_chinh.addLayout(hang_nhap)
        layout_chinh.addWidget(self.danh_sach_hien_thi)
        layout_chinh.addLayout(hang_nut)

        self.setLayout(layout_chinh)

    def lam_moi_danh_sach(self):
        self.danh_sach_hien_thi.clear()

        for noi_dung, da_hoan_thanh in self.danh_sach_cong_viec:
            if da_hoan_thanh:
                tien_to = "[Da xong] "
            else:
                tien_to = "[Chua xong] "

            self.danh_sach_hien_thi.addItem(
                tien_to + noi_dung
            )

    def them_cong_viec(self):
        noi_dung = self.o_nhap_cong_viec.text().strip()

        if noi_dung == "":
            QMessageBox.critical(
                self,
                "Loi",
                "Vui long nhap noi dung cong viec!"
            )
            return

        self.danh_sach_cong_viec.append((noi_dung, False))

        self.o_nhap_cong_viec.clear()
        self.lam_moi_danh_sach()

    def xoa_cong_viec(self):
        vi_tri = self.danh_sach_hien_thi.currentRow()

        if vi_tri < 0:
            QMessageBox.critical(
                self,
                "Loi",
                "Vui long chon cong viec can xoa!"
            )
            return

        self.danh_sach_cong_viec.pop(vi_tri)
        self.lam_moi_danh_sach()

    def danh_dau_hoan_thanh(self):
        vi_tri = self.danh_sach_hien_thi.currentRow()

        if vi_tri < 0:
            QMessageBox.critical(
                self,
                "Loi",
                "Vui long chon cong viec can danh dau!"
            )
            return

        noi_dung, _ = self.danh_sach_cong_viec[vi_tri]

        self.danh_sach_cong_viec[vi_tri] = (
            noi_dung, True
        )

        self.lam_moi_danh_sach()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cua_so = UngDungToDo()
    cua_so.show()

    sys.exit(app.exec_())