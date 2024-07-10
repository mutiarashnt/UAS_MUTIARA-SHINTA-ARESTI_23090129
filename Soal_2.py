data = [
    ["Mahasiswa_1", 90, 80],
    ["Mahasiswa_2", 50, 60],
    ["Mahasiswa_3", 65, 70]
]

algoritma = 0
matematika = 0
jumlah_mahasiswa = len(data)

rata_rata = []

for mahasiswa in data:
    nama = mahasiswa[0]
    nilai_algoritma = mahasiswa[1]
    nilai_matematika = mahasiswa[2]
    
    algoritma += nilai_algoritma
    matematika += nilai_matematika
    
    rata_rata = (nilai_algoritma + nilai_matematika) / 2
    rata_rata.append((nama, rata_rata))

rata_rata_algoritma = algoritma / jumlah_mahasiswa
rata_rata_matematika_numerik = matematika / jumlah_mahasiswa

print(f"Rata-rata nilai Algoritma: {rata_rata_algoritma:.2f}")
print(f"Rata-rata nilai Matematika Numerik: {rata_rata_matematika_numerik:.2f}")
print('\n')

print("Rata-rata nilai untuk setiap mahasiswa:")
for nama, rata_rata in rata_rata:
    print(f"{nama}: {rata_rata:.2f}")