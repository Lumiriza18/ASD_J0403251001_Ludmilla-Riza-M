#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Latihan 4: kombinasi huruf
#================================================

def kombinasi(n,hasil=""): #langkah awal fungsi dengan teks kosong ""

    if len(hasil)==n:
        print(hasil)
        return
    kombinasi(n,hasil + "A") #cabang kiri: pilihan untuk selalu mencoba menambahkan huruf "A" terlebih dahulu
    kombinasi(n,hasil + "B") #cabang kanan: pilihan untuk menambahkan huruf "B" setelah urusan dengan huruf "selesai"
kombinasi(2)
"""
kombinasi(2, "")

➜ kombinasi(2, "A")

➜ kombinasi(2, "AA") -> Cetak AA

➜ kombinasi(2, "AB") -> Cetak AB

➜ kombinasi(2, "B")

➜ kombinasi(2, "BA") -> Cetak BA

➜ kombinasi(2, "BB") -> Cetak BB
"""