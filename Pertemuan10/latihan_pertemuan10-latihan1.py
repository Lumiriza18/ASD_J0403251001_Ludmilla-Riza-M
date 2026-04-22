#-------------------------------------------------
# Latihan : BST
#NIM: J0403251001
#Nama: Ludmilla Riza Maharuni
#------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai angkanya
        self.left = None # menunjukkan ke cabang kiri(untuk nilai yang lebih kecil)
        self.right = None # menunjukkan ke cabang kanan(untuk nilai yang lebih besar)

def insert(root,data):
    if root is None: #jika root kosong, buat node baru dengan data yang diberikan
        return Node(data) 
    
    if data < root.data: ##jika angka baru lebih kecil dari angka saat ini,arahkan proses ke cabang kiri
        root.left =insert(root.left,data)
    elif data >root.data: ##jika angka baru lebih besar dari angka saat ini,arahkan proses ke cabang kanan
        root.right =insert(root.right,data)
    
    return root #mengembalikan root yang sudah di update dengan node baru yang di masukkan
# mengisi data BST
root=None #mulai dengan tree kosong
data_list =[50,30,70,20,40,50,80] #data yang akan dimasukkan ke dalam BST

for data in data_list:#memasukkan data ke dalam BST dengan memanggil fungsi insert untuk setiap data dalam data_list
    root=insert(root,data) #memanggil fungsi insert untuk setiap data dalam data_list dan memperbarui root dengan hasilnya
print("data BST berhasil di buat")#menampilkan pesan bahwa data BST sudah berhasil dibuat

#==========================================
#Latihan 2 :Traversal Inorder
#NIM: J0403251001
#Nama: Ludmilla Riza Maharuni
#==========================================

#alur inorder gimana itu......
def inorder(root): #fungsi ini untuk melakukan traversal inorder pada BST, yaitu mengunjungi node dalam urutan: kiri -> node saat ini -> kanan
    if root is not None:#cek apakah node saat ini tidak kosong
        inorder(root.left) #rekursif ke subtree kiri terlebih dahulu
        print(root.data,end=" ")#cetak data pada node saat ini setelah mengunjungi subtree kiri
        inorder(root.right)#rekursif ke subtree kanan setelah mencetak data pada node saat ini
print("hasil inorder:")#menampilkan hasil traversal inorder dari BST dengan memanggil fungsi inorder pada root
inorder(root)#memanggil fungsi inorder pada root untuk memulai traversal inorder dari seluruh tree

#==========================================
#Latihan 3: Seaarch BTS
#NIM: J0403251001
#Nama: Ludmilla Riza Maharuni
#==========================================
def search(root,key): #fungsi ini untuk mencari apakah sebuah nilai (key) ada dalam BST yang dimulai dari root
    if root is None:#jika root kosong, berarti key tidak ditemukan dalam tree, jadi kembalikan False
        return False#jika key lebih kecil dari data pada node saat ini, lanjutkan pencarian di subtree kiri
        
    if key < root.data: #jika key lebih kecil dari data pada node saat ini, lanjutkan pencarian di subtree kiri
        return search(root.left,key)#jika key lebih besar dari data pada node saat ini, lanjutkan pencarian di subtree kanan
    elif key > root.data:#jika key lebih besar dari data pada node saat ini, lanjutkan pencarian di subtree kanan
        return search(root.right,key)#jika key sama dengan data pada node saat ini, berarti key ditemukan dalam tree, jadi kembalikan True
    else:#jika key sama dengan data pada node saat ini, berarti key ditemukan dalam tree, jadi kembalikan True
        return True

#uji pencariana
ke=40 #nilai yang akan dicari dalam BST
if search (root,ke): #jika fungsi search mengembalikan True, berarti data ditemukan dalam BST, jadi tampilkan pesan "data ditemukan"
    print("data ditemukan")
else: #jika fungsi search mengembalikan False, berarti data tidak ditemukan dalam BST, jadi tampilkan pesan "data tidak ditemukan"
    print("data tidak di temukan")
    