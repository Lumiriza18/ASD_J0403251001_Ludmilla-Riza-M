#================================================
#Nama:Ludmilla Riza Maharuni
#NIM: J0403251001
#kelas: B2
#================================================

#===============================================
#Latihan 3: Mencari nilai maksimum
#================================================

def cari_maks(data,index=0): #base case/titik berhenti)
    #base case
    if index == len(data)-1:
        return data[index]
    
    #recursif case
    maks_sisa=cari_maks(data,index+1)

    if data[index]>maks_sisa: #bagoian perbandingan
        return data[index]
    else:
        return maks_sisa

angka=[3,7,2,9,5]
print("nilai maksimum:", cari_maks(angka))

"""
pada list [3, 7, 2, 9, 5]:

Si 3 bertanya ke sisa list [7, 2, 9, 5]: "Siapa yang paling gede?"

Si 7 bertanya ke sisa list [2, 9, 5]: "Siapa yang paling gede?"

Si 2 bertanya ke sisa list [9, 5]: "Siapa yang paling gede?"

Si 9 bertanya ke sisa list [5]: "Siapa yang paling gede?"

Si 5 (angka terakhir) menjawab: "Aku!" (karena dia sendirian).

Kembali ke Si 9: "Antara aku (9) dan kiriman dari belakang (5), besaran mana? Oh, besaran 9."

Kembali ke Si 2: "Antara aku (2) dan kiriman dari belakang (9), besaran mana? Besaran 9."

Kembali ke Si 7: "Antara aku (7) dan kiriman dari belakang (9), besaran mana? Besaran 9."

Kembali ke Si 3: "Antara aku (3) dan kiriman dari belakang (9), besaran mana? Besaran 9."

Hasil Akhir: Nilai maksimum adalah 9.
"""