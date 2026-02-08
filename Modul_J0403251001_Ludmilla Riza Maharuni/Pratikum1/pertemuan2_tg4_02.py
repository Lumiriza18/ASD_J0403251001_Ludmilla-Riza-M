#====================================================
#peratikum 2: konsep ADT dan file hending(STUDI KASUS)
#Latihan dssar 1A: membuat fungsi load data
#===================================================
nama_file="data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict={} #ini sialisasi data
    with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
        for baris in file:
            baris=baris.strip()#menghilangkan karakter baris baru
            if not baris:
                continue
            parts=baris.split(",")
            if len(parts)!=3:
                continue
            nim,nama,nilai_str=parts
            try:
                nilai=int(nilai_str)
            except ValueError:
                data_dict[nim]={"nama":nama,"nilai":nilai}
        return data_dict

        #nilai_int=int(nilai_str)
        #nim,nama,nilai= baris.split(",") #pecah menjadi data ketika bertemu koma
        #simpan sebagai dict{key}"[nim,nama,nilai]
        #data_dict[nim]={
           # "nama":nama,
           # "nilai": int(nilai)
        
    return data_dict
#memanggil fungsi baca_data_mahasiswa
buka_data=baca_data_mahasiswa(nama_file)
print('jumlah data terbaca',len(buka_data))

#====================================================
#peratikum 2: konsep ADT dan file hending(STUDI KASUS)
#Latihan dssar 2: membuat fungsi menampilkan data
#===================================================



def tampilkan_data(data_dict):
    if len(data_dict)==0:
        print("data kosong")
        return
    
    #membuat header tabel
    print("==== Daftar Mahasiswa====")
    print(f"{'NIM': 10}|{'Nama':<12}|{'Nilai':>5}")#mengatur identasi biar kolom rapi
    print("-"*32)#menampilkan garis header
    '''
    untuk tampilan yang rapi,atur f-string formating
    {'NIM': <10} artinya:
    tampilkan nim <= rata kiri dengan lebar 10 karakter
    {'Nama:<12}
    tampilkan nama rata kiri, dengan lebar kolom12 karakter
    {nilsi:>5}
    tampilkan nilai >= rata kanan,lebar kolom 5 karakter
    '''

    for nim in sorted(data_dict):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim<10}|{nama:<12}|{nilai>5}")
#memanggil fungsi menampilkan data
tampilkan_data(buka_data)

#====================================================
#peratikum 2: konsep ADT dan file hending(STUDI KASUS)
#Latihan dssar 2: membuat fungsi menampilkan data
#===================================================
def car_data(data_dict, nim_cari):
    if nim_cari in data_dict:
        nama=data_dict[nim_cari]["nama"]
        nilai=data_dict[nim_cari]["nilai"]
        print("\n====== data mahasiswa ditemukan=======")
        print(f"NIM:{nim_cari}")
        print(f"Nama:{nama}")
        print(f"Nilai:{nilai}")
    else:
        print("\n data tidak di temukan")
        #memanggil fungsi mencari data

#====================================================
#peratikum 2: konsep ADT dan file hending(STUDI KASUS)
#Latihan dssar 4: membuat fungsi update nilai
#===================================================
def update_nilai(data_dict):
    #cari nim mahasiswa yang akan di update nilainya
    nim=input('masukkan nim mahasiswa yang akan di update nilainya')

    if nim not in data_dict:
        print('nim tidak ditemukkan,update dibatalkaan')
    try:
        nilai_baru=int(input("masukkan nilai baru (0-100):").strip())
    except ValueError:
        print("nilai harus antara 0 sampai 100.Update dibatalkan")
        return
    
    if nilai_baru< 0 or nilai_baru>100:
        print('nilai harus antara 0 sampai 100.update')
        nilai_lama=data_dict[nim]['nilai']
        data_dict[nim]['nama']=nilai_baru
        print(f" update berhasil.nilai{nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

update_nilai(buka_data)

#====================================================
#peratikum 2: konsep ADT dan file hending(STUDI KASUS)
#Latihan dssar 5: membuat fungsi menyimpan perubahan data ke file
#===================================================

def simpan_data(nama_file,data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama=data_dict[nim]["nama"]
            nilai=data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")
simpan_data(nama_file,buka_data)
print('data berhasil di simpan ke file')

#====================================================
#peratikum 2: konsep ADT dan file hending(STUDI KASUS)
#Latihan dssar 6: 
#===================================================
def main():
    #menjalankan fungsi 1 load data
    buka_data=baca_data_mahasiswa(nama_file)

while True:
    print("\n======== menu utama=========")
    print("1. tampilkan data mahasiswa")#fungsi no2
    print("2. cari data berdsarkan nim")#fungsi no3
    print("3 update nilai mahasiswa")#fungsi no4
    print("4. simpan perubahan data ke file")# fungsi no 5
    print("0. keluar program")

    pilihan=input('masukkan pilihan menu:')
    if pilihan =="1":
        tampilkan_data(buka_data)
    elif pilihan =="2":
        nim_cari=input("masukkan nim yang dicari").strip()
        car_data(buka_data,nim_cari)
    elif pilihan =="3":
        update_nilai(buka_data)
    elif pilihan =="4":
        simpan_data(nama_file,buka_data)
    elif pilihan =="0":
        break
    else:
        print('pilihan tidak valid)')

if __name__=="__main__":
   main()

