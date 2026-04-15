#=======================================
# Latihan 4
#=======================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi inorder: left -> root-> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data,end=" ")
        inorder(node.right)


#membuat Tree
root= Node("A")

#membuat child level 1
root.left=Node("B")
root.right=Node("C")

#membuat child level 2
root.left.left=Node("D")
root.left.right=Node("E")


print("data pada root", root.data)


#penjelasaa
"""
1.Program mulai di puncak, tetapi ia tidak mencetak A (Akar) terlebih dahulu, 
melainkan turun ke cabang kiri dan terus turun sampai mencapai D.
2. Setelah mencapai D, ia kembali ke node B dan mengecek cabang kanan, mencetak E.
3. Setelah selesai dengan node B, ia kembali ke node A dan mengecek cabang kanan, mencetak C.

"""