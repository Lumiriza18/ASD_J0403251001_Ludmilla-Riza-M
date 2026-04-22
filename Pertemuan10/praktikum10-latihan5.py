# ========================================================== 
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang 
# ==========================================================

# Class Node 
class Node: #class Node untuk menyimpan data BST
    def __init__(self, data): #-> Node ini menyimpan angkanya(data), dan
                                # memiliki dua slot kosong (left dan right) untuk
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None# child kanan

# Fungsi preorder untuk melihat isi tree 
def preorder(root): #untuk membaca tree dengan urutan
                    #cetak node saat ini -> kunjungi kiri -> kunjungi kanan
    if root is not None: #cek apakah node saat ini tidak kosong
        print(root.data, end=" ") #cetak data pada node saat ini
        preorder(root.left) #rekursif ke subtree kiri
        preorder(root.right) #rekursif ke subtree kanan

# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): #fungsi ini untuk menampilkan struktur tree dengan indentasi sesuai levelnya
    if root is not None: #cek node kosong atau tidak
        print("   " * level + f"{posisi}: {root.data}") #cetak posisi dan data dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L") #rekursif ke subtree kiri dengan level bertambah 1 dan posisi "L"
        tampil_struktur(root.right, level + 1, "R") #rekursif ke subtree kanan dengan level bertambah 1 dan posisi "R"

# Fungsi rotasi kiri 
def rotate_left(x): #fungsi ini untuk melakukan rotasi kiri pada node x, yang merupakan root dari subtree yang tidak seimbang
    # x adalah root lama 
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara 

    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2 

    # y menjadi root baru 
    return y

# ----------------------------- 
# Program utama 
# ----------------------------- 
# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
root = Node(10)  # membuat node root dengan nilai 10
root.right = Node(20) # membuat node dengan nilai 20 sebagai child kanan dari root
root.right.right = Node(30) # membuat node dengan nilai 30 sebagai child kanan dari node 20, sehingga membentuk tree yang tidak seimbang

print("Preorder sebelum rotasi kiri:") 
preorder(root) #menampilkan preorder traversal dari tree sebelum rotasi kiri
print("\n\nStruktur sebelum rotasi kiri:") 
tampil_struktur(root) 

# Melakukan rotasi kiri pada root 
root = rotate_left(root) 
print("\nPreorder sesudah rotasi kiri:") 
preorder(root) 
print("\n\nStruktur sesudah rotasi kiri:") 
tampil_struktur(root)