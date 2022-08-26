# List produk toko
ListProduk = [
    {'no'       : '001',
     'nama'     : 'adidas',
     'harga'    : '1200000',
     'stock'    : '7'
     },
    {'no'       : '002',
     'nama'     : 'nike',
     'harga'    : '1500000',
     'stock'    : '4'
     },
    {'no'       : '003',
     'nama'     : 'puma',
     'harga'    : '800000',
     'stock'    : '15'
     },
]

# Function menu utama
def main_menu():
    while True:
        menu_utama = input('''\n
    ---------------------------------------------------
                       SELAMAT DATANG
                DI SISTEM GUDANG SEPATU JAYA
    ---------------------------------------------------
    Pilih menu berikut ini :
    1. Lihat Daftar Sepatu        4. Hapus Data Sepatu
    2. Tambah Sepatu              5. Sistem Selesai
    3. Update Data Sepatu
    ---------------------------------------------------
    Ketik angka menu : ''')

        if(menu_utama == '1'):
            daftar_sepatu()
        elif(menu_utama == '2'):
            tambah_stock()
        elif(menu_utama == '3'):
            update_produk()
        elif(menu_utama == '4'):
            hapus_produk()
        elif(menu_utama == '5'):
            print('''\n
    ----------------------
         Terima Kasih
         Sampai Jumpa
    ----------------------''')
            break

# Function Menu1 (Daftar Sepatu) / READ DATA
def daftar_sepatu():
    while True:
        menu_daftar_sepatu = input('''\n
    -------------------------
       LIHAT DAFTAR SEPATU
    -------------------------
    Pilih menu berikut ini :
    1. Daftar seluruh sepatu
    2. Lihat sepatu tertentu
    0. Kembali ke menu utama
    -------------------------
    Ketik angka menu: ''')
        if(menu_daftar_sepatu == '1'):
            daftar_sepatu_semua()
        elif(menu_daftar_sepatu == '2'):
            daftar_sepatu_tertentu()
        elif(menu_daftar_sepatu == '0'):
            break
        else:
            input_salah()

# Function Pendukung Menu1
def daftar_sepatu_semua():
    print('''\n
    -----------------------------------------
                 DAFTAR SEPATU
    -----------------------------------------
    Kode| Nama\t\t| Stock\t| Harga
    ''')
    if not ListProduk:
        tidak_ada_data()
    else:
        for i in range(len(ListProduk)):
            print('    {}\t|{}\t\t|{}\t|Rp {}'.format(ListProduk[i]['no'],ListProduk[i]['nama'],ListProduk[i]['stock'],ListProduk[i]['harga']))
        print('    -----------------------------------------')

def daftar_sepatu_tertentu():
    print('''\n
    ------------------
    DAFTAR NAMA SEPATU
    ------------------
    Kode|Nama Sepatu''')
    for i in range(len(ListProduk)):
        print('     {}  |{}'.format(ListProduk[i]['no'],ListProduk[i]['nama']))
    print('    ------------------')

    InputSepatu = input_no_sepatu()
    PilihSepatu = filter_data(InputSepatu)
    if not PilihSepatu:
        tidak_ada_data()
    else:
        info_sepatu(PilihSepatu)

# Function Menu2 (Tambah Stock) / CREATE DATA
def tambah_stock():
    while True:
        menu_tambah_stock = input('''\n
    ------------------------
       TAMBAH DATA SEPATU
    ------------------------
    Pilih menu berikut ini :
    1. Tambah data sepatu
    0. Kembali ke menu utama
    ------------------------
    Ketik angka menu: ''')
        if(menu_tambah_stock == '1'):
            tambah_stock_sepatu()
        elif(menu_tambah_stock == '0'):
            break
        else:
            input_salah()

# Function Pendukung Menu2
def tambah_stock_sepatu():
    InputSepatu = input_no_sepatu()
    PilihSepatu = filter_data(InputSepatu)
    InputNamaSepatu = input_nama_sepatu()
    FilterNamaSepatu = filter_nama_sepatu(InputNamaSepatu)

    if PilihSepatu:
        print('\n    ----Data Sudah Ada----')
    elif FilterNamaSepatu:
        print('\n    ----Data Sudah Ada----')
    else:
        while True:
          try:
            HargaSepatu = int(input('    Masukkan harga sepatu (hanya angka): '))
            break
          except:
            input_salah(); print()
        while True:
          try:
            StockSepatu = int(input('    Masukkan stock sepatu (hanya angka): '))
            break
          except:
            input_salah();print()
        while True:
            Inputkonfirmasi = input('    Apakah data akan disimpan? (Y/N): ').lower()
            if(Inputkonfirmasi == 'y'):
                ListProduk.append(
                    {'no' : InputSepatu,
                     'nama' : InputNamaSepatu,
                     'harga' : HargaSepatu,
                     'stock' : StockSepatu})
                print('\n    ----Data Tersimpan----')
                break
            elif(Inputkonfirmasi == 'n'):
                print('\n    ----Data tidak tersimpan----')
                break
            else:
                input_salah()

# Function Menu3 (Update Produk) / UPDATE DATA
def update_produk():
    while True:
        menu_update_produk = input('''\n
    ------------------------
       UPDATE DATA SEPATU
    ------------------------
    Pilih menu berikut ini :
    1. Update data sepatu
    0. Kembali ke menu utama
    ------------------------
    Ketik angka menu: ''')
        if(menu_update_produk == '1'):
            update_produk_sepatu()
        elif(menu_update_produk == '0'):
            break
        else:
            input_salah()

# Function Pendukung Menu3 
def update_produk_sepatu():
    daftar_sepatu_semua()
    InputSepatu = input_no_sepatu()
    PilihSepatu = filter_data(InputSepatu)

    if not PilihSepatu:
        tidak_ada_data()
    else:
        info_sepatu(PilihSepatu)
        ProdukIndex = -1
        for i in PilihSepatu:
            ProdukIndex = ListProduk.index(i)

        while True:
            InputKonfirmasi = input('\n    Apakah data akan diubah? (Y/N): ').lower()
            if(InputKonfirmasi == 'y'):
                while True:
                    InputUpdateProduk = input('    Tulis bagian yang akan diubah (stock/harga): ').lower()
                    if(InputUpdateProduk == 'stock' or InputUpdateProduk == 'harga'):
                      break
                    else:
                      input_salah(); print()
                BagianUpdate = any(InputUpdateProduk in i for i in ListProduk)
                if(BagianUpdate):
                    InputDataBaru = input('    Masukkan {} baru:'.format(InputUpdateProduk.lower()))
                    while True:
                        KonfirmasiUpdate = input('    Anda yakin ingin diubah? (Y/N): ').lower()
                        if(KonfirmasiUpdate == 'y'):
                            ListProduk[ProdukIndex][InputUpdateProduk] = InputDataBaru
                            print('\n    ----Data Berhasil Diubah----')
                            break
                        elif(KonfirmasiUpdate =='n'):
                            print('\n    ----Data Tidak Berubah----')
                            break
                        else:
                            input_salah()
                else:
                    input_salah()
                break
            elif(InputKonfirmasi =='n'):
                break
            else:
                input_salah()

# Function Menu4 (Hapus Produk) / DELETE DATA
def hapus_produk():
    while True:
        menu_hapus_produk = input('''\n
    ------------------------
        HAPUS DATA SEPATU
    ------------------------
    Pilih menu berikut ini :
    1. Hapus Produk
    0. Kembali ke menu utama
    ------------------------
    Ketik angka menu: ''')

        if(menu_hapus_produk == '1'):
            hapus_produk_sepatu()
        elif(menu_hapus_produk == '0'):
            break
        else:
            input_salah()

# Function Pendukung Menu4
def hapus_produk_sepatu():
    daftar_sepatu_semua()
    InputSepatu = input_no_sepatu()
    PilihSepatu = filter_data(InputSepatu)

    if not PilihSepatu:
        tidak_ada_data()
    else:
        info_sepatu(PilihSepatu)
        while True:
            KonfirmasiUpdate = input('    Anda yakin ingin dihapus? (Y/N): ').lower()
            if(KonfirmasiUpdate =='y'):
                del ListProduk[next((index for (index, d) in enumerate(ListProduk) if d['no'] == InputSepatu), None)]
                print('\n    ----Data berhasil dihapus----')
                break
            elif(KonfirmasiUpdate =='n'):
                print('\n    ----Data Tidak Terhapus----')
                break
            else:
                input_salah()

# Function apabila input salah
def input_salah():
    print('\n    ----Maaf inputan anda salah----')

# Function Filter Data
def filter_data(InputSepatu):
    return list(filter(lambda x : x.get('no') == InputSepatu, ListProduk))

def filter_nama_sepatu(InputSepatu):
    return list(filter(lambda x : x.get('nama') == InputSepatu, ListProduk))

# Function Data Tidak Ada
def tidak_ada_data():
    print('\n    ----Data yang anda cari tidak ditemukan----')

# Function Input Sepatu
def input_no_sepatu():
    return input('    Masukkan kode sepatu: ')

def input_nama_sepatu():
    return input('    Masukkan nama sepatu: ').lower()

# Function Info Sepatu
def info_sepatu(PilihSepatu):
    print('''
    -----------------
       Info sepatu
    -----------------''')
    for i in PilihSepatu:
        print('    No    : {}\n    Nama  : {}\n    Harga : {}\n    stock : {}'.format(i['no'],i['nama'],i['harga'],i['stock']))


main_menu()
