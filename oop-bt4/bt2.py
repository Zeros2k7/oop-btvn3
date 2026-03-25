class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = max(0.1, he_so_luong)
        self.luong_toi_da = luong_toi_da

    def hien_thi_tt(self):
        print(f"[{self.ma_nv}] {self.ho_ten} | HSL: {self.he_so_luong}", end=" | ")
class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap_ld = phu_cap_ld

    def hien_thi_tt(self):
        super().hien_thi_tt()
        print(f"Loại: CTV | Hạn HD: {self.thoi_han_hd} | Phụ cấp: {self.phu_cap_ld}")
class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri = vi_tri

    def hien_thi_tt(self):
        super().hien_thi_tt()
        print(f"Loại: Chính thức | Vị trí: {self.vi_tri}")
class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_ql, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_ql = ngay_ql
        self.phu_cap_ql = phu_cap_ql

    def hien_thi_tt(self):
        super().hien_thi_tt()
        print(f"Loại: Trưởng phòng | Ngày QL: {self.ngay_ql} | Phụ cấp QL: {self.phu_cap_ql}")