def data():
    informasi = []


    while True:
        nim = int(input('Masukkan NIM : '))
        nama = str(input('Masukkan Nama : '))

        mahasiswa = {'nim' : nim, 'nama' : nama}
        informasi.append(mahasiswa)

        tambah = int(input('Ingin Tambah Lagi? (ya/tidak : )'))
        if tambah == 'ya':
           data
        else: 
            print(informasi)

def tampil():
    print('Data Barang yang Telah Diinput')
    for i in informasi:
        print(f"NIM : {i['NIM']}, Nama : {i['Nama']}")
    print('\n')