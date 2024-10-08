<details>
<summary> Tahap 1 </summary>

## Kelompok : BO4

### i. Anggota Kelompok

1. Sayyid Thariq Gilang Muttaqien (2306275714)
2. Rizki Amani Hasanah (2306213376)
3. Andi Muhammad Adlyn Fakhreyza Khairi Putra (2306241713)
4. Dara Zakya Apriani (2306165906)
5. Rama Aditya Rifki Harmono (2306165502)
6. Salomo Immanuel Putra (2306219745)

 ### ii. Deskripsi Aplikasi

__Nama Aplikasi: Jakarta Wardrobe (JaWa)__ 

Jakarta Wardrobe (JaWa) adalah sebuah aplikasi informasi yang menyediakan data lengkap mengenai produk fashion yang tersedia di berbagai toko di wilayah Jakarta. Aplikasi ini bukanlah sebuah *platform* berbelanja *online*, melainkan sebuah wadah informasi yang memudahkan pengguna, baik warga Jakarta maupun pendatang, untuk menemukan dan mengeksplorasi produk fashion, seperti celana, baju, dress, sepatu, dan lainnya. Kategori yang disediakan di antaranya adalah *women’s clothing*, *men’s clothing*, dan *footwear*. 

Keberadaan aplikasi JaWa diharapkan dapat membantu pengguna untuk mengakses dan mendapatkan informasi setiap produk yang dicari, termasuk deskripsi, detail produk, ulasan, dan lokasi toko yang menjual produk tersebut. Aplikasi ini dilengkapi dengan berbagai fitur menarik, seperti *rating* dan *comment* yang akan tersedia pada laman ulasan, memungkinkan pengguna memberikan penilaian serta ulasan terhadap produk, sehingga dapat membantu pengguna lain dalam mengambil keputusan yang lebih terinformasi. Selain itu, pengguna juga dapat menyimpan produk favorit mereka ke dalam halaman khusus yang disebut *User Choice*, di mana mereka dapat dengan mudah mengakses kembali produk-produk yang mereka sukai di masa mendatang. Selain fitur-fitur diatasm JaWa juga menyediakan fitur *categories* yang mengelompokkan produk berdasarkan jenis fashion, serta modul filter location, yang memungkinkan pengguna menyaring produk berdasarkan lokasi toko, sehingga mereka dapat menemukan produk fashion yang tersedia di daerah terdekat. 

__Kebermanfaatan Aplikasi:__ 

1. __Memberikan informasi yang komprehensif__ tentang produk fashion di Jakarta, sehingga pengguna dapat dengan mudah menemukan produk yang  dicari.
2. __Membantu pengguna memilih produk berdasarkan lokasi serta rating dan ulasan__ yang diberikan oleh pengguna lain, meningkatkan pengalaman eksplorasi.
3. __Menawarkan fitur personalisasi__ melalui fitur *User Choice*, yang memungkinkan pengguna menyimpan produk favorit mereka untuk referensi di masa mendatang.
4. __Mempermudah pencarian produk__ dengan fitur filter berdasarkan jenis fashion, nama produk (*alphabetical*), dan lokasi toko.
5. __Mendorong interaksi komunitas__ melalui fitur komentar dan ulasan, di mana pengguna dapat berbagi pengalaman mereka mengenai produk tertentu. 

Dengan fitur-fitur ini, Jakarta Wardrobe menjadi solusi efektif bagi pengguna yang ingin mengetahui ketersediaan produk fashion di Jakarta sebelum mengunjungi toko, sehingga dapat menghemat waktu dan memastikan produk yang diinginkan tersedia. Aplikasi ini menyediakan informasi yang berguna bagi para warga Jakarta maupun pengunjung untuk merencanakan pembelian produk dengan lebih efisien.


### iii. Daftar Modul

1. #### *Rating (Review Page)* 

Modul ini bertanggung jawab untuk menyimpan dan menampilkan rating setiap produk. Rating diberikan dalam bentuk angka dengan range 1 sampai 5 yang disimpan sebagai atribut rating_value dalam tabel. Pada impleemntasinya, modul ini akan mengumpulkan dan menghitung rata-rata rating dari semua pengguna untuk setiap produk.

#### *Attributes*:
- id: Primary Key \
- product_id: Foreign Key yang terhubung ke tabel Produk \
- user_id: Foreign Key yang terhubung ke tabel Pengguna \
- rating_value: Integer yang menyimpan nilai rating (1–5) \
- timestamp: Timestamp untuk merekam waktu pemberian rating 

2. #### *Comment (Review Page)* 

Modul ini bertanggung jawab dalam menyimpan komentar yang diberikan oleh pengguna pada setiap produk. Setiap komentar dihubungkan dengan produk dan pengguna melalui product_id dan user_id. Modul ini memungkinkan penyimpanan komentar dalam bentuk teks (comment_text), dengan waktu pembuatan disimpan dalam timestamp. Implementasi comment dan rating akan dijadikan satu dalam review page.

#### *Attributes*:
- id: Primary Key \
- product_id: Foreign Key yang mengacu pada tabel Produk \
- user_id: Foreign Key yang mengacu pada tabel Pengguna \
- comment_text: Text yang menyimpan isi komentar \
- timestamp: Timestamp untuk waktu pemberian komentar 

3. #### *Edit Profile* 

Modul ini disusun untuk mengelola data profil pengguna yang dapat diedit secara individual. Setiap profil pengguna memiliki atribut seperti username, profile_image, dan email. Modul ini menyimpan perubahan data pengguna dalam tabel User, memungkinkan pengguna untuk memperbarui informasi personal mereka secara *real-time*.

#### *Attributes*:
- id: Primary Key \
- username: String untuk menyimpan nama pengguna \
- profile_image: URL atau path untuk menyimpan lokasi gambar profil pengguna \
- email: String untuk alamat email pengguna \
- date_joined: Timestamp untuk menyimpan tanggal bergabung pengguna 

4. #### *User Choice* 

Modul ini memungkinkan setiap pengguna untuk memiliki halaman personal yang menampilkan barang-barang yang mereka masukkan ke dalam daftar favorit, disebut sebagai *User Choice*. Modul ini menyimpan pilihan produk berdasarkan preferensi pengguna, yang akan ditampilkan secara khusus pada halaman tersebut. Setiap produk favorit dihubungkan dengan pengguna melalui user_id dan disimpan dalam bentuk daftar produk yang telah ditambahkan ke dalam pilihan mereka.

#### *Attributes*:
- id: Primary Key \
- user_id: Foreign Key yang terhubung ke pengguna tertentu \
- favorite_products: Array atau relasi *Many-to-Many* ke tabel Produk yang menyimpan daftar produk favorit pengguna 


5. #### *Categories* 
	
Modul ini mengelompokkan produk berdasarkan kategori tertentu. Setiap produk terkait dengan satu kategori melalui category_id, yang memungkinkan pengelompokan produk dan penelusuran lebih mudah. Kategori yang tersedia tercantum dalam tabel *Categories*.

#### *Attributes*:
- category_id: Primary Key \
- category_name: String untuk nama kategori, misalnya “Tops”, "Bottoms", "Dress", "Footwear" \
- description: Text untuk deskripsi kategori \
- Produk Attributes: product_id, category_id untuk menghubungkan produk dengan kategori 

6. #### *Location (Filter)* 

Modul ini menyaring produk berdasarkan lokasi yang relevan. Setiap produk memiliki atribut lokasi seperti __city__ dan __district__, memungkinkan pengguna untuk menyaring daftar produk berdasarkan lokasi yang lebih ter-filter di Jakarta.

#### *Attributes:*
- id: Primary Key \
- product_id: Foreign Key yang terhubung ke tabel Produk \
- city: String yang menyimpan kota \
- district: String yang menyimpan kecamatan \
- location_name: Nama lokasi toko yang menjual produk \
- latitude: Float untuk posisi lintang toko \
- longitude: Float untuk posisi bujur toko 

### iv. Sumber initial dataset kategori utama produk



### v. Role atau Peran Pengguna

1. *Rating* \
Pengguna dapat melihat dan memberikan rating untuk produk.

2. *Comment* \
Pengguna dapat melihat dan memberikan komentar untuk produk.

3. *Edit Profile* \
Pengguna dapat menyunting profil pengguna, seperti ID, nama, dan gambar pengguna.

4. *User Choice* \
Pengguna dapat menyesuaikan preferensi mereka untuk menyesuaikan konten dan pengalaman di website agar lebih interaktif dan personal.

5. *Categories* \
Dalam fitur ini pengguna dapat mengelompokkan produk ke dalam kategori-kategori tertentu.

6. *Location (Filter)* \
Dalam fitur ini pengguna dapat menyaring produk berdasarkan lokasi pengguna.


### vi. Tautan Deployment

[http://sayyid-thariq31-jawaapp.pbp.cs.ui.ac.id/]

</details>
