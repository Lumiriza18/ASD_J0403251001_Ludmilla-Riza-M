#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#studi kasus: Sistem Antrian Layanan Akademik
#implementasi queue =>
#Enqueue : memindahkan Pointer rear(nambah data dari belakang)
#dequeue : memindahkan pointer front/head(menghapus data dari depan)
#front -> A -> B -> C ->Rear
#================================================

# 1) mendefinisikan node (unit dasar linked list)
class Node:
    def _init_(self,nim,nama):
        self.nim =nim   #menyimpan NIM mahasiswa
        self.nama= nama#menyimpan Nama Mahasiswa
        self.next= None  #menyimpan ke node berikutnya

#2) mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front =None
        self.rear =None

    def is_empty(self):
        #ketika queue kosong maka front=rear=none
        return self.front is None
    
#menambahkan data baru ke bagian belakang(rear)
    def enqueue(self,nim,nama):
        nodebaru = Node(nim,nama)
        #jika data baru masuk dari queue yang kosong makadata baru= front= rear
        if self.is_empty():
            self.front= nodebaru
            self.rear =nodebaru
            return

        #jika queue tidak kosong, maka data-baru diletakkan setelah rear kemudian di jadikan sebagai rear  
        self.rear.next = nodebaru
        self.rear= nodebaru
    #menghapus data paling depan (memberikan layanan akademik )
    def dequeue(self):

        if self.is_empty():
            print("antrian kosong.tidak ada mahasiswA yang dilayani")
        #lihat, data bagian front, simpan di variabel data yang akan dihapus (dilayanin)
        node_dilayani=self.front

        #geser pointer fornt ke next front
        self.front=self.front.next

        #jika  front mmenjadi none(data antrian )
        if self.front is None:
            self.rear=None

        return node_dilayani
    
    def tampilkan(self):
        print("daftar antrian.mahasiswa (font-> rear)")
        current = self.front
        no=1
        while current is not None:
            print(f"{no}.{current.nim}.{current.nama}")
            no +=1
    
#program menu
def main():
    #instansiasi queue
    q=queueAkademik

    while True:
        print("===========sistem antrian akademik==========")
        print("1. tambahkan mahasiswa")
        print("2. layani mahasiswa")
        print("3. lihat antrian")
        print("4.keluar")

        pilihan= input("pilih menu (1-4):").strip()

        if pilihan== "1":
            nim= input("maukkan NIM:").strip()
            nama= input("masukan nama:")

            q.enqueue(nim,nama)
            print("masukkan baehasil ditambahkan ke antrian")

        elif pilihan =="2":
            dilayani=q.dequeue()
            print(f"mahasiswa dilayanin:",{dilayani.nim},{dilayani.nama})

        elif pilihan =="3":
            q.tampilkan()
        
        elif pilihan=="4":
            print("program selesai.terima kasih")
        
#elif:
#print("pilihantidak valid, pilih menu 1-4")
    
if __name__=="_main_":
            main()





