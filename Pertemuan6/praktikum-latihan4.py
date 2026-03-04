#=============================================
# Nama: Ludmilla Riza Maharuni
# NIM: J0403251001
#latihan 4
#=============================================

def merge_sort(data):
    if len(data)<=1:
        return data
    mid= len(data)//2
    left=data[:mid]
    right=data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge_sort(left_sorted,right)

'''
1. yang dimaksud dengan base case adalah kondisi yang berfungsi untuk menghentikan
memanggil pemanggilan fungsi rekursif.

2. alsan memanggil dirinya sendiri adalah untuk memecahkan masalah yang besar dan kompleks dengan 
membagikan masalah-masalah kecil  yang polanya sama misalnya seperti  x+1=2
x=3 dan kita seperti memanggil fungsi x 

3. tujuan dari fungsi merge()
untuk menggabungkan dua sub-list yang sudah terurut/ seperti memanggil suatu fungsi 
'''