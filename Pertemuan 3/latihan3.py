#=============================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#latihan 3:Implementasikan	Pencarian	pada	node	tertentu	Double	Linked	List.
#==================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Menyimpan node terakhir untuk traversing mundur
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")
    
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

# Contoh Penggunaan
dll = DoublyLinkedList() 
dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)

print("List elements:")
dll.display_forward()

# Mencari elemen 9
element_to_search = input("masukkan elemen yangingin dicarai:")
if dll.search(element_to_search):
    print(f"Elemen {element_to_search} ditemukan dalam doubly linked list")
else:
    print(f"Elemen {element_to_search} tidak ditemukan dalam doubly linked list")
