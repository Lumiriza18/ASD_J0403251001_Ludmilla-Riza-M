
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
#membuat Tree
root= Node("A")

#membuat child level 1
root.left=Node("B")
root.right=Node("C")

#membuat child level 2
root.left.left=Node("D")
root.left.right=Node("E")
root.right.left= Node("F")
root.right.right= Node("G")

#menampilkan isi node
print("data pada root", root.data)
print("child kiri root", root.left.data)
print("child kanan root:",root.right.data)
print("child kiri dari B:", root.left.left.data)
print("child kanan dari B :",root.left.right.data)
print("child kiri dari C:",root.right.left.data)
print("child kanan dari c:",root.right.right.data)

#Lanjutkan (sudah)
#pembahasan
# level 0: A(pembuatan root/tree)

# level 1: root "A" kini menggandeng kotak "B" di cabang kirinya (root.left) 
# dan kotak "C" di cabang kanannya (root.right).

#Level 2 : kotak B dan C sekarang memiliki anak/ cucu 
# yaitu dari kiri-kannan "B"diiisi oleh "D" dan "E"
# sedangkan C disisi cabang kiri dan kanan  yang diisi 
#F dan G