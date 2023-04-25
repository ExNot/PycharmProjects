class Asdf:
    kalan = 3
    def saldiri(self):
        print("Saldırı gerçekleştirildi")
        self.kalan -=1

    def canli_mi(self):
        if(self.kalan<=0):
            print("Öldü")
        else:
            print(str(self.kalan) + "canı kaldı")

oyuncu1 = Asdf()
oyuncu2 = Asdf()

oyuncu1.saldiri(oyuncu2)
oyuncu1.saldiri()
oyuncu1.saldiri()

oyuncu1.canli_mi()