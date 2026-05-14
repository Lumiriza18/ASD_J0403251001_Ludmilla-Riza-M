# Nama  : Ludmilla Riza Maharuni
# NIM   : J0403251001
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree 

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid (menghubungkan semua node tanpa siklus)
# Node: A, B, C, D → spanning tree butuh 3 edge
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]  # Menghubungkan A-C-D-B, semua node terhubung

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

#
# Jawaban Analisis: 
# 1. Apa perbedaan graph awal dan spanning tree? 
# Graph awal:
"""
Memiliki 5 edge
Masih mengandung cycle (contoh: A-B_D_C_A)
Bisa tetap terhubung meskipun ada jalur redundan
Semua node: A, B, C, D
"""
#Spanning Tree
"""
Hanya memiliki 3 edge (karena jumlah node = 4, maka edge = n-1)
Tidak memiliki cycle
Tetap terhubung (connected) dengan jumlah edge minimal
Semua node: A, B, C, D juga (tetap mencakup semua node)
"""
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# karena
"""
Cycle membuat edge berlebih → Jika ada cycle, minimal satu edge bisa dihilangkan tanpa memutuskan koneksi antar node.
Definisi tree dalam teori graf adalah graf terhubung tanpa cycle.
Jika ada cycle, maka jumlah edge akan lebih dari n-1, sehingga bukan lagi tree (melainkan graf berbasis cycle).
"""
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 
"""
karena menghindari dari siklus perulangan
Graph awal bisa memiliki banyak edge (bisa saja edge > n-1).
Spanning tree hanya mengambil edge yang diperlukan untuk menghubungkan semua node tanpa cycle.
Rumus jumlah edge tree = n - 1 (dengan n = jumlah node).
Sementara graph awal bisa memiliki edge hingga n*(n-1)/2 (jika complete graph).
"""