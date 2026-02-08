#====================================================
#peratikum 1: konsep ADT dan file Handing
#Latihan dssar 1A: membaca seluruh isi file
#===================================================
#membuat file dengan mode read("r")
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    isi_file=file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)
print("===========hasill read============")
print("tipe data:", type(isi_file))
print("jumlah karakter",len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)

#membuka file per-baris
print("======= file per-baris =======")
jumlah_baris=0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris=jumlah_baris + 1
        baris=baris.strip() #menghapus spasi
        print("baris ke-", jumlah_baris)
        print("isinya:",baris)

print('=========================================')
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris=baris.strip() 
        nim,nama,nilai= baris.split(",")
        print("nim:",nim , "|nama:",nama,"|nilai:", nilai)

#peratikum 1: konsep ADT dan file Handing
#Latihan dssar 1A: membaca seluruh isi file
print("===============================")
data_list=[]
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris=baris.strip()
        nim,nama,nilai= baris.split(",")
        #simpan sebagai list"[nim,nama,nilai]
        data_list.append([nim,nama,int(nilai)])

print("===============data mahasiswa dalam list=============")
print(data_list)
print()
print("=================jumlah record dalam list============")
print("jumlah record", len(data_list))
print()
print("==========menampilakan data record tertentu=========")
print("contoh record pertama:", data_list[0])
print()

#peratikum 1: konsep ADT dan file Handing
#Latihan dssar 4A: membaca file dan menyimpan ke dictionary
data_dict={}#buat variabel untuk dictionary
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris=baris.strip()
        nim,nama,nilai= baris.split(",")
        #simpan data mahasiswa ke dictionary dengan nim
    data_dict[nim]={ #key
        "nama": nama, #value
        "nilai":int(nilai)#value
    }
print("=======data mahasiswa dalam dictonary========")
print(data_dict)






 