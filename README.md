## Anggota Kelompok:
Daffa Ilham Restupratama - 2106751013 <br>
Dipa Alhaza - 2106751543 <br>
Griselda Neysa Sadiya - 2106751392 <br>
Pantun Elfreddy Sihombing - 2106751612 <br>
Rania Maharani Narendra - 2106650222 <br>

# Jejakarbon
Tautan aplikasi Heroku:  

🌏[Halaman Utama Jejakarbon](https://jejakarbon.herokuapp.com/)🌳

JejaKarbon adalah environmental web application dimana kita bisa melakukan donasi kepada perusahaan Go Green dan melakukan tracker carbon footprint yang dihasilkan oleh pengguna, khususnya tracker penggunaan transportasi. JejaKarbon akan mengembalikan jumlah perkiraan carbon footprint yang dihasilkan oleh pengguna.   

## Background
Carbon Footprint atau jejak karbon adalah jumlah emisi karbon dioksida yang berkaitan dengan aktivitas dari seseorang ataupun suatu objek seperti gedung, pabrik, kendaraan, dan sebagainya. Emisi tersebut adalah hasil dari pembakaran bahan bakar fosil di bidang manufaktur, pemanasan, dan transportasi. 

Banyak dampak yang muncul karena carbon footprint, seperti perubahan iklim yang bisa mengarah ke pemanasan global, polusi udara, hujan asam, mencairnya es di kutub, dan pengasaman pesisir serta laut. Jadi, emisi karbon ini sangat berdampak bagi lingkungan kita.

Tanpa kita sadari, hampir semua aktivitas yang kita lakukan menghasilkan carbon footprint, terutama dalam transportasi. menurut data dari EPA (United States Environmental Protection Agency), penyumbang terbesar dari emisi karbon dioksida pada tahun 2020 adalah sektor transportasi. Indonesia sendiri merupakan salah satu negara dengan jumlah kendaraan bermotor terbanyak di dunia. 

Untuk mengurangi dampak dari Carbon Footprint,  kita harus bekerja sama saling mengurangi Carbon Footprint yang kita hasilkan. Dengan itu, kelompok kami memilih tema carbon footprint. 

## Manfaat Aplikasi
Dengan adanya JejaKarbon, diharapkan:
- Pengguna bisa mengetahui jumlah carbon footprint mereka, hal ini dilakukan untuk meningkatkan awareness sebanyak apa carbon footprint yang telah dihasilkan dari penggunaan transportasi sehari-hari pengguna.
- Pengguna bisa melakukan donasi, membantu perusahaan penggerak go green untuk menghijaukan lingkungan.

## Modul yang akan diimplementasikan dalam Jejakarbon
1) Halaman utama, Halaman login/logout, Register, faq (**Rania Maharani Narendra**)
- About JejaKarbon
- Daftar frequently asked question (get)
- form faq (post)
2) Halaman input data transportasi dan perhitungan carbon footprint (**Griselda Neysa Sadiya**)
- Form input data transportasi (post)
- Perhitungan carbon footprint 
- Status penghasilan carbon footprint (get)
3) Halaman progres akun pengguna (**Daffa Ilham Restupratama**)
- Profile user (get)
- Edit profile (post)
- Status penghasilan carbon footprint (get) => dari input data transportasi
- Daftar donasi yang telah dilakukan (get) => dari form ikut donasi/pembayaran
4) Halaman penambahan project (**Dipa Alhaza**)
- Form pembukaan donasi (post)
- Daftar seluruh donasi yang terdaftar (get)
5) Halaman form ikut donasi/pembayaran (**Pantun Elfreddy Sihombing**)
- Form mengikuti donasi (post)
- Daftar donasi yang telah dilakukan user (get)

## Role Pengguna dalam JejaKarbon
1) User nonlogin:
- Membuat akun
- melihat faq
- Melihat daftar donasi
2) User login pribadi:
- Sama seperti user nonlogin (kecuali membuat akun)
- Melakukan donasi
- bertanya pada faq
- Melihat progress akun/membuka profile
- Melakukan input data transportasi dan mendapatkan data carbon footprint  
3) User login Organisasi:
- Membuka donasi
- Melihat daftar donasi
- melihat faq dan bertanya
- Melihat progress akun/membuka profile
4) Admin:
- menjawab faq
- sama seperti user login kecuali bertanya pada faq

Sumber Pendukung:
[Why Is a Carbon Footprint Bad for the Environment? All You Need to Know](https://impactful.ninja/why-is-a-carbon-footprint-bad-for-the-environment/#:~:text=Our%20carbon%20footprint%20has%20a,of%20glaciers%20and%20polar%20ice)
