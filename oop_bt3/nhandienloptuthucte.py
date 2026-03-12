class Dog:
    def __init__(self, ten, mau_sac, giong, cam_xuc):
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc
    def sua(self):
        print(f"{self.ten} đang sủa: Gâu gâu!")
    def vay_duoi(self):
        print(f"{self.ten} đang vẫy đuôi mừng.")
    def an(self):
        print(f"{self.ten} đang ăn cơm.")
    def chay(self):
        print(f"{self.ten} đang chạy tung tăng.")
class Car:
    def __init__(self, hang, kich_thuoc, mau, gia):
        self.hang = hang
        self.kich_thuoc = kich_thuoc
        self.mau = mau
        self.gia = gia
    def tang_toc(self):
        print(f"Xe {self.hang} đang tăng tốc...")
    def giam_toc(self):
        print(f"Xe {self.hang} đang giảm tốc độ.")
    def dam(self):
        print("Cảnh báo: Xe đã xảy ra va chạm!")
class Account:
    def __init__(self, ten_tk, so_tk, ngan_hang, so_du):
        self.ten_tk = ten_tk
        self.so_tk = so_tk
        self.ngan_hang = ngan_hang
        self.so_du = so_du
    def rut_tien(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            print(f"Đã rút {so_tien}. Số dư còn lại: {self.so_du}")
        else:
            print("Số dư không đủ!")
    def gui_tien(self, so_tien):
        self.so_du += so_tien
        print(f"Đã gửi {so_tien}. Số dư mới: {self.so_du}")
    def kiem_tra_so_du(self):
        print(f"Số dư tài khoản {self.so_tk}: {self.so_du}")
