#================================
# Praktikum 11 - Latihan 1(DFS)
#Nama : Ludmilla Riza Maharuni
#NIM : J0403251001
#================================
#Graph berikut merepresentasikan jalur eksplorasi: 
from platform import node


graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': [] 
} 
#Gunakan algoritma DFS untuk menelusuri graph mulai dari node A. 
def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 

visited = set() 
print("DFS dari A:") 
dfs(graph, 'A', visited) 


#Pertanyaan Analisis 
#1. Node mana yang dikunjungi pertama? A  
#2. Mengapa DFS cocok untuk mencari jalur terdekat?  Karena DFS mengeksplorasi satu cabang hingga selesai sebelum kembali dan mengeksplorasi cabang lainnya, sehingga dapat menemukan jalur terdekat jika jalur tersebut berada di cabang yang pertama kali dieksplorasi. Namun, perlu diingat bahwa DFS tidak selalu menjamin menemukan jalur terdekat dalam semua kasus, tergantung pada struktur graph dan urutan eksplorasi.
#3. Apa perbedaan urutan DFS jika struktur graph diubah? Urutan DFS akan berubah sesuai dengan struktur graph yang diubah, karena DFS mengunjungi node berdasarkan urutan tetangga yang ada dalam graph. Jika struktur graph diubah, maka urutan kunjungan node juga akan berubah sesuai dengan perubahan tersebut.