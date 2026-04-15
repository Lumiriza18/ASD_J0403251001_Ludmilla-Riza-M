class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#
def preorder(node):
    if node is not None:
        print(node.data,end=" ") #root
        preorder(node.left) #left
        preorder(node.right) #right

#membuat Tree
root= Node("A")

#membuat child level 1
root.left=Node("B")
root.right=Node("C")

#membuat child level 2
root.left.left=Node("D")
root.left.right=Node("E")

# menjalankan tranvesal preorder
print(" hasil preorder transversal:")
preorder(root)

#penjelasanya
#1.Program mulai di puncak, mencetak A (Akar).

#2. Ia turun ke cabang kiri, mencetak B, lalu turun lagi ke kiri dan mencetak D.

#3. Sisi kiri B sudah habis, jadi ia mengecek sisi kanan B dan mencetak E.

#4. Seluruh bagian kiri A (yaitu B, D, E) sudah selesai dibaca, jadi program akhirnya pindah ke cabang kanan A, dan mencetak C.

