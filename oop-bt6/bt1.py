from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    """Ngoại lệ khi giá hàng hóa < 0"""
    pass
class MaHangTrungLap(Exception):
    """Ngoại lệ khi mã hàng đã tồn tại trong danh sách"""
    pass
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.gia = gia 
    @property
    def ma_hang(self):
        return self._ma_hang
    @property
    def ten_hang(self):
        return self._ten_hang
    @property
    def gia(self):
        return self._gia
    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(f"Lỗi: Giá '{value}' không hợp lệ (phải >= 0).")
        self._gia = value
    @abstractmethod
    def loai_hang(self):
        pass
    @abstractmethod
    def in_ttin(self):
        pass
    def __str__(self):
        return f"[{self.loai_hang()}] {self.ma_hang} - {self.ten_hang}: {self.gia:,} VNĐ"
    def __eq__(self, other):
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False
    def __lt__(self, other):
        if isinstance(other, HangHoa):
            return self.gia < other.gia
        return False
    def __hash__(self):
        return hash(self.ma_hang)
class HangDienMay(HangHoa):
    def loai_hang(self):
        return "Điện máy"
    def in_ttin(self):
        return f"{self.__str__()} (Bảo hành 12 tháng)"
class HangSanhSu(HangHoa):
    def loai_hang(self):
        return "Sành sứ"
    def in_ttin(self):
        return f"{self.__str__()} (Loại hàng dễ vỡ)"
class HangThucPham(HangHoa):
    def loai_hang(self):
        return "Thực phẩm"
    def in_ttin(self):
        return f"{self.__str__()} (Cần bảo quản lạnh)"
class QuanLyHangHoa:
    def __init__(self):
        self.danh_sach = []
    def them_hang(self, hang):
        if any(h.ma_hang == hang.ma_hang for h in self.danh_sach):
            raise MaHangTrungLap(f"Lỗi: Mã hàng '{hang.ma_hang}' đã tồn tại!")
        self.danh_sach.append(hang)
    def luu_file(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for hang in self.danh_sach:
                    f.write(f"{hang.loai_hang()}|{hang.ma_hang}|{hang.ten_hang}|{hang.gia}\n")
            print(f"--- Đã lưu {len(self.danh_sach)} mặt hàng vào file {filename} ---")
        except Exception as e:
            print(f"Lỗi khi lưu file: {e}")
    def hien_thi(self):
        for hang in sorted(self.danh_sach):
            print(hang.in_ttin())