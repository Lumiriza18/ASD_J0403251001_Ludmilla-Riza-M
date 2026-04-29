#=================================
# implementasi BFS
#Nama : Ludmilla Riza Maharuni
#NIM : J0403251001
#================================

#representasi graph
graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}
#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

#representasi graph
graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}


def bfs( graph, start):
    #fungsi ini untuk melakukan penelusuran graph dengan BFS
    # graph : dictionarry yang menyimpan struktur dari grapth
    # start : node awal penelusuran

    #queeu digunakan untuk menyimpan node yang di proses / dibaca
    queeu = deque()
    #variabel yang digunakan utuk menyimpan node yang telah di kunjungi ataudi baca
    visited=set()

    #masukkan node awal ke queeu
    queeu.append(start)

    #tandai node awal sebagai node yang sudah di kunjungi
    visited.add(start)

    while queeu :
        #mengambil node paling depan dari queeu untuk di proses
        node = queeu.popleft()
        #tampilkan node yang sedang dikunjungi /di baca
        print(node,end=" ")
        #priksa tetangga yang di ambil dari node 
        for neighbor in graph[node]:
            #jika tetangga belum di kunjungi 
            if neighbor not in visited:
                # tanfdai sebagai sudah di kunjungi
                visited.add(neighbor)
                #masukkan tetangga ke queeu untuk diproses nanti
                queeu.append(neighbor)

# menjalankan bfs dari node A
bfs(graph,'A')
