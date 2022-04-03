from dbm import dumb


class Kalkulator:
    mutableToAll = [1, 2, 3]

    def __init__(self, hai="Dumb") -> None:
        self.hai = hai
        self.yo = 12345

    def hitung(self):
        print("Hai ", self.hai)

    def me_static():
        print("This is me static")


objz = Kalkulator(hai="Hi")
print(objz.yo)
objz.hitung()

objA = Kalkulator("Zoo")
objA.hitung()
objA.mutableToAll.append(5)

print("The ist of OBJZ is : ", objz.mutableToAll)
