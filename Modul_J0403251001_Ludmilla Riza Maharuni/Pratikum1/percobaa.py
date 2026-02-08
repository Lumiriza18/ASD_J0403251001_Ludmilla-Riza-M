# ...existing code...
nama_file = "data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue
            parts = baris.split(",")
            if len(parts) != 3:
                continue
            nim, nama, nilai_str = parts
            try:
                nilai = int(nilai_str)
            except ValueError:
                continue
            data_dict[nim] = {"nama": nama, "nilai": nilai}
    return data_dict

def tampilkan_data(data_dict):
    if not data_dict:
        print("data kosong")
        return
    print("==== Daftar Mahasiswa ====")
    print(f"{'NIM':<10}|{'Nama':<12}|{'Nilai':>5}")
    print("-" * 32)
    for nim in sorted(data_dict):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10}|{nama:<12}|{nilai:>5}")

def car_data(data_dict, nim_cari):
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        print("\n====== data mahasiswa ditemukan =======")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("\ndata tidak ditemukan")

def update_nilai(data_dict):
    nim = input('masukkan nim mahasiswa yang akan di update nilainya: ').strip()
    if nim not in data_dict:
        print('nim tidak ditemukan, update dibatalkan')
        return
    try:
        nilai_baru = int(input("masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("nilai harus berupa angka. Update dibatalkan")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print('nilai harus antara 0 sampai 100. Update dibatalkan')
        return
    nilai_lama = data_dict[nim]['nilai']
    data_dict[nim]['nilai'] = nilai_baru
    print(f"update berhasil. nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")
    print('data berhasil di simpan ke file')

def main():
    buka_data = baca_data_mahasiswa(nama_file)
    print('jumlah data terbaca', len(buka_data))
    while True:
        print("\n======== menu utama =========")
        print("1. tampilkan data mahasiswa")
        print("2. cari data berdasarkan nim")
        print("3. update nilai mahasiswa")
        print("4. simpan perubahan data ke file")
        print("0. keluar program")
        pilihan = input('masukkan pilihan menu: ').strip()
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            nim_cari = input('masukkan NIM yang dicari: ').strip()
            car_data(buka_data, nim_cari)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            break
        else:
            print('pilihan tidak valid')

if __name__ == "__main__":
    main()
# ...existing code...