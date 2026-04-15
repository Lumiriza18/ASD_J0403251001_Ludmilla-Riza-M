#================================
# materi 1 : membuat node 
#================================

# class node digunnakna untuk dasar dati tree

from xml.dom import Node
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
#membuat root
root= Node("A")
#menampilkan isi node
print("data pada root", root.data)
print("data child kiri root", root.left)
print("data child kanan root", root.right)

#pembahasan:-------------------------------
"""
Bagian class Node adalah cetakan untuk membuat kotak penyimpan data
yang memiliki dua cabang penghubung (kiri dan kanan). Menggunakan cetakan tersebut, 
program membuat kotak pertama (disebut root) dan mengisinya dengan huruf "A". 
Karena root ini baru dibuat dan belum disambungkan dengan kotak anak apa pun, maka saat dicetak, 
cabang kiri dan kanannya masih berstatus None alias kosong.
"""
