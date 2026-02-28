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

def jumlah_list(data,index=0):
    #basecase jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    #recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data,index+1)
print("==============program===========")
print(jumlah_list([2,4,6,8]))
