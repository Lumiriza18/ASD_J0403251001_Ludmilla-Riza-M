# ==========================================================
# PROGRAM MST JARINGAN KABEL KAMPUS
# Nama  : Ludmilla Riza Maharuni
# NIM   : J0403251001
# Kelas : B2
# ==========================================================
# Kasus: Mencari biaya minimum pemasangan kabel antar gedung
# ==========================================================

# ---------- 1. REPRESENTASI WEIGHTED GRAPH ----------
# Data hubungan antar gedung: (bobot, gedung1, gedung2)
# Bobot = biaya pemasangan kabel

edges = [
    (4, 'A', 'B'),   # Gedung A ke B biaya 4
    (2, 'A', 'C'),   # Gedung A ke C biaya 2
    (3, 'B', 'D'),   # Gedung B ke D biaya 3
    (1, 'C', 'D'),   # Gedung C ke D biaya 1
    (5, 'A', 'D')    # Gedung A ke D biaya 5
]

# ---------- 2. FUNGSI FIND (UNTUK DETECT CYCLE) ----------
# Mencari root/akar dari sebuah gedung (untuk Union-Find)
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # Path compression
    return parent[node]

# ---------- 3. FUNGSI UNION (MENGGABUNGKAN 2 HIMPUNAN) ----------
def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    
    # Union by rank (optimasi agar tree tetap pendek)
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

# ---------- 4. ALGORITMA KRUSKAL ----------
def kruskal(edges):
    # Step 1: Urutkan edge dari biaya terkecil ke terbesar
    edges.sort()
    
    # Inisialisasi parent (setiap gedung adalah parent dari dirinya sendiri)
    gedung = set()
    for _, u, v in edges:
        gedung.add(u)
        gedung.add(v)
    
    parent = {g: g for g in gedung}
    rank = {g: 0 for g in gedung}
    
    # Step 2: Pilih edge terkecil yang tidak membentuk cycle
    mst = []           # Menyimpan edge yang terpilih
    total_biaya = 0    # Menyimpan total biaya
    
    for biaya, u, v in edges:
        # Cek apakah u dan v sudah terhubung (cycle?)
        if find(parent, u) != find(parent, v):
            # Jika belum terhubung, ambil edge ini
            union(parent, rank, u, v)
            mst.append((u, v, biaya))
            total_biaya += biaya
    
    return mst, total_biaya

# ---------- 5. EKSEKUSI & OUTPUT ----------
print("=" * 50)
print("PROGRAM MST JARINGAN KABEL KAMPUS")
print("=" * 50)

print("\nData hubungan antar gedung (biaya):")
for biaya, u, v in edges:
    print(f"  {u} --- {v} = {biaya}")

# Jalankan algoritma Kruskal
mst, total_biaya = kruskal(edges)

print("\n" + "=" * 50)
print("HASIL JARINGAN KABEL OPTIMAL (MST):")
print("=" * 50)

print("\nEdge yang dipilih:")
for u, v, biaya in mst:
    print(f"  {u} --- {v} : biaya = {biaya}")

print("\n" + "-" * 30)
print(f"TOTAL BIAYA MINIMUM = {total_biaya}")
print("-" * 30)

# Verifikasi manual
print("\nVerifikasi:")
print("  Edge C-D (1) + A-C (2) + B-D (3) = 6")
print("  Semua gedung terhubung: A-C-D-B")

# Jawaban Analisis: 
# 1. Algoritma apa yang digunakan? Algoritma Kruskal
# 2. Edge mana saja yang dipilih?3 edge yang dipilih (karena jumlah gedung = 4, maka MST membutuhkan 3 edge)
# 3. Berapa total biaya minimum? Total biaya minimum = 6
# 4. Mengapa MST cocok digunakan pada kasus ini?
"""
- Mencari biaya pemasangan kabel paling murah
-Menghubungkan semua node dengan total bobot minimum
-Jaringan kabel tidak perlu jalur ganda (boros biaya)
-MST menjamin setiap gedung terakses tanpa ada yang terisolasi
"""