#=============================================
# Nama: Ludmilla Riza Maharuni
# NIM: J0403251001
#latihan 1
#=============================================

def insertion_sort(data):
    for i in range(1,len(data)):
        key = data[i]
        j=i-1
        while j>=0 and data[j] > key:
            data[j+1]=data[j]
            j-=1
        data[j+1] = key
        return data

'''
1. perulangan mulai dari index satu karena menggap elemen pertama(index 0) sudah berada di bagian 
yang terurut dan agar lebih mudah untuk memahami logikanya

2. fungsi variabel key adalah sebagai tempat penyimpanan sementara untuk nilai yang 
sedang kita memasukkan ke posisi yang bener
Saat kita menemukan angka di sebelah kiri yang lebih besar dari key, angka tersebut akan digeser ke kanan (menimpa posisi asal key).
Tanpa menyimpan nilai tersebut di variabel key, 
kita akan kehilangan angka yang sedang ingin kita urutkan karena tertimpa oleh angka yang digeser.

3. Digunakan while bukan for dengan menggunakan while  perulangan langsung berhenti begitu menemukan
posisi yang tepat (saat data[j] tidak lagi lebih besar dari key) atau telah mencapai tujuan paling kiri
(j >=0).
sedangkan for akan mengecek semua elemendi sebelah kiri meskipun posisi yang benar telah di temukan

4. operasi yang terjadi di dalam while  adalah pergeseran(shifting)
jika data[j] > Key maka:
data[j+1]=data[j] : nilai yang lebih besar digeser satu posisi kekanan
j-=1 : bergerak satu langkah ke kiri untuk mengeceknya

'''