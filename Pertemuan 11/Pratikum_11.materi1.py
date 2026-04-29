#====================================
#implementasi dasar graph
#Nama : Ludmilla Riza Maharuni
#NIM : J0403251001
#====================================

graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}
for node in graph:
    print(node, "->",graph[node])
