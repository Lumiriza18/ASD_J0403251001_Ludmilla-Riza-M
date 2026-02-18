#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#================================================
#implementasi dasa : Queeue barbasis Linked list
#================================================

class node:
    def __init__(self,data):#konstruktor
        self.data= data #sebagai objek untuk menyimpan nilai/data
        self.next= None #pointer ke note berikutnya (awal=none)

#queeue dengan 2 pointer : front dan rear pokoknya depan belakang
class QueueLL:
    def __init__(self):
        self.front= None #node paling depan 
        self.rear=None #node paling belakang
        
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        #menambah data di belakang (rear)
        nodebaru=node(data) 
        # jika queue kosong, front dan rear menunjukkan 

        if self.is_empty():
            self.front=nodebaru
            self.rear=nodebaru
            return
        #jikaqueue tidak kosong:
        #rear lama menuju ke dode baru
        self.rear.next=nodebaru #kalo ada next itu berarticuma nunjuk saja 
        #rear pindah ke node baru
        self.rear=nodebaru
    
    def dequeue(self):
        #menghapus data dari depan

        # 1)lihat   data yang paling depan  ke next
        data_terhapus = self.front.data

        #2) geser front kenode berikutnya 
        self.front=self.front.next

        #3) Jika setelah  geser front menjadi none, maka queue kosong
        # rear juga harus jadi none
        if self.front is None:
            self.rear=None

        return data_terhapus



    def tampilkan(self):
        #menampilkan isi queue
        current= self.front
        print("front", end="->")
        while current is not None:
            print(current.data, end="->")
            current= current.next
        print("Rear")
        #print("None-rear di node trakhir")

#instantiasi objeck class QueueLL
q=QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()


