Horas Imanuel Siregar (F55123053) dari kelas Teknik Informatika B

Penjelasan kuis 2 :
1. Bubble Sort (disebut sebagai "naive bayes" dalam soal):
Kasus Terbaik (Best Case): O(n)
Kasus terbaik terjadi ketika array sudah dalam keadaan terurut.
Dalam kondisi ini, algoritma hanya akan melakukan satu iterasi melalui array, membandingkan setiap pasangan elemen yang berdekatan tanpa melakukan pertukaran (swap).
Meskipun loop dalam tetap berjalan sebanyak n-1 kali, loop luar akan berhenti setelah iterasi pertama.
2. Merge Sort (metode divide-and-conquer):
Kasus Terbaik (Best Case): O(n log n)
Merge Sort memiliki kompleksitas waktu yang sama untuk kasus terbaik, rata-rata, dan terburuk.
Hal ini karena, terlepas dari urutan array masukan, Merge Sort selalu membagi array menjadi dua bagian, mengurutkannya secara rekursif, dan kemudian menggabungkan dua bagian yang telah diurutkan.
Proses pembagian membutuhkan log n langkah, dan setiap langkah melibatkan penggabungan yang membutuhkan n operasi.
