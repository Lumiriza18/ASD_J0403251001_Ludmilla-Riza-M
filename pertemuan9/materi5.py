

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat traversal posterder : left -> right-> root
def  posterorder(node):
    if node is not None:
        posterorder(node.left)
        posterorder(node.right)
        print(node.data, end=" ")


#membuat Tree
root= Node("A")

#membuat child level 1
root.left=Node("B")
root.right=Node("C")

#membuat child level 2
root.left.left=Node("D")
root.left.right=Node("E")

print("data pada root", root.data)
print(" hasil postorder transversal:")
posterorder(root)

"""
1.Program mencari ujung paling kiri bawah, lalu mencetak D.

2.Pindah ke saudaranya di sebelah kanan, lalu mencetak E.

3. Karena kedua anaknya (D dan E) sudah dicetak, program naik dan mencetak induknya, yaitu B.

4. Seluruh bagian kiri Tree sudah beres. Program pindah ke cabang kanan dari akar utama, lalu mencetak C.

5.Karena semua cabang kiri dan kanan sudah selesai, terakhir program naik ke puncak dan mencetak akar utamanya, yaitu A.
"""