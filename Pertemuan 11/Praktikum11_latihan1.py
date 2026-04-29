#================================
# Praktikum 11 - Latihan 1(BFS)
#Nama : Ludmilla Riza Maharuni
#NIM : J0403251001
#================================
from collections import deque

graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

#1. Node mana yang dikunjungi pertama?  Rumah
#2. Mengapa BFS cocok untuk mencari jalur terdekat? Karena BFS mengecek/mengunjungi tiap" lecvel dan mencari  node yang di tuju dengan cara mengecek note tetangga
#3. Apa perbedaan urutan BFS jika struktur graph diubah? Urutan BFS akan berubah sesuai dengan struktur graph yang diubah, karena BFS mengunjungi node berdasarkan level dan urutan tetangga yang ada dalam graph. Jika struktur graph diubah, maka urutan kunjungan node juga akan berubah sesuai dengan perubahan tersebut.
