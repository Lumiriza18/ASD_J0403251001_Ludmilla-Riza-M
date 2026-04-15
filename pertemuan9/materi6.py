#==============================
# Struktur organisasi perusahaan
#===============================



class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

def  preorder(node):
    if node is not None:
        print(node.data, end=" ") #root
        preorder(node.left) #left
        preorder(node.right) #right

#membuat tree struktur organisasi
root= Node("direktur")

#child lavel 1
root.left=Node("manager A")
root.right=Node("manager B")

#child level 2
root.left.left=Node("staff1")
root.left.right=Node("staff2")
root.right.right=Node("staff3")


print("struktur organisasi  (preorder):")
preorder(root)

#penjelasan
"""
1.Puncak Pohon (root): Posisi paling atas (akar) tidak lagi diisi huruf, melainkan diisi oleh Direktur.

2.Cabang Level 1: Direktur memiliki dua bawahan langsung, yaitu Manager A di cabang kiri dan Manager B di cabang kanan.

3.Cabang Level 2: * Manager A memiliki dua bawahan, yaitu Staff 1 (kiri) dan Staff 2 (kanan).

4.Manager B hanya diberi satu bawahan, yaitu Staff 3 di posisi kanan (root.right.right).

5. Cara Membaca (Preorder): Kamu menggunakan cara baca Preorder (Atasan -> Bawahan Kiri -> Bawahan Kanan). 
Artinya, program akan mengabsen atasan paling tinggi, 
lalu menelusuri seluruh tim Manager A sampai habis, barulah pindah menelusuri tim Manager B.
"""