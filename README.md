# Postest2
By Naura Syawal Athallah Putri 
#### NIM: 2390116032

## Nama Program
#### Japaneses Snack and Ramen Shop

## Flowchart
![Postest 2 drawio](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/6ba210b5-abed-42a3-ba64-c7cd748b290d)


# Penjelasan Ouput Program
## Menu Login
Menu login bagi user. User dapat memilih untuk login sebagai admin atau cutomer. Jika user login sebbagai admin, maka user harus memasukkan password yang benar, jika tidak user tidak akan bisa login sebagai admin dan akan looping pada menu pilihan login. Juka user masuk sebagai customer, maka user akan langsung diarahkan ke menu customer.

![login](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/8bb4bd2d-ec69-4f50-8e78-23b6da7a3111)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 4_59_16 AM](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/ae3e970a-ad85-4777-b735-0ba178afcd84)

## Untuk menampilkan tabel 
Berikut untuk meampikan tabel. List tabel disimpan di dalam database yang nantinya akan ditampilkan melalui function display_tabel.
![tabel](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/3e483a22-5d08-4f79-8805-557e92bb6e10)
![CodeSnap 📸 - UTS - Visual Studio Code 10_10_2023 5_07_09 AM](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/7c169ae6-6c27-484c-9e15-3c727e4bf9cf)

## Menampilkan Menu Customer
Menu bagi user yag login sebagai customer. User akan diberikan 2 pilihan, takni untuk membeli produk atau keluar dari program. Jika user input angka 1, maka user akan diarahkan ke bagian pembelian produk. Jika userinput angka 2, maka program akan berhenti. Jika user input selain keduanya, program akan looping pada bagian menu customer.
![menu cust](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/b46f3197-dbcf-4e62-ac62-399f0d71e100)

## Membeli produk
User akan diperlihatkan tabel yang berisi produk-produ yang ditawarkan. Setelah itu user bisa menginput nomor ndex tabel untuk memilih produk mana yang akan user beli. Jika user input nomor index yang tidak sesuai dengan yang ada di dalam tabel, maka akan muncul ouput "Nomor produk tidak valid" . Setelah user input nomor index, user harus meng-input berapa banyak produk yang user ingin beli. Apabila user menginput jumlah produk yang melebihi stok tyang tersedia, maka akan muncul ouput "Stok kurang". 

Setelah user input jumlah produk yang ingin dibeli, maka program otomatis akan mengurangi stok yang tersedia dengan jumlah produk yang user belih. Program akan looping sampai user input "q" sebagai tanda penyelesaian pembelian. Setelah itu akan muncul tampilan checkout dengan harga total dari produk yang telah user beli sebelumnya.

![beli p](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/ace9fbfb-060a-4a27-b75d-3e7a01846f90)
![CodeSnap 📸 - UTS - Visual Studio Code 10_10_2023 5_23_32 AM](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/fb6f333e-b59a-4357-933d-0e0c9444e48f)

## Menu Admin
Menu bagi user yang login sebagai admin. User akan diberikan 5 pilihan, yakni menambah produk pada tabel, melihat tabel, mengubah data produk yang ada di dalam tabel, menghapus produk, serta keluar dari program
![login amdn](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/ce517c2b-cd6e-4b86-89b6-da5986a20ca3)

## Menambah Produk
User akan diperlihatkan tabel produk dan disuruh untuk inout index tabel sebagai tempat dimana produk tersebut akan ditambah. User kemudian harus memasukkan nama produk, deskripsi singkat, harga, serta jumlah stok dari produk yang tersedia. Setelahnya akan diperlihatkan tabel yang telah diperbaharui.

Apabila user input data yang tidak sesuai dengan tipe data yang diinginkan, maka akan muncul ouput "Mohon masukkan tipe data yang sesuai" dan user akan dibawa kmbali ke  program awal.

![tamba p](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/11e469b3-c518-4358-9e61-61cacf0f90e4)
![tmbh](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/34cd6032-2b65-47fd-8282-38c875d51f1f)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 6_18_09 AM](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/d6470c85-35bd-4fc4-811e-d838598a1f00)

## Melihat Produk
Pada bagian ini, user juga dapat melihat tabel yang telah diperbaharui
![tabel](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/672afd26-e559-4ebe-bd8c-30d6e4ae5fab)
![see](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/a515ca98-9011-49ad-ae18-d6709bfe2e15)

## Update Produk
User akan diperlihatkan tabel produk dan disuruh untuk input index tabel sebagai tempat dimana produk tersebut akan diganti. User kemudian harus memasukkan nama produk, deskripsi singkat, harga, serta jumlah stok dari produk yang tersedia. Setelahnya akan diperlihatkan tabel yang telah diperbaharui.

Apabila user input data yang tidak sesuai dengan tipe data yang diinginkan, maka akan muncul ouput "Mohon masukkan tipe data yang sesuai" dan user akan dibawa kmbali ke  program awal.

![cange p](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/c59d784c-ef0e-4eda-a34c-8144431e3b9c)
![ap](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/e235f23b-639a-4d56-b5e7-991ed133867d)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 6_26_36 AM](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/c30ffcb5-e180-4b8d-a0fe-6b2cbf6d7209)


## Hapus Produk
User akan diperlihatkan tabel produk dan disuruh untuk input index tabel yang ingin dihapus. Setelahnya akan diperlihatkan tabel yang telah diperbaharui. User akan diberikan opsi untuk melanjutkan penghapusan. Jikan input Y, maka user dapat kembali menghapus tabel tersebut. Jika input selain Y, maka user akan kembali pada tamilan menu admin.

Apabila user input index tabel yang tidak sesuai dengan index tabel yang tersedia, maka akan muncu ouput "Nomor produk tidak valid"

![delet p](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/52f413a5-5951-4f1e-98fd-c477bccf8b8a)
![delet](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/346c28d0-d58f-47e4-a881-bf88a5a335df)
![postest_2 py - UTS - Visual Studio Code 10_10_2023 6_29_20 AM](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/38726fd1-6f97-49ff-8f79-87785b94f3af)


## Exit Program
User dapat keluar dari program

![exit](https://github.com/NauraSyawaAthallahPutri/PostTest2/assets/144810430/df74bb88-c01a-4ffa-9e61-f136b39ef16f)





