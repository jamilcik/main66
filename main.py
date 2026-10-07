class Bog:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.daraxtlar = []

    def daraxt_qoshish(self, daraxt):
        self.daraxtlar.append(daraxt)

    def malumot(self):
        print("Bog':", self.nomi)
        print("Manzil:", self.manzil)
        print("Daraxtlar:", self.daraxtlar)


bog = Bog("Jamil Bog'i", "Samarqand")

bog.daraxt_qoshish("Olma")
bog.daraxt_qoshish("Anor")
bog.daraxt_qoshish("O'rik")

bog.malumot()
