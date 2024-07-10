class Buah:
    def __init__(self,inputNama, inputWarna, inputRasa):
        self.nama = inputNama 
        self.warna = inputWarna
        self.rasa = inputRasa

    def info_buah(self):
        return f'Nama : {self.nama}, Warna : {self.warna}'
    
class Mangga(Buah):
    def __init__(self, nama, warna, jenis, vitamin):
        Buah.__init__(self, nama, warna, jenis)
        self.vitamin = vitamin

    def info_mangga(self):
        return f'{self.info_buah()}, Vitamin : {self.vitamin}'
    
arum_manis = Mangga('Arum Manis', 'Hijau', 'Manis')
print(arum_manis.info_mangga())