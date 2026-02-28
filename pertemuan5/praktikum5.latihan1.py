#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Latihan1: Rekursi pangkat
#================================================

def pangkat(a,n):
    #base case
    if n==0:
        return 1
    #recursive case
    return a*pangkat(a,n-1)
print(pangkat(2,4)) #ambil 2 sebanyak 4 kali

"""
seperti:
ke-1: ambil satu angka 2, sisa 3 kali lagi
ke-2: ambil satu angka 2, sisa 2 kali lagi
ke-3: ambil satu angka 2, sisa 1 kali lagi
ke-4: ambil satu angka 2, sisa 0 kali lagi
berhenti dan kembali ke 1 karena nilainya 0

2x2x2x2x1=16
"""