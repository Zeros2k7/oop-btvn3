class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_san_xuat = nha_san_xuat
        self.gia = gia
    
    def get_ma_hang(self):
        return self.ma_hang