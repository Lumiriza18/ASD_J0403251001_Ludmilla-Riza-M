#=============================================
# Nama: Ludmilla Riza Maharuni
# NIM: J0403251001
#=============================================

def merge_sort(data, depth=0):
    # Membuat indentasi berdasarkan kedalaman rekursi (untuk tracing)
    indent = "  " * depth
    print(f"{indent}--> Memproses: {data}")

    # Base Case: Jika data hanya berisi 1 elemen atau kosong
    if len(data) <= 1:
        return data

    # 1. DIVIDE: Membagi data menjadi dua bagian
    mid = len(data) // 2
    left_part = data[:mid]
    right_part = data[mid:]

    print(f"{indent}   [Divide] Kiri: {left_part} | Kanan: {right_part}")

    # 2. RECURSIVE CALL: Memanggil fungsi ini kembali untuk setiap bagian
    # Jangan lupa masukkan parameter (depth + 1)
    left_sorted = merge_sort(left_part, depth + 1)
    right_sorted = merge_sort(right_part, depth + 1)

    # 3. CONQUER & COMBINE: Menggabungkan kembali bagian yang sudah urut
    return merge(left_sorted, right_sorted, depth)

def merge(left, right, depth):
    result = []
    i = 0  # Pointer untuk list kiri
    j = 0  # Pointer untuk list kanan

    # Membandingkan elemen dari list kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Mengambil sisa elemen jika ada (slicing)
    result.extend(left[i:])
    result.extend(right[j:])
    
    indent = "  " * depth
    print(f"{indent}   [Merge] Hasil: {result}")
    return result

# --- Eksekusi Program ---
angka = [13, 7, 28, 5, 19, 36, 4]
print("PROSES SORTING:")
print("=" * 40)
hasil_akhir = merge_sort(angka)
print("=" * 40)
print(f"Hasil Akhir: {hasil_akhir}")