class Dagangan:
    total_barang = 0
    daftar_barang = []

    def __init__(self, nama_barang, stok_barang, harga_barang):
        self.__nama_barang = nama_barang
        self.__stok_barang = stok_barang
        self.__harga_barang = harga_barang
        Dagangan.total_barang += 1
        Dagangan.daftar_barang.append((self.__nama_barang, self.__stok_barang, self.__harga_barang))

    @staticmethod
    def tampilkan_daftar_barang():
        print("Jumlah barang dagangan pada toko:", Dagangan.total_barang, "buah")
        for idx, barang in enumerate(Dagangan.daftar_barang, start=1):
            nama, stok, harga = barang
            print(f"{idx}. {nama} seharga Rp {harga} (stok: {stok})")

    def __del__(self):
        Dagangan.total_barang -= 1
        for barang in Dagangan.daftar_barang:
            if barang[0] == self.__nama_barang:
                Dagangan.daftar_barang.remove(barang)
                print(f"{self.__nama_barang} dihapus dari toko!")
                break


# Contoh penggunaan
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.tampilkan_daftar_barang()

del Dagangan1
Dagangan.tampilkan_daftar_barang()
