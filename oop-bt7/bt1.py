import csv
import json

class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, loai, thong_tin):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.loai = loai
        self.thong_tin = thong_tin

    def to_dict(self):
        return {
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "loai": self.loai,
            "thong_tin": self.thong_tin
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["ho_ten"],
            int(data["tuoi"]),
            data["gioi_tinh"],
            data["dia_chi"],
            data["loai"],
            data["thong_tin"]
        )

def read_csv(filename):
    danh_sach = []
    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cb = CanBo(
                    row["ho_ten"], int(row["tuoi"]), row["gioi_tinh"],
                    row["dia_chi"], row["loai"], row["thong_tin"]
                )
                danh_sach.append(cb)
    except FileNotFoundError:
        print("Không tìm thấy file!") 
    return danh_sach

def save_json(filename, danh_sach):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([cb.to_dict() for cb in danh_sach], f)

def load_json(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
            return [CanBo.from_dict(d) for d in data]
class QuanLyCanBo:
    def __init__(self, filename="canbo.json"):
        self.danh_sach = []
        self.filename = filename

class QuanLyCanBo:
    def __init__(self):
        self.danh_sach = []

    def them(self, cb):
        self.danh_sach.append(cb)
        self.auto_save()

    def auto_save(self):
        save_json(self.filename, self.danh_sach)
        self.auto_save()

    def auto_save(self):
        save_json("canbo.json", self.danh_sach)