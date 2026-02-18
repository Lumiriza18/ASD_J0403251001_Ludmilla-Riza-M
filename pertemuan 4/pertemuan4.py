#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#================================================
#implementasi dasa :Node pada linked list
#================================================

#membuat class node(merupakan unit dasar dari linked list)
class node:
    def __init__(self,data):#konstruktor
        self.data= data #sebagai objek untuk menyimpan nilai/data
        self.next= None #pointer ke note berikutnya (awal=none)
# 1) mebuaat satu per satu 
node("A") #memanggil konstruktor dengan memanggil kelasnya 
nodeA=node("A")
nodeB=node("B")
nodeC=node("C")

#2) menghubungkan node: A-> B-> C->None
nodeA.next=nodeB #node B di simpan di next A / pariabel setelah A adalah node B
nodeB.next=nodeC

#3) menentukan node pertama (head)
head= nodeA

#4)traversal : dari head sampai none
current=head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current=current.next # pindah ke node berikutnya 

#===========================================================
#implementasi dasar: Linked list + insert list
#===========================================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head= None #awalnya kosong
        
    def insert_awal(self,data): #konsep push dalam stack
        #buat node baru
        node_baru=node(data) #panggil class node

        #2) node baru menujuk ke head lama
        node_baru.next=self.head

        #3) head pindah ke node baru
        self.head=node_baru

    def hapus_awal(self): #konsep pop dalam stack
        data_terhapus=self.head.data #peek itu melihat data paling depan/head/atas baru kita geser setelah head dan head yang lama hilang dalam stack
        #menggeserkan head ke node berikutnya
        self.head= self.head.next
        print("node yang dihapus :",data_terhapus)

    def tampilkan(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

print("==============list baru=================")
ll=LinkedList() #instantantiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()

