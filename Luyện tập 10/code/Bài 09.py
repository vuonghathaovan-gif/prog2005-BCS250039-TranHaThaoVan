class Xe:
    so_luong_xe = 0
    def __init__(self, bien_so, hang_xe, nam_san_xuat):
        self.bien_so = bien_so
        self.hang_xe = hang_xe
        self.nam_san_xuat = nam_san_xuat
        Xe.so_luong_xe += 1
    @property
    def bien_so(self):
        return self.__bien_so
    @bien_so.setter
    def bien_so(self, gia_tri):
        if len(gia_tri) < 4:
            raise ValueError("4 ký tự")
        self.__bien_so = gia_tri
    @property
    def hang_xe(self):
        return self.__hang_xe
    @hang_xe.setter
    def hang_xe(self, gia_tri):
        hang_hop_le = ["Toyota", "Honda", "Ford", "Mazda"]
        if gia_tri not in hang_hop_le:
            raise ValueError("Not hãng")
        self.__hang_xe = gia_tri
    def __str__(self):
        return "Xe: " + self.__hang_xe + " | " + self.__bien_so + " | Năm: " + str(self.nam_san_xuat)
    def tuoi_xe(self):
        return 2025 - self.nam_san_xuat
    @classmethod
    def get_so_luong(cls):
        return "Tổng số xe: " + str(cls.so_luong_xe)
    @staticmethod
    def la_xe_cu(nam):
        return nam < 2010
    def __eq__(self, other):
        if not isinstance(other, Xe):
            return False
        return self.__bien_so == other.__bien_so
class XeTai(Xe):
    def __init__(self, bien_so, hang_xe, nam_san_xuat, tai_trong):
        super().__init__(bien_so, hang_xe, nam_san_xuat)
        self.tai_trong = tai_trong
    @property
    def tai_trong(self):
        return self.__tai_trong
    @tai_trong.setter
    def tai_trong(self, gia_tri):
        if gia_tri <= 0:
            raise ValueError("Tải trọng>0")
        self.__tai_trong = gia_tri
    def __str__(self):
        return "Xe: " + self.hang_xe + " | " + self.bien_so + " | Tải trọng: " + str(self.__tai_trong) + " tấn"
    def co_qua_tai(self, hang_hoa):
        return hang_hoa > self.__tai_trong
    @staticmethod
    def phan_loai(tai_trong):
        if tai_trong >= 10:
            return "Nặng"
        return "Nhẹ"
    def __eq__(self, other):
        if not isinstance(other, XeTai):
            return False
        return self.bien_so == other.bien_so and self.__tai_trong == other.__tai_trong
xe1 = Xe("51A-123", "Toyota", 2015)
print(xe1)
print("Tuổi:", xe1.tuoi_xe(), "năm")
print(Xe.get_so_luong())
print("2008 là xe cũ?", Xe.la_xe_cu(2008))
xt1 = XeTai("51C-111", "Ford", 2018, 5)
print(xt1)
print("Qua tải?", xt1.co_qua_tai(10))
print(XeTai.phan_loai(15))