
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
