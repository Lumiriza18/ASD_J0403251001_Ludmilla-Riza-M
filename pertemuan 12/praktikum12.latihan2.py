# Nama  :  Ludmilla Riza Maharuni
# NIM :  J0403251001
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 2: Implementasi Dijkstra 
# ========================================================== 
import heapq 

# Weighted graph dengan bobot positif 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

def dijkstra(graph, start): 
    # Fungsi untuk mencari jarak terpendek dari node start 
    # ke seluruh node lain menggunakan algoritma Dijkstra.
    
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]
    
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 
        
        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
            
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    
    return distances  # ← HARUS berada di dalam fungsi (satu indentasi dengan def)

hasil = dijkstra(graph, 'A') 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa jarak terpendek dari A ke B? 4
# 2. Berapa jarak terpendek dari A ke C? 2
# 3. Berapa jarak terpendek dari A ke D? 3
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
#A+D=0+3=3
#C+B=2+3=5 
#karena kita akan mencari jalur terkecil bukan terjauh itulah mengapa kita memili jalur A & D yang 3 daripada C & D yang 5
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
#priority_queue (yang diimplementasikan dengan heapq) berfungsi untuk:
#Menyimpan node-node yang akan diproses bersama dengan jarak sementaranya
#Selalu memproses node dengan jarak terkecil terlebih dahulu (karena sifat min-heap)
#Mempercepat algoritma karena tidak perlu mencari node dengan jarak minimum secara linear setiap iterasi
#Menjamin bahwa ketika sebuah node di-pop dari queue, jaraknya sudah final (optimal)
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 
# Dijkstra menggunakan pendekatan greedy dengan 
#asumsi bahwa jarak terpendek yang sudah dipilih tidak akan berubah lagi, sehingga jika 
#terdapat edge dengan bobot negatif, algoritma dapat menghasilkan perhitungan shortest path 
#yang salah. Selain itu, pada graph yang sangat besar dengan jumlah node dan edge yang
#banyak, proses perhitungan juga dapat menjadi lebih kompleks dan membutuhkan 
#penggunaan struktur data tambahan seperti priority queue agar tetap efisien. 