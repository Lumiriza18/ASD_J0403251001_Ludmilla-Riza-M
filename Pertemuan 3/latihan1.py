#======================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#Implementasikan fungsi untuk menghapus node dengan nilai tertentu
#=============================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


ll = LinkedList() 

elemen = input("Masukkan elemen (pisahkan dengan koma): ")
for data in elemen.split(","):
    if data.strip():
        ll.insert_at_end(int(data))

print("Linked List awal:")
ll.display()

hapus = int(input("Masukkan elemen yang ingin dihapus: "))
ll.delete_node(hapus)

print("Linked List setelah dihapus:")
ll.display()