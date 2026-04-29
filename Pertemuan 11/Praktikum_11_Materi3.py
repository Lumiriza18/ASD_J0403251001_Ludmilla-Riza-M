#================================
# dfs
#Nama : Ludmilla Riza Maharuni
#NIM : J0403251001
#================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, node, visited):
    # fungsi untuk melakukan penelusuran graph menggunakan DFS
    # graph : dictionary yang menyimpan graph
    # node : menyimpan node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi

    # set untuk menyimpan node yang sudah dikunjungi
    visited.add(node)
    # tampilkan node saat ini sebagai node yang sudah dikunjungi
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# set visited
visited = set()

# menjalankan DFS dari node A
dfs(graph, 'A', visited)
