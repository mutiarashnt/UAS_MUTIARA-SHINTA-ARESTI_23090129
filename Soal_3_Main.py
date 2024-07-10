import Soal_3_Class as sc

while True:
    sc.menu()
    pilihan = int(input('Masukkan pilihan : '))
    
    if pilihan == 1:
        sc.tambah_antrian()
    elif pilihan == 2:
        sc.hapus_antrian()
    elif pilihan == 3:
        exit()
    