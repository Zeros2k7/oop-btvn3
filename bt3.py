#y/c1:
class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
    def __str__(self):
        return f"Họ tên: {self.ho_ten:15} Tuổi: {self.tuoi:2} GT: {self.gioi_tinh:5} ĐC: {self.dia_chi}"
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec
#y/c2:
class QLCB:
    def __init__(self):
        self.danh_sach_can_bo = []

    def them_moi_can_bo(self, can_bo):
        self.danh_sach_can_bo.append(can_bo)
        print("=> Đã thêm cán bộ thành công!")

    def tim_kiem_theo_ten(self, ten):
        ket_qua = [cb for cb in self.danh_sach_can_bo if ten.lower() in cb.ho_ten.lower()]
        if not ket_qua:
            print(f"Không tìm thấy cán bộ có tên: {ten}")
        else:
            print(f"--- Kết quả tìm kiếm cho '{ten}' ---")
            for cb in ket_qua:
                print(cb)

    def hien_thi_danh_sach(self):
        if not self.danh_sach_can_bo:
            print("Danh sách trống.")
        else:
            print("--- Danh sách toàn bộ cán bộ ---")
            for cb in self.danh_sach_can_bo:
                print(cb)