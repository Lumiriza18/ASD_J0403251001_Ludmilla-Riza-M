# Nama  :  Ludmilla Riza Maharuni
# NIM :  J0403251001
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Program Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ========================================================== 

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Bobot menunjukkan jarak antar kota dalam satuan kilometer
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},      # Dari Bogor ke Jakarta (5), Depok (2)
    'Depok': {'Jakarta': 2, 'Bandung': 6},    # Dari Depok ke Jakarta (2), Bandung (6)
    'Jakarta': {'Bandung': 7},                # Dari Jakarta ke Bandung (7)
    'Bandung': {}                              # Bandung tidak memiliki tetangga keluar
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Dijkstra dengan priority queue (heapq)
    Parameter:
        graph: dictionary yang merepresentasikan weighted graph
        start: node awal (source node)
    Mengembalikan:
        distances: dictionary berisi jarak terpendek dari start ke setiap node
    """
    
    # kita belum mengetahui jarak ke node tersebut
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # Priority queue (min-heap) menyimpan pasangan (jarak, node)
    # Heap akan selalu mengeluarkan node dengan jarak terkecil terlebih dahulu
    priority_queue = [(0, start)]
    
    # Proses selama priority queue masih berisi node
    while priority_queue:
        # Ambil node dengan jarak terkecil dari heap
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # OPTIMASI: Jika jarak yang di-pop lebih besar dari jarak yang tercatat,
        # lewati proses ini (sudah ada jalur yang lebih baik)
        if current_distance > distances[current_node]:
            continue
        
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak sementara melalui node saat ini
            distance = current_distance + weight
            
            # Jika ditemukan jarak yang lebih kecil ke tetangga,
            # perbarui jarak dan masukkan ke priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 3. Penentuan node awal dalam program
start_node = 'Bogor'  # Node awal dapat diubah sesuai kebutuhan

# Eksekusi algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# 4. Output jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {start_node}:")
print("-" * 35)
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")
print("-" * 35)

# Menampilkan rute terpendek ke setiap kota (opsional)
print("\nPenjelasan jalur terpendek:")
print("-" * 50)

# Bogor ke Bogor
print(f"Bogor -> Bogor: langsung (0 km)")

# Bogor ke Depok (langsung)
print(f"Bogor -> Depok: langsung (2 km)")

# Bogor ke Jakarta (via Depok)
print(f"Bogor -> Jakarta: Bogor -> Depok (2) + Depok -> Jakarta (2) = 4 km")
print(f"  (lebih baik dari langsung Bogor -> Jakarta = 5 km)")

# Bogor ke Bandung (via Depok)
print(f"Bogor -> Bandung: Bogor -> Depok (2) + Depok -> Bandung (6) = 8 km")
print(f"  (lebih baik dari via Jakarta: Bogor -> Depok(2) + Depok -> Jakarta(2) + Jakarta -> Bandung(7) = 11 km)")


# Jawaban Analisis: 
# 1. Node awal yang digunakan apa? 
#Node awal yang digunakan adalah 'Bogor'. Ini ditentukan pada variabel start_node.

# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# yaitu adalah 'Depok' dengan jarak 2 km. 

# 3. Node mana yang memiliki jarak paling besar dari node awal? 
#Node yang memiliki jarak paling besar dari Bogor adalah 'Bandung' 
#dengan jarak 8 km.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Langkah-langkah algoritma Dijkstra pada kasus ini:
# a. Inisialisasi: distances = {Bogor:0, Depok:tak hingga, Jakarta:tak hingga, Bandung:tak hingga}
# priority_queue = [(0, Bogor)]
# b. Pop (0, Bogor): tetangga Depok (2) dan Jakarta (5)
# - Depok: 0+2=2 < ∞ → update Depok=2, push (2, Depok)
# - Jakarta: 0+5=5 < ∞ → update Jakarta=5, push (5, Jakarta)
# status: Bogor=0, Depok=2, Jakarta=5, Bandung= tak hingga
# c. Pop (2, Depok): tetangga Jakarta (2) dan Bandung (6)
# - Jakarta: 2+2=4 < 5 → update Jakarta= 4, push (4, Jakarta)
# - Bandung: 2+6=8 < ∞ → update Bandung= 8, push (8, Bandung)
# status: Bogor=0, Depok=2, Jakarta=4, Bandung=8
# d. Pop (4, Jakarta): tetangga Bandung (7)
#- Bandung: 4+7=11 > 8 → tidak update (karena 11 > 8)
# status tetap: Bogor=0, Depok=2, Jakarta=4, Bandung=8
# e. Pop (8, Bandung): Bandung tidak punya tetangga → selesai

# f. Hasil akhir: jarak terpendek dari Bogor ke semua kota telah ditemukan.
"""
Inti dari algoritma ini adalah "relaksasi" yaitu terus memperbaiki jarak
terpendek dengan memanfaatkan priority queue untuk selalu memproses node
dengan jarak terkecil terlebih dahulu.
"""
