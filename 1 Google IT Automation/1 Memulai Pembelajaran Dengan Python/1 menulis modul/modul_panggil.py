def myFunction():
    print("Hello World")

nama = "Theo"

class Reviewer:
    def __init__(self, nama, kelas) -> None:
        self.nama = nama
        self.kelas = kelas

    def review(self):
        print("Reviewer %s bertanggung jawab di kelas %s"%(self.nama, self.kelas))