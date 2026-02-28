#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Materi rekursif:faktorial
#recursive case=>3!=3x2x1
#base case => 0 berhenti
#================================================

def faktorial(n):
    if n==0: #kalo base case sama dengan 0
        return 1 #kembali ke satu,berhenti
    #rekursif cave
    return n*faktorial(n-1) #n-1*n-2*n-3......n-?
print("======program faktorial===========")
print("hasilFaktorial: ",faktorial(4)) #masukkan/panggil 4 ke persamman n