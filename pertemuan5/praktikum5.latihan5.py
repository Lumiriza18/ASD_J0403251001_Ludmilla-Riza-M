#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Latihan 5: Kasus generator PIN
#================================================

def buat_pin(panjang,hasil=""): 
    if len(hasil)==panjang: #jika pin sudah mwencapai panjang 3 angka,maka komputer akan mencetak nya dan berhenti di jalur itu
        print("pin:",hasil)
        return
    for angka in["0","1","2"]: #menggunakan for agar komputer mencoba angka "0", lalu "1",lalu"2" secara bergantian
        buat_pin(panjang,hasil +angka)
buat_pin(3) #menentukan panjang dari parameter pin nya