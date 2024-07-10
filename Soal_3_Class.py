antrian = []

def menu():
    print('Pilihan : ')
    print('1. Tambah Antrian')
    print('2. Hapus Antrian')
    print('3. Keluar')
    print('\n')

def tambah_antrian(antrian):
    nama = input("Masukkan nama pelanggan: ")
    antrian.append(nama)

def hapus_antrian(antrian):
    if antrian:
        antrian.pop(0)
    else:
        return "Antrian kosong."