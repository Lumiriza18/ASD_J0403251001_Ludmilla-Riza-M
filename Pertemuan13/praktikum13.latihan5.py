# ==========================================================
# PROGRAM MST - JARINGAN JALAN ANTAR KOTA
# Nama  : Ludmilla Riza Maharuni
# NIM   : J0403251001
# Kelas : B2
# ==========================================================
# Kasus: Mencari jalur jalan terpendek yang menghubungkan semua kota
# Algoritma: Kruskal
# ==========================================================

# ---------- 1. REPRESENTASI WEIGHTED GRAPH ----------
# Data jalan antar kota: (jarak, kota1, kota2)
# Jarak dalam satuan yang sama (misal: puluhan km)

edges = [
    (5, 'Bogor', 'Jakarta'),     # Bogor - Jakarta = 5
    (2, 'Bogor', 'Depok'),       # Bogor - Depok = 2
    (3, 'Depok', 'Jakarta'),     # Depok - Jakarta = 3
    (6, 'Jakarta', 'Bandung'),   # Jakarta - Bandung = 6
    (4, 'Depok', 'Bandung')      # Depok - Bandung = 4
]

# ---------- 2. FUNGSI FIND (UNTUK DETECT CYCLE) ----------
# Mencari root/akar dari sebuah kota (untuk Union-Find)
def find(parent, kota):
    # Jika kota bukan parent dari dirinya sendiri, cari parent-nya
    if parent[kota] != kota:
        # Path compression: buat parent langsung ke root
        parent[kota] = find(parent, parent[kota])
    return parent[kota]

# ---------- 3. FUNGSI UNION (MENGGABUNGKAN 2 HIMPUNAN) ----------
def union(parent, rank, kota1, kota2):
    # Cari root dari kedua kota
    root1 = find(parent, kota1)
    root2 = find(parent, kota2)
    
    # Union by rank: gabungkan tree yang lebih kecil ke yang lebih besar
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        # Jika sama, jadikan salah satu sebagai root dan naikkan rank-nya
        parent[root2] = root1
        rank[root1] += 1

# ---------- 4. ALGORITMA KRUSKAL ----------
def kruskal(edges):
    # Step 1: Urutkan edge dari jarak terkecil ke terbesar
    edges.sort()
    
    # Kumpulkan semua kota unik dari data edge
    kota_set = set()
    for _, kota1, kota2 in edges:
        kota_set.add(kota1)
        kota_set.add(kota2)
    
    # Inisialisasi parent dan rank untuk Union-Find
    # Awalnya setiap kota adalah parent dari dirinya sendiri
    parent = {kota: kota for kota in kota_set}
    rank = {kota: 0 for kota in kota_set}
    
    # Step 2: Pilih edge terkecil yang tidak membentuk cycle
    mst = []          # Menyimpan edge yang terpilih
    total_jarak = 0   # Menyimpan total jarak minimum
    
    print("\nProses Pemilihan Edge:")
    print("=" * 40)
    
    for jarak, kota1, kota2 in edges:
        # Cek apakah kota1 dan kota2 sudah dalam satu grup (cycle?)
        if find(parent, kota1) != find(parent, kota2):
            # Jika belum terhubung, edge ini AMAN untuk diambil
            union(parent, rank, kota1, kota2)
            mst.append((kota1, kota2, jarak))
            total_jarak += jarak
            print(f"✓ Dipilih : {kota1} - {kota2} (jarak = {jarak})")
        else:
            # Jika sudah terhubung, edge ini akan membuat CYCLE (LEWATI)
            print(f"✗ Dilewati: {kota1} - {kota2} (jarak = {jarak}) [akan membuat cycle]")
    
    return mst, total_jarak

# ---------- 5. EKSEKUSI & OUTPUT ----------
print("=" * 50)
print("PROGRAM MST - JARINGAN JALAN ANTAR KOTA")
print("= = = = = = = = = = = = = = = = = = = = =")
print("\nKasus: Semua kota harus terhubung dengan total jarak MINIMUM")
print("\nData jalan antar kota:")
print("-" * 40)
for jarak, kota1, kota2 in edges:
    print(f"  {kota1:8s} --- {kota2:8s} : jarak = {jarak}")
print("-" * 40)

# Jalankan algoritma Kruskal
mst, total_jarak = kruskal(edges)

# Output hasil MST
print("\n" + "=" * 50)
print("HASIL JARINGAN JALAN OPTIMAL (MST):")
print("=" * 50)
print("\nEdge yang dipilih (jalan yang akan dibangun):")
print("-" * 40)
for kota1, kota2, jarak in mst:
    print(f"  {kota1:8s} --- {kota2:8s} : jarak = {jarak}")
print("-" * 40)
print(f"\n🌟 TOTAL JARAK MINIMUM = {total_jarak}")
print("=" * 50)

# Verifikasi manual
print("\nVerifikasi rute:")
print("  Depok - Bogor (2) + Depok - Bandung (4) + Depok - Jakarta (3) = 9")
print("  Atau: Bogor - Depok (2) + Depok - Jakarta (3) + Depok - Bandung (4)")
print("  Semua kota terhubung melalui Depok sebagai pusat!")

# Jawaban Analisis: 
# 1. Kasus apa yang dipilih?
"""
Kasus 1 - Jaringan Jalan Antar Kota

Data jalan antar kota:
Bogor - Jakarta = 5
Bogor - Depok = 2
Depok - Jakarta = 3
Jakarta - Bandung = 6
Depok - Bandung = 4
""" 
# 2. Algoritma apa yang digunakan? Algoritma Kruskal
"""
-Bekerja dengan mengurutkan semua edge dari jarak terkecil ke terbesar
-Memilih edge satu per satu yang tidak membentuk cycle
-Cocok untuk kasus dengan daftar edge yang jelas
"""
# 3. Edge mana saja yang dipilih dalam MST? 
"""
Edge:
Bogor-Depok = 2
Depok-jakarta= 3
Depok-Bandung= 4
"""
# 4. Berapa total bobot MST? Total bobot minimum = 2 + 3 + 4 = 9
# 5. Mengapa edge tertentu tidak dipilih?
"""
Edge : Bogor-Jakarta = jarak 5 = karena bogor-jakarta sudah terhubung melalui Bogor-Depok_Jakarta(yang akan membuat cycle)
Edge: Jakarta-Bandung = jarak 6 = jakarta-bandung telah terhubung melelui jalur jakarta-depok-bandung (ini akan membuat cycle)
"""