# Postest2
By Naura Syawal Athallah Putri 
#### NIM: 2390116032

## Nama Program
#### Japaneses Snack and Ramen Shop

## Flowchart
![Postest 2 drawio](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/27049384-1636-4c8d-bd88-a8322e85c96f)

# Penjelasan Ouput Program
## Menu Login
Menu login bagi user. User dapat memilih untuk login sebagai admin atau cutomer. Jika user login sebbagai admin, maka user harus memasukkan password yang benar, jika tidak user tidak akan bisa login sebagai admin dan akan looping pada menu pilihan login. Juka user masuk sebagai customer, maka user akan langsung diarahkan ke menu customer.
![login](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/d5e1c254-524c-4f11-8b68-de2f2bb9c7cd)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 4_59_16 AM](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/053e9651-bd55-45cf-a1f8-b5cdc5b079b9)

## Untuk menampilkan tabel 
Berikut untuk meampikan tabel. List tabel disimpan di dalam database yang nantinya akan ditampilkan melalui function display_tabel.
![tabel](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/b0c8214d-fc09-4179-8ef7-f95c07ed904c)
![CodeSnap 📸 - UTS - Visual Studio Code 10_10_2023 5_07_09 AM](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/8dae7c96-db67-4103-953f-249de84e33f5)

## Menampilkan Menu Customer
Menu bagi user yag login sebagai customer. User akan diberikan 2 pilihan, takni untuk membeli produk atau keluar dari program. Jika user input angka 1, maka user akan diarahkan ke bagian pembelian produk. Jika userinput angka 2, maka program akan berhenti. Jika user input selain keduanya, program akan looping pada bagian menu customer.
![menu cust](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/b647fdad-b675-4df7-892f-9b58964bc48e)

## Membeli produk
User akan diperlihatkan tabel yang berisi produk-produ yang ditawarkan. Setelah itu user bisa menginput nomor ndex tabel untuk memilih produk mana yang akan user beli. Jika user input nomor index yang tidak sesuai dengan yang ada di dalam tabel, maka akan muncul ouput "Nomor produk tidak valid" . Setelah user input nomor index, user harus meng-input berapa banyak produk yang user ingin beli. Apabila user menginput jumlah produk yang melebihi stok tyang tersedia, maka akan muncul ouput "Stok kurang". 

Setelah user input jumlah produk yang ingin dibeli, maka program otomatis akan mengurangi stok yang tersedia dengan jumlah produk yang user belih. Program akan looping sampai user input "q" sebagai tanda penyelesaian pembelian. Setelah itu akan muncul tampilan checkout dengan harga total dari produk yang telah user beli sebelumnya.

![beli p](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/4cbc17d0-a1b6-4cb1-9c7b-afff56d54be5)
![CodeSnap 📸 - UTS - Visual Studio Code 10_10_2023 5_23_32 AM](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/b733dcb2-6de5-491c-a143-b7847fe59f2d)

## Menu Admin
Menu bagi user yang login sebagai admin. User akan diberikan 5 pilihan, yakni menambah produk pada tabel, melihat tabel, mengubah data produk yang ada di dalam tabel, menghapus produk, serta keluar dari program
![login amdn](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/e63d70a3-6b10-49ef-99e5-45d34876bdf4)

## Menambah Produk
User akan diperlihatkan tabel produk dan disuruh untuk inout index tabel sebagai tempat dimana produk tersebut akan ditambah. User kemudian harus memasukkan nama produk, deskripsi singkat, harga, serta jumlah stok dari produk yang tersedia. Setelahnya akan diperlihatkan tabel yang telah diperbaharui
![tamba p](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/caf69b7d-e79d-4f10-93d9-582a5ebe7962)
![tmbh](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/6dbe10c1-3fad-4c5d-8e26-8d02948bb47c)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 6_18_09 AM](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/a4263551-f104-4e3c-83f5-0412755425b4)

## Melihat Produk
Pada bagia ini, user juga dapat melihat tabel yang telah diperbaharui
![tabel](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/97a3ffab-797f-4df9-83f4-6bd26a4b98eb)
![see](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/6b76f93d-0331-44c1-b836-e244c376a12b)

## Update Produk
User akan diperlihatkan tabel produk dan disuruh untuk input index tabel sebagai tempat dimana produk tersebut akan diganti. User kemudian harus memasukkan nama produk, deskripsi singkat, harga, serta jumlah stok dari produk yang tersedia. Setelahnya akan diperlihatkan tabel yang telah diperbaharui
![cange p](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/7c84f06a-323f-47d5-bc8d-b4e8705c2c54)
![ap](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/1046dbc0-35d6-42fa-bcdb-646876773610)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 6_26_36 AM](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/7c3ab210-c93e-4224-a09e-0d5f591453a3)


## Hapus Produk
User akan diperlihatkan tabel produk dan disuruh untuk input index tabel yang ingin dihapus. Setelahnya akan diperlihatkan tabel yang telah diperbaharui. User akan diberikan opsi untuk melanjutkan penghapusan. Jikan input Y, maka user dapat kembali menghapus tabel tersebut. Jika input selain Y, maka user akan kembali pada tamilan menu admin
![delet p](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/d9e921e8-e535-4b5c-8009-ef9a1bf0f0c0)
![delet](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/e4344dc3-fa4f-49f9-8b93-5d819a25fa96)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 6_29_20 AM](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/ac354c0e-39f4-4676-9c5b-502aa7b6b6f3)

## Exit Program
User dapat keluar dari program
![exit](https://github.com/NauraSyawaAthallahPutri/Postest2/assets/144810430/070748d8-f71b-42b9-9f00-b6aa1840c0a4)




