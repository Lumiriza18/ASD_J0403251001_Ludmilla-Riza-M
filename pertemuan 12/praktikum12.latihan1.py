# Nama  :  Ludmilla Riza Maharuni
# NIM :  J0403251001
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path 

# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 
# Representasi weighted graph menggunakan dictionary bersarang 

graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] 
jalur_2 = graph['A']['C'] + graph['C']['D'] 
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")

#pertanyaan Analisis 
# 1. Berapa total bobot jalur A -> B -> D? 
# J: Total bobot jalur A → B → D = 4 + 5 = 9
# 2. Berapa total bobot jalur A -> C -> D? 
# J:Total bobot jalur A → C → D = 2 + 1 = 3
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
#J:jalur terpendek = A → C → D (dengan bobot 3)
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#J:Karena yang menentukan "pendek" dalam weighted graph adalah total bobot (cost/distance), bukan jumlah edge (hop count).
#Jalur A→B→D memiliki 2 edge dengan bobot 9
#Jalur A→C→D memiliki 2 edge dengan bobot 3
#Kedua jalur memiliki jumlah edge yang sama, tetapi bobotnya berbeda. Bahkan bisa terjadi jalur dengan lebih banyak edge memiliki total bobot lebih kecil (misalnya jalur 3 edge dengan bobot 1+1+1 = 3, lebih pendek dari jalur 2 edge dengan bobot 6+6 = 12).
#Intinya: Yang dihitung adalah akumulasi bobot setiap edge, bukan banyaknya edge yang dilalui.

