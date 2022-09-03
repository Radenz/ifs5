
# Rational Agent

## PEAS Description
Ada 4 hal yang harus diperhatikan saat merancang rational agent, yang disebut dengan **P E A S**.
1. **P**erformance Measure  
	*Performance measure* adalah pengukuran kinerja untuk menilai apakah agent yang dibangun sudah bekerja dengan baik atau belum.
2. **E**nvirontment  
	*Environtment* adalah lingkungan di mana agent akan ditempatkan.
3. **A**ctuators  
	*Actuators* adalah bagian dari agent yang bisa melakukan aksi dan berdampak pada lingkungan.
4. **S**ensors  
	*Sensors* adalah bagian dari agent yang bertugas untuk menangkap persepsi dari lingkungan.

#### Contoh: Automated Taxi Driver
Dalam agent pengemudi taksi otomatis, **P E A S** dideskripsikan sebagai berikut.
1. Performance measure
	- Keamanan mengemudi
	- Kecepatan sampai di tempat tujuan
	- Tidak melanggar peraturan lalu lintas
	- Perjalanan yang nyaman bagi penumpang
	- Keuntungan yang didapat maksimal
2. Environtment
	- Jalan (jalanan lurus, belok, perempatan, dsb.)
	- Kendaraan lain yang ada di sekitarnya
	- Pejalan kaki
	- Penumpang
3. Actuators
	- Kemudi (untuk menentukan arah kendaraan)
	- Pedal gas
	- Rem
	- Tuas (untuk mengaktifkan lampu sen)
	- Klakson.
4. Sensors
	- Kamera
	- Sonar
	- Speedometer
	- GPS
	- Odometer (penunjuk jarak yang telah ditempuh)
	- Sensor dalam mesin
	- Keyboard (untuk memberikan umpan balik bagi penumpang kepada agent)

## Task Environtment
Berikut adalah sifat-sifat lingkungan tugas.

### 1. Fully vs Partially Observable
Lingkungan tugas dikatakan *fully observable* jika sensor-sensor pada agen dapat mendeteksi semua aspek yang relevan dengan pilihan aksi, dengan relevansi bergantung pada ukuran kinerja (performance measure) agen. Contoh lingkungan yang *fully observable* adalah lingkungan agen permainan catur.

Sebaliknya, lingkungan tugas dikatakan *partially observable* jika hanya ada sebagian state lingkungan yang dapat ditangkap oleh agen. Contoh lingkungan yang *partially observable* adalah lingkungan agen permainan poker karena state dari kartu lawan tidak diketahui.

### 2. Deterministic vs Non-deterministic
Jika state lingkungan selanjutnya sepenuhnya ditentukan oleh state saat ini dan aksi yang dieksekusi oleh agen―artinya state saat ini sepenuhnya ditentukan oleh state dan aksi yang dieksekusi sebelumnya―maka lingkungan tugas dikatakan *deterministic*, jika tidak, maka lingkungan dikatakan *non-deterministic*. Contoh dari lingkungan yang *deterministic* adalah lingkungan agen permainan catur, sedangkan contoh dari lingkungan *non-deterministic* adalah agen pengemudi taksi.

### 3. Episodic vs Sequential
Pada lingkungan *episodic*, pengalaman agen dibagi menjadi "episode-episode" atomik. Artinya, episode selanjutnya tidak bergantung pada aksi yang dilakukan pada episode sebelumnya. Sebagai contoh, agen penentu penyebab sakit kepala tidak mempertimbangkan penyebab sakit kepala pasien sebelumnya untuk menentukan penyebab sakit kepala pasien saat ini.  
Pada lingkungan *sequential*, keputusan saat ini dapat berpengaruh pada keputusan-keputusan selanjutnya. Sebagai contoh, pada permainan catur, aksi yang dilakukan oleh agen saat ini akan berpengaruh pada keputusan/aksi selanjutnya.

### 4. Static vs Dynamic
Jika lingkungan dapat berubah ketika agen sedang mempertimbangkan aksinya (berpikir), maka lingkungan disebut *dynamic*; jika tidak, maka lingkungan disebut *static*. Jika lingkungan tidak berubah seiring waktu tetapi skor performa agen berubah, maka lingkungan tersebut dikatakan *semidynamic*. Sebagai contoh, lingkungan agen permainan catur adalah lingkungan *static*, sedangkan lingkungan agen pengemudi taksi adalah lingkungan *dynamic* karena taksi tersebut dan kendaraan lain tetap bergerak ketika agen sedang mempertimbangkan aksinya. Akan tetapi, lingkungan agen permainan catur yang diberi waktu adalah lingkungan *semidynamic* karena skor performa agen dipengaruhi oleh waktu.

### 5. Discrete vs Continuous
Perbedaan antara *discrete* dan *continuous* berlaku pada state lingkungan, bagaimana waktu ditangani, dan *percept* dan aksi agen. Misalnya, lingkungan agen permainan catur memiliki state yang terbatas dan kumpulan *percept* dan aksi yang diskrit sehingga lingkungan tersebut adalah *discrete*. Di sisi lain, lingkungan agen pengemudi taksi memiliki stat yang kontinu dan waktu yang kontinu―kecepatan dan lokasi taksi dan kendaraan lain berubah pada nilai yang kontinu secara kontinu―sehingga lingkungan tersebut adalah *continuous*.

### 6. Single-Agent vs Multiagent
Pada lingkungan *single-agent*, perubahan state hanya bergantung pada agen yang melakukan aksi. Pada lingkungan *multiagent*, perubahan state lingkungan juga dipengaruhi oleh aksi agen yang lain.
>*Lingkungan single-agent berarti lingkungan yang di dalamnya hanya terdapat satu agen saja, sedangkan lingkungan multiagent adalah lingkungan yang di dalamnya memuat agen lain atau entitas dan objek lain yang adapat dianggap sebagai agen. Entitas/objek yang dimaksud adalah entitas/objek yang perilakunya seperti memaksimumkan performance measure tertentu yang nilainya bergantung pada agen yang menjadi perhatian*.

Contoh lingkungan single-agent adalah lingkungan agen *Rubik's cube solver*, sedangkan contoh lingkungan multiagent adalah lingkungan agen permainan poker.

### Known vs Unknown
Perbedaan antara *known* dan *unknown* sebenarnya tidak merujuk pada lingkungan, tetapi pengetahuan agen tentang "hukum fisis" pada lingkungan. Pada lingkungan yang *known*, luaran (atau probabilitas setiap luaran untuk lingkungan *non-deterministic*) untuk setiap aksi telah diberikan. Contoh dari lingkungan yang *known* adalah permainan kartu solitaire.

Pada lingkungan yang *unknown*, agen harus mempelajari bagaimana cara kerja lingkungan untuk mengambil keputusan yang terbaik. Contoh dari lingkungan yang *unknown* adalah lingkungan *video game* terbaru.

## Agent Structure
Secara garis besar, struktur agen terdiri atas **architecture** dan **program**. *Architecture* menyatakan perangkat komputasi yang dilengkapi dengan sensor dan actuator. *Program* adalah mekanisme pada agen yang menerima kumpulan *percept* yang ditangkap oleh sensor dan mengembalikan aksi yang akan dilakukan oleh aktuator.  
Ada 5 jenis dasar program agen yang mewujudkan prinsip-prinsip yang mendasari hampir semua sistem cerdas.
1. Simple reflex agents  
	Simple reflex agents langsung menghasilkan aksi berdasarkan *percept* dari kumpulan *rule* yang sudah didefinisikan.
2. Model-based reflex agents
	Model-based reflex agents bisa membentuk model lingkungan ketika agen berhadapan dengan lingkungan yang *partially observable* sehingga bisa menentukan aksi yang tepat.
3. Goal-based agents
	Pemilihan aksi goal-based agents tidak hanya berdasarkan kondisi lingkungan saat itu, namun juga mempertimbangkan informasi *goal* agar aksi yang dipilih makin mendekatkan agen ke *goal*.
4. Utility-based agents
	Utility-based agents merupakan perbaikan dari *goal-based agents* ketika ada beberapa pilihan aksi yang mendekatkan agen ke *goal*, yaitu dengan memilih aksi yang memiliki nilai utilitas lebih baik.
5. Learning agents
	Learning agents adalah program agen yang mampu memperbaiki kinerjanya seiring waktu berdasarkan pengalaman yang disimpan.

## Agent Level
### Level 1: Problem Solving Agent
*Problem solving agent* memliki informasi semua state persoalan yang bisa ditangkap oleh agen dan semua aksi yang bisa dipilih untuk mencapai tujuan sudah diberikan. Tugas agen adalah melakukan pencarian aksi apa yang harus dilakukan agar agen mencapai *goal*.

### Level 2: Knowledge Based Agent
*Knowledge based agent* tidak memliki informasi semua state persoalan yang ada, tetapi hanya memliki *basic knowledge*/*premises*. Agen ini memanfaatkan pengetahuan dasar yang diberikan untuk melakukan penalaran untuk mendapatkan fakta atau state yang baru.

### Level 3: Learning Agent
*Learning agent* tidak memliki informasi semua state persoalan yang ada ataupun *basic knowledge*. Agent hanya diberikan kumpulan data observasi beberapa waktu. Berdasarkan kumpulan data yang diberikan, agen harus dapat membentuk pengetahuan dasar, kemudian menyelesaikan persoalan dengan pengetahuan dasar yang telah dibentuk.  
Berdasarkan jenis ketersediaan data dan umpan balik yang diperoleh agen, terdapat 3 jenis pembelajaran.
1. Supervised learning: ada data hasil observasi dan keputusan atau nilai yang dicari dari setiap data yang ada.
2. Unsupervised learning: ada data hasil observasi, tetapi tidak ada kelas dari setiap data yang ada.
3. Reinforcement learning: tidak ada data hasil obervasi, agen harus berupaya mencari sendiri dengan melakukan aksi berulang kali dan berusaha membentuk *policy* aksi yang seharusnya dilakukan pada suatu keadaan atau state tertentu.