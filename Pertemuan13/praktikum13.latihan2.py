# Nama  : Ludmilla Riza Maharuni
# NIM   :  J0403251001
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree

# ========================================================== 
# Implementasi Sederhana Algoritma Kruskal 
# ========================================================== 
# Daftar edge: (bobot, node1, node2) 
edges = [ 
(1, 'C', 'D'), 
(2, 'A', 'C'), 
(3, 'B', 'D'), 
(4, 'A', 'B'), 
(5, 'A', 'D') 
] 
# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 
mst = [] 
total_weight = 0 
connected = set() 
for weight, u, v in edges: 
# Memilih edge yang tidak membentuk cycle sederhana if u not in connected or v not in connected: 
    mst.append((u, v, weight)) 
    total_weight += weight 
    connected.add(u) 
    connected.add(v) 
    print("Minimum Spanning Tree:") 
    for edge in mst: 
        print(edge) 
        print("Total bobot =", total_weight) 

# Jawaban Analisis: 
# 1. Edge mana yang dipilih pertama kali? Edge (C,D) dengan bobot 1 dipilih pertama kali
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
#Karena algoritma Kruskal menggunakan strategi Greedy:
"""
Tujuan MST adalah meminimalkan total bobot dari semua edge yang dipilih.

Dengan memilih edge berbobot paling kecil terlebih dahulu, kita memastikan bahwa pada setiap langkah, kita mengambil keputusan lokal yang optimal.

Strategi ini terbukti (secara teoritis) menghasilkan solusi global optimal untuk MST.
"""
# 3. Berapa total bobot MST yang dihasilkan?
"""
- Total bobot = 6

Perhitungan:
- Edge C-D bobot 1
- Edge A-C bobot 2
- Edge B-D bobot 3
Total = 1 + 2 + 3 = 6
"""
# 4. Mengapa edge tertentu tidak dipilih?
"""
Edge yang tidak dipilih adalah:
= A-B (bobot 4) -> saat digabungkan A-C-D-B akan membentuk cycle
= A-D (bobot 5) ->  saat node A dan D sudah terhubung melalaui jalur A-C-D akan membentuk cycle
prinsip Edge yang akan memebentuk cycle tidak boleh ditambahkan ke MST
"""