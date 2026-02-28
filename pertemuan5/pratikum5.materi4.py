#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Materi backtracking 1: kombinasi biner(n) 
#================================================

def biner(n,hasil=""):
    #base case:jika pangjang string sudah n, cetak hasil
    if len(hasil) == n: #syarat berhenti ibarat sedang membuat kata ,jika panjang sudah mencapai target (n) maka tidak perlu ditambh lagi
        print(hasil)
        return
    #choose + Explore : tambah "0"
    biner(n,hasil + "0") #menambahkan "0" ke dalam susunan

    #choose + explore: tambah "1"
    biner(n,hasil +"1") #setelahangka 0 selesai ,program akan mencoba pilihanlain yaitu menmabhkan angka 1

biner(3)