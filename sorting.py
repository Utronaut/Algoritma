# Algoritma Mergesort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Rekursi untuk mengurutkan masing-masing bagian
        merge_sort(left_half)
        merge_sort(right_half)

        # Menggabungkan kembali
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menambahkan sisa elemen jika ada
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Data yang akan diurutkan
x = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
merge_sort(x)
print("Hasil Merge Sort :", x)

#Algoritma Quicksort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Data yang akan diurutkan
x = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
x_sorted = quick_sort(x)
print("Hasil Quick Sort :", x_sorted)


    
"""
Merge Sort

Best Case :
Kondisi => Data sudah terurut.
Kompleksitas => Tetap O(n log n), karena merge sort akan selalu membagi data menjadi dua dan menggabungkannya kembali, terlepas dari kondisi data.

Worst Case :
Kondisi => Data terbalik atau tidak terurut sama sekali.
Kompleksitas => Tetap O(n log n), karena proses pembagian dan penggabungan selalu sama.

Average Case :
Kondisi => Data acak.
Kompleksitas => O(n log n), karena proses tetap sama untuk semua kasus.

Untuk algoritma Merge Sort, kompleksitas waktu pada semua kasus, baik best case, worst case, maupun average case, adalah O(n log n). Hal ini disebabkan oleh sifat algoritma yang selalu membagi data menjadi dua bagian dan menggabungkannya kembali dengan cara yang sama, tanpa memedulikan urutan data awal. Bahkan jika data sudah terurut (best case) atau benar-benar tidak terurut (worst case), langkah-langkah pembagian dan penggabungan tetap dilakukan secara konsisten sehingga kompleksitasnya tidak berubah.



Quick Sort

Best Case :
Kondisi => Pivot membagi data menjadi dua bagian yang seimbang setiap iterasi.
Kompleksitas => O(n log n), karena pembagian yang seimbang meminimalkan jumlah rekursi.

Worst Case :
Kondisi => Data sudah terurut atau terbalik (pivot selalu menjadi elemen terkecil/terbesar).
Kompleksitas => O(n²), karena setiap iterasi hanya mengurangi ukuran array sebesar satu elemen.

Average Case :
Kondisi => Data acak.
Kompleksitas => O(n log n), karena probabilitas pembagian yang seimbang lebih tinggi dalam data acak.

Sementara itu, untuk Quick Sort, performa algoritma sangat dipengaruhi oleh pemilihan pivot. Pada best case, jika pivot membagi data menjadi dua bagian yang hampir sama besar pada setiap iterasi, maka kompleksitasnya adalah O(n log n) karena jumlah rekursi menjadi minimal. Namun, pada worst case, seperti saat data sudah terurut atau terbalik, pivot yang terpilih selalu menjadi elemen terbesar atau terkecil, sehingga data hanya terbagi sedikit setiap iterasi. Akibatnya, jumlah rekursi meningkat signifikan dan kompleksitas menjadi O(n²). Pada average case, dengan data yang acak, probabilitas pembagian yang seimbang lebih tinggi sehingga kompleksitas mendekati O(n log n), menjadikannya lebih efisien secara umum dibandingkan dengan kasus terburuk.  

"""