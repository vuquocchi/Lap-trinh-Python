import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QMessageBox
)
from PyQt5.QtCore import Qt


class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()

        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        self.setWindowTitle("May tinh bo tui")
        self.setFixedSize(320, 420)

        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setPlaceholderText("0")
        self.man_hinh.setMinimumHeight(60)

        self.man_hinh.setStyleSheet("""
            QLineEdit {
                font-size: 26px;
                padding: 10px;
                border: 2px solid #888888;
                border-radius: 8px;
                background-color: white;
            }
        """)

        cac_nut = [
            ["C", "DEL", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "(", ")"]
        ]

        bo_cuc_nut = QGridLayout()
        bo_cuc_nut.setSpacing(8)

        for hang, danh_sach_nut in enumerate(cac_nut):
            for cot, ky_tu in enumerate(danh_sach_nut):
                nut = QPushButton(ky_tu)
                nut.setMinimumSize(60, 52)
                nut.setStyleSheet("""
                    QPushButton {
                        font-size: 18px;
                        border-radius: 8px;
                        background-color: #E8E8E8;
                    }
                    QPushButton:hover {
                        background-color: #D0D0D0;
                    }
                    QPushButton:pressed {
                        background-color: #AAAAAA;
                    }
                """)

                nut.clicked.connect(
                    lambda checked=False, gia_tri=ky_tu:
                    self.xu_ly_nut(gia_tri)
                )

                bo_cuc_nut.addWidget(nut, hang, cot)

        bo_cuc_chinh = QVBoxLayout()
        bo_cuc_chinh.setSpacing(12)
        bo_cuc_chinh.addWidget(self.man_hinh)
        bo_cuc_chinh.addLayout(bo_cuc_nut)

        self.setLayout(bo_cuc_chinh)

    def xu_ly_nut(self, ky_tu):
        if ky_tu == "C":
            self.man_hinh.clear()

        elif ky_tu == "DEL":
            noi_dung = self.man_hinh.text()
            self.man_hinh.setText(noi_dung[:-1])

        elif ky_tu == "=":
            self.tinh_ket_qua()

        else:
            noi_dung = self.man_hinh.text()
            self.man_hinh.setText(noi_dung + ky_tu)

    def tinh_ket_qua(self):
        bieu_thuc = self.man_hinh.text()

        if bieu_thuc == "":
            return

        ky_tu_hop_le = "0123456789+-*/.() "

        if any(ky_tu not in ky_tu_hop_le for ky_tu in bieu_thuc):
            QMessageBox.warning(
                self, "Loi", "Bieu thuc khong hop le!"
            )
            return

        try:
            ket_qua = eval(
                bieu_thuc,
                {"__builtins__": {}},
                {}
            )

            if not isinstance(ket_qua, (int, float)):
                raise ValueError("Ket qua khong hop le")

            self.man_hinh.setText(str(ket_qua))

        except ZeroDivisionError:
            QMessageBox.warning(
                self, "Loi", "Khong the chia cho 0!"
            )

        except (SyntaxError, ValueError, TypeError, OverflowError):
            QMessageBox.warning(
                self, "Loi", "Bieu thuc khong hop le!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cua_so = MayTinhBoTui()
    cua_so.show()

    sys.exit(app.exec_())