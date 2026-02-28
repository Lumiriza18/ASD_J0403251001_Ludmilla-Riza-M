#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas:P2
#================================================

#===============================================
# Tugas : membuat program  sistem antrian pelanggan pada sebuah bengkel motor
#================================================



class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None # Pointer ke node selanjutnya

class QueueBengkel:
    def __init__(self):
        # Inisialisasi antrian kosong
        self.front = None # Menunjuk pelanggan terdepan
        self.rear = None  # Menunjuk pelanggan terakhir

    def enqueue(self, no, nama, servis):
        # Membuat node baru untuk pelanggan
        baru = Node(no, nama, servis)
        
        # Jika antrian kosong, front dan rear menunjuk ke node baru
        if self.rear is None:
            self.front = self.rear = baru
            print(f"\n[Berhasil] Pelanggan {nama} ditambahkan ke antrian.")
            return
        
        # Jika tidak kosong, tambahkan di belakang dan geser rear
        self.rear.next = baru
        self.rear = baru
        print(f"\n[Berhasil] Pelanggan {nama} ditambahkan ke antrian.")

    def dequeue(self):
        # Cek jika antrian kosong
        if self.front is None:
            print("\n[Peringatan] Antrian kosong! Tidak ada pelanggan untuk dilayani.")
            return
        
        # Simpan data pelanggan yang akan dihapus (paling depan)
        temp = self.front
        print(f"\n[Melayani] Melayani pelanggan No. {temp.no} atas nama {temp.nama} ({temp.servis}).")
        
        # Geser front ke node selanjutnya (FIFO)
        self.front = self.front.next
        
        # Jika setelah dihapus antrian jadi kosong, rear juga harus None
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        # Cek jika antrian kosong
        if self.front is None:
            print("\n[Info] Antrian saat ini masih kosong.")
            return
        
        print("\n--- DAFTAR ANTRIAN SAAT INI ---")
        current = self.front
        i = 1
        # Traversal (penelusuran) dari front sampai ujung (None)
        while current is not None:
            print(f"{i}. No: {current.no} | Nama: {current.nama} | Servis: {current.servis}")
            current = current.next
            i += 1
        print("-------------------------------")

def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel === ")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama       : ")
            servis = input("Servis     : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Keluar dari sistem. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid")

# Menjalankan program utama
if __name__ == "__main__":
    main()
