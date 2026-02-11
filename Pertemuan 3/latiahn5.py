#======================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#Latihan	5:Tambahkan	metode	untuk	membalik	(reverse)	sebuah	single	linked	list	
#=============================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan data di akhir list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Metode untuk menampilkan data dengan format " -> "
    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        # Menggabungkan elemen dengan " -> "
        print(" -> ".join(elements))

    # METODE BARU: Membalikkan linked list tanpa membuat list baru
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # 1. Simpan gerbong selanjutnya
            current.next = prev       # 2. Balikkan pengait ke gerbong sebelumnya
            prev = current            # 3. Geser 'prev' maju ke gerbong saat ini
            current = next_node       # 4. Geser 'current' maju ke gerbong selanjutnya
            
        # Setelah perulangan selesai, 'prev' akan berada di gerbong paling ujung
        # Jadikan gerbong paling ujung tersebut sebagai kepala (head) yang baru
        self.head = prev

# ==========================================
# Contoh Penggunaan dan Tampilan Input/Output
# ==========================================

ll = LinkedList()

# Meminta input dari pengguna (Contoh: 1,2,3,4,5)
input_data = input("Masukkan elemen list (pisahkan dengan koma): ")

# Memecah input berdasarkan koma dan memasukkannya ke linked list
for item in input_data.split(','):
    ll.insert_at_end(item.strip())

# Menampilkan list sebelum dibalik
print("Linked sebelum dibalik: ", end="")
ll.display()

# Membalikkan list
ll.reverse()

# Menampilkan list setelah dibalik
print("Linked setelah dibalik: ", end="")
ll.display()