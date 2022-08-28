# Intelligent Agent

> **Quick links**
> - [Edunex](https://edunex.itb.ac.id/courses/43590/preview/100865/42971)
> 	- [Slide](https://cdn-edunex.itb.ac.id/31964-Artificial-Intelligence-[General-Class]/24042-Minggu-1/7077-Introduction-to-AI/1629533226011_IF3170_AI-Introduction.pdf)

## Agent
Agent adalah suatu entitas yang bisa dikatakan **menangkap persepsi dari lingkungan** melalui **sensor** (**sensors**) dan **melakukan aksi ke lingkungan** berdasarkan hasil persepsi tadi melalui **aktuator** (**actuators**). Agent bisa dikatakan sebagai agen komputasional yang bertindak secara *autonomous*.  
Contoh agent adalah sebagai berikut.  
- Human agent  
	Sensor : mata, hidung, telinga  
	Aktuator : tangan, kaki
- Rubic solver robot agent  
	Sensor : kamera yang menagkap warna pada sisi Rubik's cube  
	Aktuator : motor-motor penggerak pemutar kubus

## Agent Model
Untuk memodelkan agent, perlu dimodelkan komponen-komponen berikut.
### 1. Percept Space
Ruang *percept* adalah kumpulan persepsi/kondisi/state yang bisa ditangkap oleh agent melalui sensor yang dirancang ada dalam agent.
### 2. Action Space
Ruang aksi adalah kumpulan aksi yang dapat dilakukan agent untuk mencapai tujuannya.
### 3. Internal State
Internal state atau kondisi internal adalah state dalam program atau di dalam proses berpikir agen yang menentukan apakah goal sudah tercapai atau belum.
### 4. Perception Function: $S \rightarrow P$ 
>$S: State$<br>$P: Percept$

Fungsi persepsi adalah fungsi yang memetakan state ke dalam suatu kondisi yang bisa ditangkap oleh agen.
### 5. World Dynamics: $S \times A \rightarrow S$
>$S: State$<br>$A: Action$

Dinamika dunia agen fungsi yang menentukan apakah state lingkungan berubah atau tetap jika pada suatu lingkungan dilakukan aksi tertentu.

#### Contoh: Vacuum-cleaner World
Agent vacuum cleaner dapat dimodelkan sebagai berikut.
- Percept Space  
	*Percept* yang ditangkap agent tersebut adalah lokasi dan keadaan ruangan, misalnya dituliskan dengan $[A, dirty]$ sehingga *percept space* dari agent tersebut adalah semua kemungkinannya.
- Action space  
	Aksi yang dapat dilakukan oleh agent tersebut adalah sebagai berikut.
	
	>$Left$ - bergerak ke kiri  
	$Right$ - bergerak ke kanan  
	$Suck$ - sedot debu  
	$NoOp$ - tidak melakukan apapun  
- Internal State  
	(State internal mungkin berbeda-beda bergantung pada cara agent berpikir.)
- Perception Function  
	Kondisi banyak kotoran dalam suatu ruangan direpresentasikan sebagai state $X$, sedangkan ruangan yang bersih direpresentasikan sebagai state $Y$. Tujuan agent adalah mendapatkan ruangan dengan state $Y$.
- World Dynamics  
	Jika pada state $X$ (ada kotoran di ruangan) agent melakukan aksi $Suck$ (sedot debu), maka state yang di-*percept* oleh agent berikutnya adalah $Y$ karena ruangan menjadi bersih.

## Agent Design
Untuk menilai rancangan agen, perlu angka kualitas untuk menentukan seberapa baik agen yang kita rancang.
### Utility Function ($U$)
>$U: S \rightarrow \mathbb{R}$<br>$U: S^* \rightarrow \mathbb{R}$<br>$S: State$<br>$S^* : State\ Sequence$<br>$\mathbb{R}: real$

Fungsi utilitas adalah fungsi yang memetakan suatu state ke bilangan real tertentu atau *sequence state* ke suatu bilangan tertentu. Misalnya pada model vacuum cleaner state dipetakan sebagai berikut.

>$X \rightarrow 0$<br>$Y \rightarrow 100$
### Problem: Temukan $P^* \rightarrow A$
>$P^* : Percept\ Sequence$<br>$A: Action$

Secara keseluruhan, yang diinginkan adalah agent bisa memilih aksi yang benar sehingga *sequence percept* yang ditangkap oleh agent menyebabkan $U$ pada akhirnya maksimal. Caranya dari pemetaan $P^* \rightarrow A$, kita harus bisa mengatur agar aksi yang dipilih oleh agent memaksimalkan *sequence state*. Karena $S \times A \rightarrow S$, nilai dari *sequence state* dimaksimalkan.

## Rational Agent
Untuk menilai bahwa agent sukses dalam melakukan aksinya, perlu didefinisikan **performance measure**. Untuk setiap *sequence percept* yang mungkin dan bekal pengetahuan '*knowledge*', rational agent harus dapat melakukan aksi yang tepat yang dapat memaksimalkan pengukuran kinerja.
### Rationality
Rational agent akan memilih aksi yang diyakininya akan membawa agent mencapai goal yang diharapkan. Sebagai contoh, jika seseorang tidak ingin basah maka:
1. Jika orang tersebut melihat prakiraan cuaca yang ternyata tidak akan hujan, maka membawa payung adalah aksi yang tidak rasional.
2. Jika orang tersebut tidak melihat prakiraan cuaca, maka membawa payung adalah aksi yang rasional.

Rasional **bukan** berarti **mahatahu** '*omniscience*', contohnya jika pada poin (2) ternyata ramalan cuaca adalah tidak akan hujan. Rasional juga **bukan** berarti **sukses**, contohnya jika orang tersebut sukses menghindari digigit anjing dengan payung, padahal payung digunakan untuk menghindari hujan.
### Limited Rationality
Agent mungkin tidak bisa melakukan komputasi untuk memliih aksi terbaik karena keterbatasan komputasi, maka rasionalitas agent terbatas pada batasan komputasi. Maka, pemilihan aksi untuk mendapatkan *sequence state* yang memiliki $U$ maksimal **terbatas** pada **kemampuan komputasi** yang dimiliki agent.