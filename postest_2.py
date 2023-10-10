#Import prettytable
from prettytable import PrettyTable 
#Agar tampilan lebih bersih
import os
os.system ('cls')

#Display Nama Toko
print("============= Japanese's Snack and Ramen Shop =============")
print('ATTENTION!: Ramen yang disediakan merupakan ramen instan yang disajikan dengan sistem self-service dan produk yang sudah dipilih tidak bisa di cancel')
print('-------------------------------------------------------------------------------------------------------------------------------------------------------')

#Password untuk login admin
pw_admin = 'gueadmin'

#Database produk
produk = [
    ['Nissin Kyushu Black', 'Ramen dengan garlic flavour dan kuah dengan campuran minyak wijen ', 15000, 10], 
    ['Myojo CharMee 100', 'Ramen pedas dengan kaldu dari perpaduan ikan, udang, kacang, wijen serta susu', 12000, 10], 
    ['Nissin Kyushu White', 'Ramen kuah putih dengan perpaduan rasa kaldu ayam dan seafood', 45000, 5],
    ['Nissin Takoyaki ','Ramen dengan saus manis dan dengan sedikit aroma bonito dan rasa rumput laut', 40000, 10],
    ['Gekikara Hot Chicken','Ramen dengan rasa ekstra pedas dan resep rasa ayam pedas special', 42000, 10],
    ['Nissin Kari', 'Dengan kuah kari khas Jepang dan mie lurus kenyal ala Jepang', 40000, 13],
    ['Takoyaki', 'Bola-bola kecil dari adonan tepung terigu berisi potongan gurita di dalamnya (1 porsi isi 10)', 35000, 10],
    ['Dorayaki', 'Terdiri dari dua pancake yang lembut dan manis yang diisi dengan selai kacang merah', 20000, 15],
    ['Onigiri', 'Nasi kepal berbentuk segitiga dengan isian Tuna Mayo', 10000 , 10],
    ['Dango', 'Bola-bola kecil dari tepung beras yang ditusuk bambu dan dibalut dengan saus Tare (1 porsi isi 3)', 6000, 10],
    ['Mochi', 'Kue bulat dari beras ketan yang kenyal dengan isian selai stroberi, matcha, dan tebu hitam (1 porsi isi 6)', 8000, 10],
    ['Matcha Tea', 'Teh hijau yang menenangkan khas Jepang', 13000, 20],
] 

# Function untuk display produk di tabel
def display_tabel ():
    tabel_produk = PrettyTable()
    tabel_produk.field_names =["Nama Produk", "Desc", "Harga", "Jumlah Tersedia"]
    
    #Untuk menunjukkan data yang sudah dimasukkan ke dalam tabel
    for item in produk:
        tabel_produk.add_row(item)
    print(tabel_produk)

# Variabel universal untuk keranjang
keranjang = []

# Function untuk display pembelian (snack)
def beli_produk(keranjang, produk):
    while True:
        
        # Untuk memilih produk yang mau dibeli
        beli = input('Masukkan nomor produk yang ingin Anda beli (ketik q untuk berhenti): ')
        
        if beli == 'q':
            break # Berhenti looping jika input q
        try:
            # Untuk meng-convert variabel beli menjadi integer
            beli = int(beli)
            
            # Untuk memeriksa apakah nomor produk yang dimasukkan ada di dalam tabel
            if 0 <= beli < len(produk):
                produk_yang_dibeli = produk[beli]
                nama_produk, desc, harga, jumlah = produk_yang_dibeli
                
                # Input banyak produk yang ingin kit beli
                jumlah_beli = int(input(f'Masukkan jumlah produk yang ingin anda beli (stok {nama_produk} sisa {jumlah}): '))

                # Untuk memeriksa dan memperbarui jumlah stok yang tersedia
                if 1 <= jumlah_beli <= jumlah:
                    keranjang.append([nama_produk, harga, jumlah_beli])
                    produk[beli][3] -= jumlah_beli  
                else:
                    print("Stok kurang")
            
            else:
                print("Nomor produk tidak valid.")
        
        except ValueError:
            print("Masukkan nomor produk yang ada di tabel.")

# Halaman Login
while True:
    print('1. Login sebagai customer')
    print('2. Login sebagai admin')
    login = int(input('Pilih menu login: '))
    
    if login == 1:
        break #Berhenti looping jika masuk sebagai customer
    
    elif login == 2:
        # pw = input('Masukkan Password Admin: ')
        # if pw == pw_admin:
        #     print("Semangat kerja min :v")
            break  #Berhenti looping jika password benar
        # else:
        #     print("Salah pw lo min")

#------------------------------------ Customer -----------------------------------
# Pilihan menu bagi customer
if login == 1:
    while True:
        print('---Menu pembelian---')
        print('1. Beli produk')
        print('2. Exit')
        pilih = int(input('Pilih yang anda inginkan: '))

        #Jika memilih untuk beli produk
        if pilih == 1:
            display_tabel()
            beli_produk(keranjang, produk)
            
            #Menampilkan total harga dari barang yang kita beli
            print('----- Checkout -----')
            harga_total = sum([produk[1] * produk[2] for produk in keranjang])
            print(f'Total Harga: Rp {harga_total}')
            print('Enjoy the food!')
            
        # Keluar dari program
        elif pilih == 2:
            break

#------------------------------------- Admin -------------------------------------
# Function untuk menambah produk
def tambah_produk():
    display_tabel()
    
    try:
        tambah = int(input("Masukkan nomor tabel sebagai tempat produk ingin Anda tambah (ketik q untuk batal): "))
        nama_produk = input("Masukkan nama produk: ")
        desc = input("Masukkan deskripsi singkat produk: ")
        harga = int(input("Masukkan harga produk: "))
        jumlah_stok = int(input("Masukkan stok yang tersedia: "))
        
        produk_baru = nama_produk, desc, harga, jumlah_stok
        produk.insert(tambah, produk_baru)
        
    except ValueError:
        print("Tolong masukkan tipe data yang sesuai")

# Function untuk mengganti produk
def ganti_produk():
    display_tabel()
    
    try:
        ganti = int(input("Masukkan nomor produk yang ingin Anda update: "))
        nama_produk = input("Masukkan nama produk: ")
        desc = input("Masukkan deskripsi singkat produk: ")
        harga = int(input("Masukkan harga produk: "))
        jumlah_stok = int(input("Masukkan stok yang tersedia: "))
        
        produk[ganti]= [nama_produk, desc, harga, jumlah_stok]
    
    except ValueError:
        print("Tolong masukkan  tipe data yang sesuai")
    
# Function untuk meghapus produk dari tabel
def hapus_produk():
    display_tabel() 
    try:
        hapus = int(input("Masukkan nomor produk yang ingin Anda hapus: "))
        
        # Mengecek apakah nomor produk pada tabel valid
        if 0 <= hapus < len(produk):
            print(f"{produk.pop(hapus)} telah dihapus")
        else:
            print("Nomor produk tidak valid.")
            
    except ValueError:
        print("Masukkan nomor produk yang valid.")

# Pilihan menu sebagai admin
if login == 2:
    while True:
        #Pilihan menu  admin
        print('---Mau ngapain nih min?---')
        print('1. Tambah produk')
        print('2. Lihat produk')
        print('3. Update produk')
        print('4. Hapus produk')
        print('5. Exit')
        pilih = int(input('Pilih yang anda inginkan: '))
        
        #Jika memilih untuk menambah Produk
        if pilih == 1:
            tambah_produk()
            display_tabel()
        
        # Jika memilih untuk melihat produk
        elif pilih == 2:
            display_tabel()
            
        # Jika memilih untuk mengupdate produk
        elif pilih == 3:
            ganti_produk()
            display_tabel()
        
        #Jika Memilih untuk menghapus produk
        elif pilih == 4:
            while True:
                hapus_produk()
                display_tabel()
                hapus_lagi = input('Apakah anda ingin menghapus lagi? (Ketik Y jika iya): ')
                if hapus_lagi != 'Y':
                    break
                
        elif pilih == 5:
            break