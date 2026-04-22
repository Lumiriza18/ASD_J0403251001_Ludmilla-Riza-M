#==========================================
#Latihan 4:  membuat BST yang tidak seimbang
#NIM: J0403251001
#Nama: Ludmilla Riza Maharuni
#==========================================

#class Node untuk menyimpan data BST
class Node: 
    def __init__(self, data):  #-> Node ini menyimpan angkanya(data), dan
                                # memiliki dua slot kosong (left dan right) untuk 
                                # di hubungkan ke angka yang lain yeng lebih kecil atau lebih besar
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 

# Fungsi insert untuk BST 
def insert(root, data): #fungsi ini berfungsi menaruh angka ke posisi yang benar dengan aturan baku
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 

    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 

    return root 

# Fungsi preorder untuk melihat bentuk tree 
def preorder(root):  #untuk membaca tree dengan urutan
                        #cetak node saat ini -> kunjungi kiri -> kunjungi kanan
    if root is not None:  #cek apakah node saat ini tidak kosong
        print(root.data, end=" ") #cetak data pada node saat ini
        preorder(root.left)  #rekursif ke subtree kiri
        preorder(root.right) #rekursif ke subtree kanan

# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"):  #fungsi ini untuk menampilkan struktur tree dengan indentasi sesuai levelnya
    if root is not None:  #cek node kosong atau tidak
        print("   " * level + f"{posisi}: {root.data}") #cetak posisi dan data dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") #rekursif ke subtree kiri dengan level bertambah 1 dan posisi "L"
        tampil_struktur(root.right, level + 1, "R")#rekursif ke subtree kanan dengan level bertambah 1 dan posisi "R"

# ----------------------------- 
# Program utama 
# ----------------------------- 
root = None  #mulai dengan tree kosong
# Data dimasukkan berurutan naik 
data_list = [10, 20, 30] #data dimasukkan secara berurutan  naik, sehingga membantuk tree yang tidak seimbang
for data in data_list:  #memasukkan data ke dalam tree dengan fungsi insert
    root = insert(root, data)  #memanggil fungsi insert untuk setiap data dalam fungsi data_list
print("Preorder BST:")  #menmapilkan preorder traversal dari tree
preorder(root)  #menampilkan preorder tranversal dari tree
print("\n\nStruktur BST:")  #menampilkan struktur tree dengan fungsi tampilkan_struktur
tampil_struktur(root) 
