## ================= PROGRAM 1: MEMBUAT LIST =================
print("=== PROGRAM 1: MEMBUAT LIST ===")

nilai_quiz = [8, 3, 9, 6]
print(nilai_quiz)

nama_buah = ["apel", "mangga", "jeruk"]
print(nama_buah)

status_lulus = [True, True, False, True]
print(status_lulus)

campuran = [10, "kopi", 20, "teh", "susu", False, "roti", True]
print(campuran)

# Cara alternatif: range()
deret = range(1, 20, 3)  # range(start, stop, step)
print(deret)
deret_list = list(deret)
print(deret_list)

# List comprehension
pangkat_tiga = [x ** 3 for x in range(0, 8)]
print(pangkat_tiga)

# List comprehension dengan if
bukan_tiga = [x for x in range(0, 10) if x != 3]
print(bukan_tiga)

kelipatan_tiga = [x for x in range(0, 20) if x % 3 == 0]
print(kelipatan_tiga)

bukan_kelipatan_tiga = [x for x in range(0, 10) if x % 3 != 0]
print(bukan_kelipatan_tiga)


## ================= PROGRAM 2: MANIPULASI LIST =================
print("\n=== PROGRAM 2: MANIPULASI LIST ===")

# index  0(-3)  1(-2)  2(-1)
hewan = ["Kucing", "Kelinci", "Hamster"]

# Mengambil data
hewan_pertama = hewan[0]
print(f"hewan pertama (index 0) = {hewan_pertama}")

hewan_terakhir = hewan[-1]
print(f"hewan terakhir adalah = {hewan_terakhir}")

# Jumlah data
jumlah_hewan = len(hewan)
print(f"jumlah hewan = {jumlah_hewan}")

# insert(posisi, item)
print(f"sebelum ditambah = \n{hewan}")
hewan.insert(2, "Burung")
print(f"sesudah insert = \n{hewan}")

# append
hewan.append("Ikan")
print(f"sesudah append = \n{hewan}")

# extend
hewan_liar = ["Harimau", "Gajah", "Zebra"]
hewan.extend(hewan_liar)
print(f"sesudah extend = \n{hewan}")

# Mengubah data (index 1 menjadi Kura-kura)
hewan[1] = "Kura-kura"
print(f"sesudah diubah = \n{hewan}")

# remove
hewan.remove("Kucing")
print(f"sesudah remove = \n{hewan}")

# pop (hapus paling belakang)
hewan.pop()
print(f"sesudah pop = \n{hewan}")


## ================= PROGRAM 3: OPERASI LIST =================
print("\n=== PROGRAM 3: OPERASI LIST ===")

skor = [7, 2, 7, 5, 9, 1, 5, 7, 3, 5, 8, 2, 6, 0]
print(f"skor = \n{skor}")

# count
jumlah_7 = skor.count(7)
jumlah_5 = skor.count(5)
print(f"jumlah angka 7 = {jumlah_7}")
print(f"jumlah angka 5 = {jumlah_5}")

# index
kota = ["Bandung", "Medan", "Surabaya", "Makassar"]
print(f"kota = {kota}")

index_medan = kota.index("Medan")
index_makassar = kota.index("Makassar")
print(f"index Medan = {index_medan}")
print(f"index Makassar = {index_makassar}")

# sort
print(f"skor sebelum sort = \n{skor}")
skor.sort()
print(f"skor sesudah sort = \n{skor}")

print(f"kota sebelum sort = {kota}")
kota.sort()
print(f"kota sesudah sort = {kota}")

# reverse
skor.reverse()
kota.reverse()
print(f"skor di-reverse = \n{skor}")
print(f"kota di-reverse = \n{kota}")


## ================= PROGRAM 4: NESTED LIST =================
print("\n=== PROGRAM 4: NESTED LIST ===")

baris_a = [10, 20]
baris_b = [30, 40]
list_biasa = [10, 20, 30, 40]
print(f"list biasa = {list_biasa}")

list_2d = [baris_a, baris_b, 50, 60]
print(f"list 2D = {list_2d}")

# Contoh penggunaan: data mahasiswa
mhs_0 = ["Dina", 19, "Perempuan"]
mhs_1 = ["Bayu", 20, "Laki-laki"]
mhs_2 = ["Citra", 21, "Perempuan"]

daftar_mhs = [mhs_0, mhs_1, mhs_2]
print(f"daftar mahasiswa = {daftar_mhs}")

for mhs in daftar_mhs:
    print(f"nama\t : {mhs[0]}")
    print(f"umur\t : {mhs[1]}")
    print(f"gender\t : {mhs[2]}\n")


## ================= LATIHAN =================
print("=== LATIHAN 1 ===")
alat_tulis = ["pulpen", "buku", "penghapus", "spidol"]
alat_tulis.append("stabilo")            # a. tambah di akhir
print("a.", alat_tulis)
alat_tulis.insert(1, "penggaris")       # b. sisip di index 1
print("b.", alat_tulis)
alat_tulis.pop()                        # c. hapus paling belakang
print("c.", alat_tulis)
alat_tulis[alat_tulis.index("penghapus")] = "tipe-x"   # d. ubah elemen
print("d.", alat_tulis)
print("e. jumlah data =", len(alat_tulis))  # e. jumlah data

print("\n=== LATIHAN 2 ===")
nilai_ujian = [60, 85, 70, 95, 60, 100, 75]
print("a. nilai 95 ada di index ke-", nilai_ujian.index(95))
print("b. jumlah nilai 60 =", nilai_ujian.count(60))
nilai_ujian.sort()
print("c.", nilai_ujian)
nilai_ujian.reverse()
print("d.", nilai_ujian)

print("\n=== LATIHAN 3 ===")
minuman_utama = ["Kopi", "Teh"]
minuman_tambahan = ["Jus Jeruk", "Air Mineral"]
minuman_utama.extend(minuman_tambahan)
print("Data gabungan:", minuman_utama)

print("\n=== LATIHAN 4 ===")
data_makanan = [["Bakso", 15000], ["Siomay", 12000], ["Batagor", 10000]]
print("a. Harga Siomay =", data_makanan[1][1])
for makanan in data_makanan:
    print(f"Nama: {makanan[0]}, Harga: {makanan[1]}")
