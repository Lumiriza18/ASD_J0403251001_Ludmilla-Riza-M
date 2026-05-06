# Nama  :  Ludmilla Riza Maharuni
# NIM :  J0403251001
# Kelas : B2
# materi dijkstra

import heapq 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
}

def dijkstra(graph, start): 
    # Menyimpan jarak minimum 
    distances = {node: float('inf') for node in graph} 

    # Jarak node awal = 0 
    distances[start] = 0 

    # Priority queue 
    pq = [(0, start)] 

    while pq: 
        current_distance, current_node = heapq.heappop(pq) 

        # Periksa semua tetangga 
        for neighbor, weight in graph[current_node].items(): 

            distance = current_distance + weight 

            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 

                distances[neighbor] = distance 

                heapq.heappush(pq, (distance, neighbor)) 

    return distances 
hasil = dijkstra(graph, 'A') 
print(hasil) 
#jelaskan algoritma
#Selalu pilih jalan yang paling cepat dulu
#Kalau nemu jalan pintas, langsung ganti rute

#PEnjelasan terceptanya
#Dari A ke A = 0 (diri sendiri)
#Dari A ke B = 4
#Dari A ke C = 2
#Dari A ke D = 3 (lewat C lebih cepat)

#distances → menyimpan jarak tercepat ke tiap node
#heapq → antrian prioritas (selalu ambil yang jaraknya paling kecil)
#pq → daftar node yang akan diproses