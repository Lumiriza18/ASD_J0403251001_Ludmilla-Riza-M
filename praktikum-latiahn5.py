#=============================================
# Nama: Ludmilla Riza Maharuni
# NIM: J0403251001
#latihan 5
#=============================================

def merge(left,right):
    result=[]
    i=0
    j=0
    while i< len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

'''
1. Lengkapi kondisi agar menjadi ascending
Melengkapi Kondisi agar Menjadi Ascending
​Bagian yang kosong pada blok if harus diisi dengan:
left[i] <= right[j] (atau bisa juga left[i] < right[j])
​Penjelasan: Karena kita ingin hasil akhirnya terurut dari kecil ke besar (ascending), 
kita membandingkan elemen dari bagian kiri (left[i]) dengan bagian kanan (right[j]). 
Jika elemen di sebelah kiri lebih kecil atau sama dengan elemen di sebelah kanan, maka elemen kiri 
tersebut yang akan dimasukkan (append) ke dalam list result terlebih dahulu.

​2. Penjelasan Fungsi result.extend()
​2. Fungsi result.extend() digunakan untuk
menambahkan sisa elemen dari list kiri
atau kanan yang belum dimasukkan ke dalam result.
Ini diperlukan karena saat perbandingan selesai,
salah satu list pasti masih memiliki sisa elemen.

'''