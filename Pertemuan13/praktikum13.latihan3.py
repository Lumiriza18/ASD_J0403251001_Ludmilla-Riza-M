# Nama  : Ludmilla Riza Maharuni
# NIM   :  J0403251001
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree

import heapq 
graph = { 
'A': {'B': 4, 'C': 2, 'D': 5}, 
'B': {'A': 4, 'D': 3}, 
'C': {'A': 2, 'D': 1}, 
'D': {'A': 5, 'B': 3, 'C': 1} 
} 
def prim(graph, start): 
    visited = set([start]) 
    edges = [] 
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    mst = [] 
    total_weight = 0 
    while edges:
        weight, u, v = heapq.heappop(edges) 
    if v not in visited: 
        visited.add(v) 
        mst.append((u, v, weight)) 
        total_weight += weight 
        for neighbor, w in graph[v].items(): 
            if neighbor not in visited: 
                heapq.heappush(edges, (w, v, neighbor)) 
    return mst, total_weight 
mst, total = prim(graph, 'A') 
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 
print("Total bobot =", total) 

# Jawaban Analisis: 
# 1. Node awal apa yang digunakan? Node 'A' digunakan sebagai node awal (start).
# 2. Edge mana yang dipilih pertama kali? Edge (A, C) dengan bobot 2 dipilih pertama kali.
# 3. Bagaimana Prim menentukan edge berikutnya? 
"""
Algoritma Prim selalu memilih edge dengan bobot terkecil yang:
- Menghubungkan node yang sudah di-visit dengan node yang belum di-visit
- Setiap edge baru dimasukkan ke dalam priority queue (min-heap)

Langkah-langkahnya:
1. Mulai dari visited = {A}
2. Masukkan semua edge dari A ke heap
3. Ambil edge berbobot paling kecil dari heap
4. Jika node tujuan belum dikunjungi, tambahkan ke MST
5. Masukkan semua edge dari node baru ke heap
6. Ulangi langkah 3-5 sampai semua node ter-visit
"""
# 4. Berapa total bobot MST yang dihasilkan?  total bobotnya 5
# 5. Apa perbedaan pendekatan Prim dan Kruskal? 
"""
A. Prim
Mulai dari 1 node, lalu melebar ke tetangga terdekat

B.Kruskal
Mulai dari edge terkecil, lalu menyambung edge-edge kecil lainnya

Analogi Gampang:
A. Prim
Seperti menyiram tanaman dari satu titik, air merambat ke segala arah
B.Kruskal
Seperti membangun tim dengan memasangkan orang terdekat, lalu menggabungkan tim-tim kecil
"""
