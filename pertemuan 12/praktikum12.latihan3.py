#Nama :Ludmilla Riza Maharuni
#NIM: J0403251001
#Kelas: B2

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 

# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
} 

def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 

    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 

    # Jarak dari start ke start adalah 0 
    distances[start] = 0 

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 

        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 

                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
                    return distances 

hasil = bellman_ford(graph, 'A') 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa bobot langsung dari A ke B? 5
# 2. Berapa total bobot jalur A -> C -> B? 4(AC)-2(CB)=2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? A-B =5 lebih jauh dari pada A-C-B= 2 
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
"""
Algoritma Bellman-Ford merupakan algoritma shortest path yang mampu menangani graph 
dengan bobot negatif. Algoritma ini bekerja dengan melakukan relaksasi seluruh edge secara 
berulang untuk memastikan setiap node memperoleh jarak minimum yang benar. Meskipun 
prosesnya lebih lambat dibandingkan Dijkstra, Bellman-Ford memiliki keunggulan dalam 
mendeteksi dan menangani edge berbobot negatif, sehingga lebih fleksibel digunakan pada 
kasus tertentu
"""
# 5. Apa yang dimaksud dengan proses relaksasi edge? 
"""
Relaksasi edge adalah proses memperbarui jarak ke suatu node jika ditemukan jalur yang lebih pendek melalui node lain. Secara matematis:
Jika distance[u] + weight(u,v) < distance[v], maka set distance[v] = distance[u] + weight(u,v)
Analoginya seperti mengendurkan/mengencangkan tali - jika ada jalur yang lebih pendek, kita "relaks" (perbarui) nilai jaraknya.
"""
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
"""
untuk bellman-ford dia bisa merealisasikan dengan bilangan negatif walaupun cukup lama
untuk Dijkstra dia tidak bisa merealisasikan dengan ada nya bilangan negatif walaupun lebih cepat dari pada bellman-ford
"""