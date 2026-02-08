#====================================================
#TUGAS HANDS-ON 1
#STUDI KASUS:SISTEM STOCK BARANG KANTIN(BERBASISFILE .txt)
#
#Nama:Ludmilla Riza Maharuni
#NIM:J0403251001
#Kelas:B2
#====================================================

#--------------------------------------------
#konstanta nama file
#--------------------------------------------
nama_file = "Stok_Barang.txt"

#====================================================
#fungsi membaca file
#====================================================
def baca_data_barang(nama_file):
    """
    membaca data barang dari file
    format Per baris:nomor_barang,nama_barang
    stok barang
    """
    data_dict={}
    with open(nama_file,"r",encoding="utf_8") as file:
        for baris in file:
            baris=baris.strip()
            #lewati baris kosong
            if baris=="":
                continue
            parts=baris.split(",")
            if len(parts)!=3:
                continue
            nomor_barang,nama_barang,stok_str=parts
            try:
                stok_int=int(stok_str)
            except ValueError:
                continue
            data_dict[nomor_barang]={"nama_barang":nama_barang,
                                     "stok":stok_str}
        return data_dict
#--------Program Utama Latihan 1--------
data_barang=baca_data_barang(nama_file)
print("==== latiahan 1 selesai====")
print("jumlah dataterbaca:",len(data_barang))

#====================================================
#Latihan 2: Tampilkan semua data mahasiswa
#====================================================
def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("barang kosong")
        return
    
"""
    tampilan yang rapi, atur f_string formatting
    {nomor barang:<10} artainya:
    tampilan nomor barang<= rata kiri dengan 10=lebar kolom 10 keakrakter
    {nama barang:<12} artinya:
    tampilkan nama rata kiri dengan lebar kolom 12 karakter
    {stok:>5} aratinya :
    tampilkan stok >= rata kanan dengan lebar kolom 5 karakter
    (buiar angka sejajar)
"""
    print("================daftar Mahasiswa================")

    #membuat header tabel
    print(f"{"nomor barang":<10}|{"nama barang":<12}|{"stok":>5}")
    print("-"*32) #buat garis header tabel
    #pengulangan untuk mencetak data:
    for nomor_barang in sorted(data_dict):
        nama_barang=data_dict[nomor_barang]["nama_barang"]
        stok=data_dict[nomor_barang]["stok"]
        print(f"{nomor_barang:<10}|{nama_barang:<12}|{stock:>5}")
        tampilkan_data(data_barang)

#====================================================
#latihan 3: cari mahasiswa berdasarkan nomor barang
#====================================================
def cari_barang(data_dict):
    #mencari barang berdasarkan nomor barang
    nomor_cari=input("masukkan nomor barnag yang di cari:").strip()
    if nomor_cari in data_dict:
        nama_barang=data_dict[nomor_cari]["nama_barang"]
        stok=data_dict[nomor_cari]["stok"]

print("\n===== Data Mahasiswa Ditemukan=======")
print(f"nomor barang: {nomor_cari}")
print(f"nama_barang: {nama_barang}")
print(f"stok: {stok}")