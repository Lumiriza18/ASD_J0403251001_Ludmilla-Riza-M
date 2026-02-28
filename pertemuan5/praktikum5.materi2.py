#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Materi rekursif: call stack
# Tracing bilangan(masuk-keluar)
#input 3
#3-2-1 (keluar)
#1-2-3(masuk)
#================================================

def hitung(n):
    #base case
    if n==0:
        print("selesai")
        return
    print("masuk",n) #dicetak saat fungsi dipanggil
    hitung(n-1) #recursive case , #panggil diri sendiri  dengan n-1
    print("keluar",n) #dicetak sewtelah fungsi rekursif selesai

print("==========program tracing===========")
hitung(2)


