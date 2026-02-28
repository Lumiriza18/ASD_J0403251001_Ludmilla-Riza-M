#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Latihan 2: Tracing Rekursi
#================================================

def countdown(n):
    if n==0:
        print("selesai")
        return
    
    print("masuk:",n)
    countdown(n-1)
    print("keluar", n)
countdown(3) #untuk memanggil diri sendiri


"""
saat bagian masuk telah habis ada printah return fungsi countdown(0)
sudah di kerjakan lanjut memanggil fungsi countdown(1)
tanpa melewati baris ke 17 dan langsung menuju baris ke 18 setelah itu
lanjut ke countdown yang lain
"""