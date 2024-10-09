<details>
<summary> Tahap 1 </summary>

## Anggota Kelompok B04

1. Sayyid Thariq Gilang Muttaqien (2306275714)
2. Rizki Amani Hasanah (2306213376)
3. Andi Muhammad Adlyn Fakhreyza Khairi Putra (2306241713)
4. Dara Zakya Apriani (2306165906)
5. Rama Aditya Rifki Harmono (2306165502)
6. Salomo Immanuel Putra (2306219745)

 ## Jakarta Wardrobe (JaWa)

Jakarta Wardrobe (JaWa) adalah sebuah aplikasi informasi yang menyediakan data lengkap mengenai produk fashion yang tersedia di berbagai toko di wilayah Jakarta. Aplikasi ini bukanlah sebuah platform berbelanja *online*, melainkan sebuah wadah informasi yang memudahkan pengguna, baik warga Jakarta maupun pendatang, untuk menemukan dan mengeksplorasi produk fashion, seperti celana, baju, dress, sepatu, dan lainnya. Kategori yang disediakan di antaranya adalah *women’s clothing*, *men’s clothing*, dan *footwear*. 

Keberadaan aplikasi JaWa diharapkan dapat membantu pengguna untuk mengakses dan mendapatkan informasi setiap produk yang dicari, termasuk deskripsi, detail produk, ulasan, dan lokasi toko yang menjual produk tersebut. Aplikasi ini dilengkapi dengan berbagai fitur menarik, seperti __*rating*__ dan __*comment*__ yang akan tersedia pada laman ulasan, memungkinkan pengguna memberikan penilaian serta ulasan terhadap produk, sehingga dapat membantu pengguna lain dalam mengambil keputusan yang lebih terinformasi. Selain itu, pengguna juga dapat menyimpan produk favorit mereka ke dalam halaman khusus yang disebut __*User Choice*__, di mana mereka dapat dengan mudah mengakses kembali produk-produk yang mereka sukai di masa mendatang. Selain fitur-fitur diatasm JaWa juga menyediakan fitur __*Categories*__ yang mengelompokkan produk berdasarkan jenis fashion, serta modul filter __location__, yang memungkinkan pengguna menyaring produk berdasarkan lokasi toko, sehingga mereka dapat menemukan produk fashion yang tersedia di daerah terdekat. 

__Manfaat Aplikasi:__ 

1. __Memberikan informasi yang komprehensif__ tentang produk fashion di Jakarta, sehingga pengguna dapat dengan mudah menemukan produk yang  dicari.
2. __Membantu pengguna memilih produk berdasarkan lokasi serta rating dan ulasan__ yang diberikan oleh pengguna lain, meningkatkan pengalaman eksplorasi.
3. __Menawarkan fitur personalisasi__ melalui fitur __*User Choice*__, yang memungkinkan pengguna menyimpan produk favorit mereka untuk referensi di masa mendatang.
4. __Mempermudah pencarian produk__ dengan fitur filter berdasarkan jenis fashion, nama produk (*alphabetical*), dan lokasi toko.
5. __Mendorong interaksi komunitas__ melalui fitur komentar dan ulasan, di mana pengguna dapat berbagi pengalaman mereka mengenai produk tertentu. 

Dengan fitur-fitur ini, Jakarta Wardrobe menjadi solusi efektif bagi pengguna yang ingin mengetahui ketersediaan produk fashion di Jakarta sebelum mengunjungi toko, sehingga dapat menghemat waktu dan memastikan produk yang diinginkan tersedia. Aplikasi ini menyediakan informasi yang berguna bagi para warga Jakarta maupun pengunjung untuk merencanakan pembelian produk dengan lebih efisien.


## Daftar Modul

1. #### *Rating (Review Page)* 

Modul ini bertanggung jawab untuk menyimpan dan menampilkan rating setiap produk. Rating diberikan dalam bentuk angka dengan range 1 sampai 5 yang disimpan sebagai atribut rating_value dalam tabel. Pada impleemntasinya, modul ini akan mengumpulkan dan menghitung rata-rata rating dari semua pengguna untuk setiap produk.

#### *Attributes*:
- id: Primary Key 
- product_id: Foreign Key yang terhubung ke tabel Produk 
- user_id: Foreign Key yang terhubung ke tabel Pengguna 
- rating_value: Integer yang menyimpan nilai rating (1–5) 
- timestamp: Timestamp untuk merekam waktu pemberian rating 

2. #### *Comment (Review Page)* 

Modul ini bertanggung jawab dalam menyimpan komentar yang diberikan oleh pengguna pada setiap produk. Setiap komentar dihubungkan dengan produk dan pengguna melalui __product_id__ dan __user_id__. Modul ini memungkinkan penyimpanan komentar dalam bentuk teks (comment_text), dengan waktu pembuatan disimpan dalam timestamp. Implementasi comment dan rating akan dijadikan satu dalam review page.

#### *Attributes*:
- id: Primary Key 
- product_id: Foreign Key yang mengacu pada tabel Produk 
- user_id: Foreign Key yang mengacu pada tabel Pengguna 
- comment_text: Text yang menyimpan isi komentar 
- timestamp: Timestamp untuk waktu pemberian komentar 

3. #### *Edit Profile* 

Modul ini bertanggung jawab untuk mengelola fitur edit profile. Modul ini disusun untuk mengelola data profil pengguna yang dapat diedit secara individual. Setiap profil pengguna memiliki atribut seperti __username__, __profile_image__, dan __email__. Modul ini menyimpan perubahan data pengguna dalam tabel User, memungkinkan pengguna untuk memperbarui informasi personal mereka secara *real-time*.

#### *Attributes*:
- id: Primary Key 
- username: String untuk menyimpan nama pengguna 
- profile_image: URL atau path untuk menyimpan lokasi gambar profil pengguna 
- email: String untuk alamat email pengguna 
- date_joined: Timestamp untuk menyimpan tanggal bergabung pengguna 

4. #### *User Choice* 

Modul ini bertanggung jawab untuk mengelola fitur User Choice. Pengguna akan memiliki halaman personal yang menampilkan barang-barang yang mereka masukkan ke dalam daftar favorit, disebut sebagai __*User Choice*__. Modul ini menyimpan pilihan produk berdasarkan preferensi pengguna, yang akan ditampilkan secara khusus pada halaman tersebut. Setiap produk favorit dihubungkan dengan pengguna melalui __user_id__ dan disimpan dalam bentuk daftar produk yang telah ditambahkan ke dalam pilihan mereka.

#### *Attributes*:
- id: Primary Key 
- user_id: Foreign Key yang terhubung ke pengguna tertentu 
- favorite_products: Array atau relasi *Many-to-Many* ke tabel Produk yang menyimpan daftar produk favorit pengguna 


5. #### *Filter Categories & Location*

Modul ini bertanggung jawab untuk mengelompokkan dan menyaring produk berdasarkan kategori dan lokasi toko yang menjual setiap produk. Pengguna dapat memilih kategori produk yang mereka inginkan serta lokasi toko yang tersedia, sehingga hanya produk yang sesuai dengan preferensi tersebut yang akan ditampilkan. Setiap produk dihubungkan dengan kategori melalui __category_id__ dan dengan lokasi melalui __location_id__, yang memungkinkan pengelompokan dan penelusuran yang lebih terfokus.

#### *Attributes*:
- category_id: Primary Key untuk kategori
- category_name: String yang menyimpan nama kategori, misalnya “Women’s Clothing”, “Men’s Clothing”, “Footwear”.
- description: Text opsional untuk deskripsi kategori
- location_id: Primary Key untuk lokasi
- location_name: String untuk nama lokasi atau area toko
- Produk Attributes:
  1. product_id: Foreign Key yang menghubungkan ke produk tertentu
  2. category_id: Foreign Key untuk menghubungkan produk dengan kategori tertentu
  3. location_id: Foreign Key untuk menghubungkan produk dengan lokasi tertentu


6. #### *Global Chat* 

Modul ini menyediakan ruang komunitas bagi pengguna Jakarta Wardrobe (JaWa) untuk saling berinteraksi dan berdiskusi. Setiap pengguna dapat mengirim dan membaca pesan di ruang obrolan umum, di mana semua pengguna dapat berpartisipasi. Modul ini menyimpan pesan dalam bentuk teks, beserta informasi pengguna yang mengirim pesan dan waktu pengiriman, untuk membangun pengalaman komunitas yang aktif dan terbuka.

#### *Attributes*:
- id: Primary Key
- user_id: Foreign Key yang menghubungkan pesan dengan pengguna tertentu
- message_text: Text yang menyimpan isi pesan
- timestamp: Timestamp untuk merekam waktu pengiriman pesan


## Sumber Dataset
- __Nama Dataset__: Jakarta Wardrobe Product Dataset (JWP-dataset)

- __Link Sumber__: [JWP-Dataset](https://docs.google.com/spreadsheets/d/10Y80cMgyFb1CXp-TrQPabfEax1dL02Cxw_cFlwhmYKs/edit?usp=sharing)



- __Deskripsi Umum__:

Dataset ini menyediakan informasi mengenai produk fashion yang tersedia di sekitar Jakarta. Terdapat total 150 baris data, di mana setiap baris merepresentasikan satu produk. Tiap produk tergolong kedalam salah satu dari 5 kategori produk. Didalam dataset ini juga tersedia informasi terkait harga, stock, deskripsi, sumber gambar produk (dalam link url), serta nama dan lokasi toko dimana produk dijual. Dataset ini disusun berdasarkan data yang dikumpulkan dengan metode scraping pada 5 website toko berikut:

- __Referensi__:

1. [Parang Kencana](https://eshop.parangkencana.com/)
2. [Nayara](https://nayara.id/)
3. [Buttonscarves](https://www.buttonscarves.com/)
4. [thenblank](https://thenblank.com/) 
5. [THISISAPRIL](https://thisisapril.com/)

- __Catatan__: 

Beberapa produk mungkin memiliki deskripsi yang tidak lengkap dan format deskripsi antar produk yang diambil dari toko berbeda tidak seragam, serta harga dan stok yang tidak eksak.

- __Ukuran Dataset__:

1. Jumlah Baris: 150
2. Jumlah Kolom: 9

- __Format Data__: CSV

- __Deskripsi Kolom__:

1. category: Kategori produk.
2. nama: Nama produk.
3. price: Harga produk dalam rupiah pada saat data dikumpulkan.
4. stock: Jumlah ketersediaan produk.
5. desc: Deskripsi singkat tentang produk.

## Role atau Peran Pengguna

1. *Rating* \
Pengguna dapat melihat dan memberikan penilaian terhadap produk yang ditampilkan melalui fitur ini. 

2. *Comment* \
Pengguna dapat melihat dan meninggalkan komentar terkait suatu produk yang nantinya dapat dilihat oleh pengguna lain.

3. *Edit Profile* \
Pengguna dapat menyunting profil pengguna, seperti ID, nama, dan profile picture, dan informasi terkait akun mereka secara *real-time*. 

4. *User Choice* \
Pengguna dapat menyesuaikan preferensi mereka untuk menyesuaikan konten dan pengalaman di website agar lebih interaktif dan personal.

5. *Categories* \
Pengguna dapat memilih kategori produk yang mereka inginkan dan nantinya akan ditampilkan.

6. *Location (Filter)* \
Pengguna dapat menyaring daftar produk berdasarkan lokasi yang lebih ter-filter di Jakarta.


## Tautan Deployment

[http://sayyid-thariq31-jawaapp.pbp.cs.ui.ac.id/]

</details>
