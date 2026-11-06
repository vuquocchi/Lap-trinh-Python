"""
Module CSDL cho ứng dụng Quản lý chi tiêu cá nhân.
Chỉ phụ trách lưu trữ và truy vấn dữ liệu; không phụ thuộc giao diện Tkinter.
"""
import sqlite3
import sys
import shutil
from pathlib import Path

if getattr(sys, "frozen", False):
    # Khi chạy EXE, lưu CSDL cạnh file EXE để dữ liệu không mất sau khi thoát.
    THU_MUC_DU_AN = Path(sys.executable).resolve().parent
    TEN_FILE_CSDL = THU_MUC_DU_AN / "chi_tieu.db"
    if not TEN_FILE_CSDL.exists():
        du_lieu_mau = Path(getattr(sys, "_MEIPASS", THU_MUC_DU_AN)) / "chi_tieu.db"
        if du_lieu_mau.exists():
            shutil.copy2(du_lieu_mau, TEN_FILE_CSDL)
else:
    THU_MUC_DU_AN = Path(__file__).resolve().parent
    TEN_FILE_CSDL = THU_MUC_DU_AN / "chi_tieu.db"

def ket_noi_csdl():
    """Tạo kết nối SQLite."""
    conn = sqlite3.connect(TEN_FILE_CSDL)
    conn.row_factory = sqlite3.Row
    return conn

def tao_bang_neu_chua_co():
    """Tạo bảng giao dịch nếu chưa tồn tại."""
    with ket_noi_csdl() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS chi_tieu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ngay TEXT NOT NULL,
                loai TEXT NOT NULL CHECK(loai IN ('Thu', 'Chi')),
                danh_muc TEXT NOT NULL,
                so_tien REAL NOT NULL CHECK(so_tien > 0),
                ghi_chu TEXT DEFAULT ''
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_chi_tieu_ngay ON chi_tieu(ngay)")
        conn.commit()

def them_giao_dich(ngay, loai, danh_muc, so_tien, ghi_chu=""):
    with ket_noi_csdl() as conn:
        cur = conn.execute(
            """INSERT INTO chi_tieu(ngay, loai, danh_muc, so_tien, ghi_chu)
               VALUES (?, ?, ?, ?, ?)""",
            (ngay, loai, danh_muc, float(so_tien), ghi_chu.strip())
        )
        conn.commit()
        return cur.lastrowid

def lay_tat_ca_giao_dich(tu_ngay=None, den_ngay=None, tu_khoa=None, loai=None):
    sql = """SELECT id, ngay, loai, danh_muc, so_tien, ghi_chu
             FROM chi_tieu WHERE 1=1"""
    params = []
    if tu_ngay:
        sql += " AND ngay >= ?"
        params.append(tu_ngay)
    if den_ngay:
        sql += " AND ngay <= ?"
        params.append(den_ngay)
    if tu_khoa:
        sql += " AND (danh_muc LIKE ? OR ghi_chu LIKE ?)"
        params.extend([f"%{tu_khoa}%", f"%{tu_khoa}%"])
    if loai and loai != "Tất cả":
        sql += " AND loai = ?"
        params.append(loai)
    sql += " ORDER BY ngay DESC, id DESC"
    with ket_noi_csdl() as conn:
        return conn.execute(sql, params).fetchall()

def sua_giao_dich(id_giao_dich, ngay, loai, danh_muc, so_tien, ghi_chu=""):
    with ket_noi_csdl() as conn:
        cur = conn.execute(
            """UPDATE chi_tieu
               SET ngay=?, loai=?, danh_muc=?, so_tien=?, ghi_chu=?
               WHERE id=?""",
            (ngay, loai, danh_muc, float(so_tien), ghi_chu.strip(), int(id_giao_dich))
        )
        conn.commit()
        return cur.rowcount > 0

def xoa_giao_dich(id_giao_dich):
    with ket_noi_csdl() as conn:
        cur = conn.execute("DELETE FROM chi_tieu WHERE id=?", (int(id_giao_dich),))
        conn.commit()
        return cur.rowcount > 0

def thong_ke_theo_danh_muc(thang=None, loai="Chi"):
    sql = """SELECT danh_muc, SUM(so_tien) AS tong
             FROM chi_tieu WHERE loai = ?"""
    params = [loai]
    if thang:
        sql += " AND substr(ngay, 1, 7) = ?"
        params.append(thang)
    sql += " GROUP BY danh_muc ORDER BY tong DESC"
    with ket_noi_csdl() as conn:
        return conn.execute(sql, params).fetchall()

def tong_hop_thang(thang=None):
    """Trả về tổng thu, tổng chi và chênh lệch trong tháng."""
    if thang is None:
        thang = __import__("datetime").date.today().strftime("%Y-%m")
    with ket_noi_csdl() as conn:
        row = conn.execute("""
            SELECT
              COALESCE(SUM(CASE WHEN loai='Thu' THEN so_tien ELSE 0 END), 0) AS tong_thu,
              COALESCE(SUM(CASE WHEN loai='Chi' THEN so_tien ELSE 0 END), 0) AS tong_chi
            FROM chi_tieu WHERE substr(ngay, 1, 7)=?
        """, (thang,)).fetchone()
    return {
        "tong_thu": row["tong_thu"],
        "tong_chi": row["tong_chi"],
        "so_du": row["tong_thu"] - row["tong_chi"]
    }

def dem_giao_dich():
    with ket_noi_csdl() as conn:
        return conn.execute("SELECT COUNT(*) FROM chi_tieu").fetchone()[0]
