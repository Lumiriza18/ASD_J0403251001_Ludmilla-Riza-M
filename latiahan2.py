#==========================================================
# TUGAS HANDS_ON MODUL 1
#STUDI KASUS:sistem Barang kantin(bebasis File.txt)
#
#Nama:Ludmilla Riza Maharuni
#NIM:J0403251001
#Kelas:B2
#=============================================================
#-----------------------
#konstanta nama file
#--------------------------

#-------------------------
#membaca data dari file
#-----------------------
nama_file = "stok_barang2txt.txt" #menyimpan nama file yang akan dibaca

#-----------------------------
#Fungsi: membaca data dari file
#-----------------------------
def baca_data(nama_file):
    data_dict = {} #membuat wadah kosong
    with open(nama_file, "r", encoding="utf-8") as file: #membuaka file dalam mode baca(read).with memastikan file tertutup otomatis
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue
            parts = baris.split(",")
            if len(parts) != 3: #jika satu baris tidak memiliki 3 bagian data, baris
                continue
            nomor, nama_barang, stok_str = parts
            try:
                stok = int(stok_str)
            except ValueError:
                continue
            data_dict[nomor] = {"nama_barang": nama_barang, "stok": stok} #data disimpan dalam dict_dict dengan format 
    return data_dict
#-----------------------------------
#fungsi menempilkan semua data
#------------------------------------
def tampilkan_data(data_dict):
    if not data_dict:
        print("data kosong")
        return
    print("==== Daftar Barang ====")
    print(f"{'Nomor':<10}|{'Nama':<20}|{'Stok':>5}")
    print("-" * 40)
    for nomor in sorted(data_dict):
        nama_barang = data_dict[nomor]["nama_barang"]
        stok = data_dict[nomor]["stok"]
        print(f"{nomor:<10}|{nama_barang:<20}|{stok:>5}")
#------------------------------------
#cari barang berdasarkan kode
#--------------------------------------
def cari_data(data_dict, nomor_cari):
    if nomor_cari in data_dict:
        nama_barang = data_dict[nomor_cari]["nama_barang"]
        stok = data_dict[nomor_cari]["stok"]
        print("\n====== data barang ditemukan =======")
        print(f"Nomor dicari: {nomor_cari}")
        print(f"Nama barang: {nama_barang}")
        print(f"Stok: {stok}")
    else:
        print("\ndata tidak ditemukan")
#---------------------------
#Tambahkan barang baru
#-------------------------------
def tambah_barang(data_dict):
    nama_barang = input("masukkan nama barang baru: ").strip()
    if not nama_barang:
        print("nama barang tidak boleh kosong")
        return
    
    try: #stok disini harus berupa angka
        stok = int(input("masukkan stok barang: ").strip())
    except ValueError:
        print("stok harus berupa angka. Tambah barang dibatalkan")
        return
    
    if stok < 0: #tidak ada jumlah barang yang negatif
        print("stok tidak boleh negatif. Tambah barang dibatalkan")
        return
#---------------------------------------------- 
# Cari nomor berikutnya dari data yang ada
#----------------------------------------------
    nomor_terakhir = 0
    for nomor in data_dict.keys():
        # Extract nomor dari format "BRG001", "BRG002", dst
        if nomor.startswith("BRG"):
            try:
                num = int(nomor[3:])
                if num > nomor_terakhir:
                    nomor_terakhir = num
            except ValueError:
                pass
    
    nomor_baru = f"BRG{nomor_terakhir + 1:03d}"
    data_dict[nomor_baru] = {"nama_barang": nama_barang, "stok": stok}
    print(f"barang berhasil ditambahkan: {nomor_baru}, {nama_barang}, {stok}")

#------------------------------
#tambahkan barang baru
#----------------------------
def update_stok(data_dict):
    nomor = input('masukkan nomor barang yang akan di update stoknya: ').strip()
    if nomor not in data_dict:
        print('nomor tidak ditemukan, update dibatalkan')
        return
    try:
        stok_baru = int(input("masukkan stok baru: ").strip())
    except ValueError:
        print("stok harus berupa angka. Update dibatalkan")
        return
    if stok_baru < 0:
        print('stok tidak boleh negatif. Update dibatalkan')
        return
    stok_lama = data_dict[nomor]['stok']
    data_dict[nomor]['stok'] = stok_baru
    print(f"update berhasil. stok {nomor} berubah dari {stok_lama} menjadi {stok_baru}")
#----------------------------
#tambahkan stok barang
#-------------------------------
"""
mengubah stok barang(tambah atau kurangi)
stok tidak boleh menjadi negatif
"""
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nomor in sorted(data_dict.keys()):
            nama_barang = data_dict[nomor]["nama_barang"]
            stok = data_dict[nomor]['stok']
            file.write(f"{nomor},{nama_barang},{stok}\n")
    print('data berhasil di simpan ke file')
#--------------------------------------------
#program utama
#--------------------------------------------
def main():
    buka_data = baca_data(nama_file)
    print('jumlah data terbaca', len(buka_data))
    while True:
        print("\n======== menu utama =========")
        print("1. tampilkan data barang")
        print("2. cari data berdasarkan nomor")
        print("3. update stok barang")
        print("4. simpan perubahan data ke file")
        print("5. tambahkan barang")
        print("0. keluar program")
        pilihan = input('masukkan pilihan menu: ').strip()
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            nomor_cari = input('masukkan nomor yang dicari: ').strip()
            cari_data(buka_data, nomor_cari)
        elif pilihan == "3":
            update_stok(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "5":
            tambah_barang(buka_data)
        elif pilihan == "0":
            break
        else:
            print('pilihan tidak valid')

if __name__ == "__main__":
    main()
