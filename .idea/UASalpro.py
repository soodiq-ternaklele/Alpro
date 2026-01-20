import heapq
import os
from collections import Counter, defaultdict
import sys

class Node:
    #Kelas Node untuk Huffman Tree dan Binary Search Tree
    def __init__(self, data=None, freq=None):
        self.data = data
        self.freq = freq

        self.value = data

        self.left = None
        self.right = None
        self.parent = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

class HuffmanCoding:
    #Kelas untuk implementasi Huffman Coding

    def __init__(self):
        self.codes = {}
        self.reverse_codes = {}
        self.heap = []

    def build_heap(self, freq_dict):
        #Membangun heap dari frekuensi karakter
        for char, freq in freq_dict.items():
            node = Node(char, freq)
            heapq.heappush(self.heap, node)

    def build_tree(self):
        #Membangun Huffman Tree dari heap
        while len(self.heap) > 1:
            # Ambil dua node dengan frekuensi terkecil
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            # Gabungkan menjadi node baru
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            # Tambahkan ke heap
            heapq.heappush(self.heap, merged)

    def build_codes_helper(self, root, current_code):
        #Fungsi rekursif untuk membuat kode Huffman
        if root is None:
            return

        # Jika node adalah leaf node (memiliki karakter)
        if root.data is not None:
            self.codes[root.data] = current_code
            self.reverse_codes[current_code] = root.data
            return

        # Traverse ke kiri dan kanan
        self.build_codes_helper(root.left, current_code + "0")
        self.build_codes_helper(root.right, current_code + "1")

    def build_codes(self):
        #Membangun kode Huffman dari Huffman Tree
        root = heapq.heappop(self.heap)
        current_code = ""
        self.build_codes_helper(root, current_code)

    def encode(self, text):
        #Mengenkripsi teks menggunakan kode Huffman
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def decode(self, encoded_text):
        #Mendekripsi teks yang telah dienkripsi
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_codes:
                decoded_text += self.reverse_codes[current_code]
                current_code = ""

        return decoded_text

    def compress(self, text):
        #Kompresi teks menggunakan Huffman Coding
        # Hitung frekuensi karakter
        freq_dict = Counter(text)

        # Bangun heap, tree, dan kode
        self.build_heap(freq_dict)
        self.build_tree()
        self.build_codes()

        # Encode teks
        encoded_text = self.encode(text)

        return encoded_text, self.codes, freq_dict

class BinarySearchTree:
    #Kelas untuk implementasi Binary Search Tree

    def __init__(self):
        self.root = None

    def insert(self, value):
        #Menyisipkan nilai ke dalam BST
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def search(self, value):
        #Mencari nilai dalam BST#
        current = self.root
        path = []

        while current is not None:
            path.append(current.value)
            if value == current.value:
                return current, path
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return None, path

    def find_min(self, node):
        #Mencari nilai minimum dari subtree
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        #Menghapus nilai dari BST
        node_to_delete, _ = self.search(value)

        if node_to_delete is None:
            return False

        # Kasus 1: Node tidak memiliki anak
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete == self.root:
                self.root = None
            elif node_to_delete == node_to_delete.parent.left:
                node_to_delete.parent.left = None
            else:
                node_to_delete.parent.right = None

        # Kasus 2: Node memiliki satu anak
        elif node_to_delete.left is None:
            child = node_to_delete.right
            self._transplant(node_to_delete, child)
        elif node_to_delete.right is None:
            child = node_to_delete.left
            self._transplant(node_to_delete, child)

        # Kasus 3: Node memiliki dua anak
        else:
            successor = self.find_min(node_to_delete.right)

            if successor.parent != node_to_delete:
                self._transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor

            self._transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor

        return True

    def _transplant(self, u, v):
        #Mengganti subtree u dengan subtree v
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def inorder(self, node, result=None):
        #Traversal inorder (kiri, root, kanan)
        if result is None:
            result = []

        if node is not None:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)

        return result

    def preorder(self, node, result=None):
        #Traversal preorder (root, kiri, kanan)
        if result is None:
            result = []

        if node is not None:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

        return result

    def postorder(self, node, result=None):
        #Traversal postorder (kiri, kanan, root)
        if result is None:
            result = []

        if node is not None:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)

        return result

    def display_tree(self, node=None, level=0, prefix="Root:"):
        #Menampilkan struktur tree secara visual
        if node is None:
            node = self.root
            if node is None:
                print("Pohon kosong")
                return

        if level == 0:
            print(f"{prefix} {node.value}")
        else:
            print(" " * (level * 4) + f"└── {node.value}")

        if node.left is not None or node.right is not None:
            if node.left is not None:
                self.display_tree(node.left, level + 1)
            else:
                print(" " * ((level + 1) * 4) + "└── (Kiri: Kosong)")

            if node.right is not None:
                self.display_tree(node.right, level + 1)
            else:
                print(" " * ((level + 1) * 4) + "└── (Kanan: Kosong)")

def huffman_coding_demo():
    #Demo interaktif untuk Huffman Coding
    print("\n" + "="*60)
    print("HUFFMAN CODING DEMO")
    print("="*60)

    # Input teks dari user
    text = input("Masukkan teks yang akan dikompresi: ")

    if not text:
        print("Teks tidak boleh kosong!")
        return

    # Buat objek Huffman Coding
    huffman = HuffmanCoding()

    # Kompresi teks
    encoded_text, codes, freq_dict = huffman.compress(text)

    # Hitung statistik
    original_size = len(text) * 8  # dalam bit (asumsi 8 bit per karakter)
    compressed_size = len(encoded_text)
    compression_ratio = (1 - compressed_size / original_size) * 100

    # Tampilkan hasil
    print("\n" + "-"*60)
    print("HASIL KOMPRESI HUFFMAN CODING")
    print("-"*60)

    print(f"\nTeks asli: '{text}'")
    print(f"Panjang teks asli: {len(text)} karakter")
    print(f"Ukuran asli: {original_size} bit")

    print(f"\nFrekuensi karakter:")
    for char, freq in sorted(freq_dict.items()):
        print(f"  '{char}': {freq} kali")

    print(f"\nKode Huffman untuk setiap karakter:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")

    print(f"\nTeks terenkripsi: {encoded_text}")
    print(f"Panjang teks terenkripsi: {compressed_size} bit")
    print(f"Rasio kompresi: {compression_ratio:.2f}%")

    # Dekompresi
    decoded_text = huffman.decode(encoded_text)
    print(f"\nTeks terdekripsi: '{decoded_text}'")

    # Verifikasi
    if text == decoded_text:
        print("✓ Kompresi dan dekompresi berhasil!")
    else:
        print("✗ Terjadi kesalahan dalam kompresi/dekompresi")

    input("\nTekan Enter untuk kembali ke menu utama...")

def binary_search_tree_demo():
    #Demo interaktif untuk Binary Search Tree
    print("\n" + "="*60)
    print("BINARY SEARCH TREE DEMO")
    print("="*60)

    # Buat BST
    bst = BinarySearchTree()

    while True:
        print("\n" + "-"*60)
        print("MENU BINARY SEARCH TREE")
        print("-"*60)
        print("1. Tambah node ke BST")
        print("2. Cari node dalam BST")
        print("3. Hapus node dari BST")
        print("4. Tampilkan traversal")
        print("5. Tampilkan struktur tree")
        print("6. Contoh BST otomatis")
        print("7. Kembali ke menu utama")

        choice = input("\nPilih opsi (1-7): ")

        if choice == "1":
            # Tambah node
            try:
                value = int(input("Masukkan nilai integer yang akan ditambahkan: "))
                bst.insert(value)
                print(f"Node dengan nilai {value} berhasil ditambahkan.")
            except ValueError:
                print("Masukkan harus berupa integer!")

        elif choice == "2":
            # Cari node
            try:
                value = int(input("Masukkan nilai integer yang akan dicari: "))
                node, path = bst.search(value)

                if node is not None:
                    print(f"Node dengan nilai {value} DITEMUKAN dalam BST.")
                    print(f"  Jalur pencarian: {' -> '.join(map(str, path))}")
                else:
                    print(f"Node dengan nilai {value} TIDAK DITEMUKAN dalam BST.")
                    print(f"  Jalur pencarian: {' -> '.join(map(str, path))}")
            except ValueError:
                print("Masukkan harus berupa integer!")

        elif choice == "3":
            # Hapus node
            try:
                value = int(input("Masukkan nilai integer yang akan dihapus: "))
                if bst.delete(value):
                    print(f"Node dengan nilai {value} berhasil dihapus.")
                else:
                    print(f"Node dengan nilai {value} tidak ditemukan dalam BST.")
            except ValueError:
                print("Masukkan harus berupa integer!")

        elif choice == "4":
            # Tampilkan traversal
            if bst.root is None:
                print("BST masih kosong!")
            else:
                print("\nTraversal BST:")
                print(f"InOrder (terurut): {bst.inorder(bst.root)}")
                print(f"PreOrder: {bst.preorder(bst.root)}")
                print(f"PostOrder: {bst.postorder(bst.root)}")

        elif choice == "5":
            # Tampilkan struktur tree
            print("\nStruktur Binary Search Tree:")
            bst.display_tree()

        elif choice == "6":
            # Contoh otomatis
            example_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
            bst = BinarySearchTree()

            for value in example_values:
                bst.insert(value)

            print(f"✓ BST contoh telah dibuat dengan nilai: {example_values}")
            print("\nTraversal BST contoh:")
            print(f"InOrder (terurut): {bst.inorder(bst.root)}")
            print(f"PreOrder: {bst.preorder(bst.root)}")
            print(f"PostOrder: {bst.postorder(bst.root)}")

            print("\nStruktur BST contoh:")
            bst.display_tree()

        elif choice == "7":
            # Kembali ke menu utama
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1-7.")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            input("\nTekan Enter untuk melanjutkan...")

def main():
    #Fungsi utama program
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n" + "="*60)
        print("PROJECT UAS ALGORITMA PEMROGRAMAN")
        print("="*60)
        print("Dibuat oleh Kelompok kami")
        print("Anggota:")
        print("1. Muhammad Aditya Wibawa 202410370110407")
        print("2. Sadaika nursadiq (202410370110398)")
        print("3. Alvin nur fajrianto(202410370110419)")
        print("4. Syahlevi Miraz Nugraha(202410370110425)")
        print("\nProgram mengimplementasikan 2 studi kasus:")
        print("1. Huffman Coding")
        print("2. Binary Search Tree dengan Traversal")
        print("="*60)

        print("\nMENU UTAMA")
        print("1. Huffman Coding - Kompresi Teks")
        print("2. Binary Search Tree - Operasi dan Traversal")
        print("3. Tentang Program")
        print("4. Keluar")

        choice = input("\nPilih studi kasus (1-4): ")

        if choice == "1":
            huffman_coding_demo()
        elif choice == "2":
            binary_search_tree_demo()
        elif choice == "3":
            print("\n" + "="*60)
            print("TENTANG PROGRAM")
            print("="*60)
            print("\nProgram ini dibuat untuk memenuhi tugas Project UAS")
            print("Mata Kuliah: Algoritma Pemrograman")
            print("\nFitur yang diimplementasikan:")
            print("1. HUFFMAN CODING")
            print("   - Kompresi dan dekompresi teks")
            print("   - Menghitung frekuensi karakter")
            print("   - Membangun kode Huffman")
            print("   - Menampilkan rasio kompresi")
            print("\n2. BINARY SEARCH TREE")
            print("   - Insert, search, delete node")
            print("   - Traversal: InOrder, PreOrder, PostOrder")
            print("   - Visualisasi struktur tree")
            print("\nProgram ini bersifat interaktif dengan input dari user.")
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif choice == "4":
            print("\nTerima kasih telah menggunakan program ini!")
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-4.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()