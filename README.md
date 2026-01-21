# PROJECT UAS ALGORITMA PEMROGRAMAN
## Implementasi Huffman Coding dan Binary Search Tree (BST) Menggunakan Python

## Deskripsi Proyek
Proyek ini merupakan Project UAS Mata Kuliah Algoritma Pemrograman yang bertujuan untuk mengimplementasikan dua konsep utama dalam algoritma dan struktur data, yaitu Huffman Coding dan Binary Search Tree (BST).
Program dibuat secara interaktif berbasis Command Line Interface (CLI).

## Anggota Kelompok
- Muhammad Aditya Wibawa (202410370110407)
- Sadaika Nursadiq (202410370110398)
- Alvin Nur Fajrianto (202410370110419)
- Syahlevi Miraz Nugraha (202410370110425)

## Teknologi yang Digunakan
- Bahasa Pemrograman: Python
- Library bawaan:
    - heapq
    - os
    - collections
    - sys

## Fitur Program

### 1. Huffman Coding
Fitur yang diimplementasikan:
- Menghitung frekuensi setiap karakter
- Membangun Huffman Tree
- Menghasilkan kode Huffman untuk setiap karakter
- Melakukan kompresi (encoding) teks
- Melakukan dekompresi (decoding) teks
- Menampilkan ukuran teks asli dan terkompresi
- Menghitung dan menampilkan rasio kompresi

### 2. Binary Search Tree (BST)
Fitur yang diimplementasikan:
- Insert (menambahkan node ke BST)
- Search (mencari node dan menampilkan jalur pencarian)
- Delete (menghapus node dari BST)
- Traversal tree:
    - InOrder
    - PreOrder
    - PostOrder
- Menampilkan struktur BST secara visual
- Menyediakan contoh BST otomatis

## Cara Menjalankan Program
Setelah program dijalankan, pengguna akan diarahkan ke **menu utama**.  
Langkah penggunaan program adalah sebagai berikut:

1. Pilih menu **Huffman Coding – Kompresi Teks** untuk melakukan kompresi dan dekompresi teks.
    - Masukkan teks yang ingin dikompresi.
    - Program akan menampilkan frekuensi karakter, kode Huffman, teks terenkripsi, rasio kompresi, dan hasil dekompresi.


2. Pilih menu **Binary Search Tree – Operasi dan Traversal** untuk mengelola data BST.
    - Tambahkan node ke dalam BST.
    - Cari node dan lihat jalur pencariannya.
    - Hapus node dari BST.
    - Tampilkan traversal (InOrder, PreOrder, PostOrder).
    - Tampilkan struktur BST dalam bentuk pohon.


3. Pilih menu **Tentang Program** untuk melihat informasi singkat mengenai tujuan dan fitur program.


4. Pilih menu **Keluar** untuk mengakhiri program.

Seluruh interaksi dilakukan melalui input angka dan teks sesuai instruksi yang ditampilkan pada layar.


## Menu Utama Program
Saat program dijalankan, akan muncul menu utama sebagai berikut:
```
1. Huffman Coding - Kompresi Teks
2. Binary Search Tree - Operasi dan Traversal
3. Tentang Program
4. Keluar
```

## Konsep Algoritma

### Huffman Coding
Huffman Coding merupakan algoritma kompresi data bersifat lossless yang menggunakan struktur data priority queue. Karakter dengan frekuensi kemunculan tinggi akan memiliki kode biner yang lebih pendek.

### Binary Search Tree
Binary Search Tree adalah struktur data berbentuk pohon dengan aturan nilai kiri lebih kecil dari root dan nilai kanan lebih besar dari root. Traversal digunakan untuk membaca data dalam urutan tertentu.

## Output Program
Program akan menampilkan:
- Frekuensi karakter
- Kode Huffman untuk setiap karakter
- Teks hasil kompresi dan dekompresi
- Rasio kompresi
- Traversal BST
- Struktur BST dalam bentuk pohon

## Kesimpulan
Program ini berhasil mengimplementasikan algoritma Huffman Coding dan struktur data Binary Search Tree secara interaktif. Program membantu memahami konsep algoritma dan struktur data secara praktis.

