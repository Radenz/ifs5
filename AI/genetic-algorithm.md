# Genetic Algorithm

## Local Beam Search
*Local Beam Search* adalah algoritma yang serupa dengan random restart hill climbing search, tetapi menyimpan $k$ state dari pada hanya 1 state. Local beam search dimulai dengan men-generate $k$ state secara random dan pada setiap langkah, semua successor dari $k$ state tersebut di-generate. Jika salah satunya ada yang merupakan goal, maka algoritma dihentikan. Jika tidak, pilih $k$ state successor terbaik dari seluruh successor dan ulangi algoritma yang diterapkan.

## Stochastic Beam Search
Karena pada dasarnya local beam search mencari $k$ state successor terbaik, maka pencarian yang dilakukan masih cukup lambat sehingga ada varian lain yang disebut dengan *stochastic beam search*. Berbeda dengan local beam search, stochastic beam search tidak mencari $k$ state successor yang terbaik, tetapi memilih $k$ state random.

## Genetic Algorithm
*Genetic Algorithm* merupakan varian dari stochastic beam search dengan successor state didapatkan dari kombinasi 2 *parent state*. Dalam algoritma ini, state direpresentasikan sebagai string alfabet *finite* (sering kali string boolean). Dalam string ini, satu karakter menyatakan satu variabel. Sebagai contoh, dalam *N-Queens Problem*, state dapat dinyatakan sebagai string 8 karater yang masing-masing karakternya menyatakan posisi baris queen.

### Fitness Function
Dalam genetic algorithm, state value disebut dengan *fitness function*. Sebagai contoh, pada N-Queens Problem, fitness function dinyatakan dengan banyaknya pasangan queen yang tidak saling menyerang, sehingga memiliki nilai:
- minimum = $0$
- maximum = $(8 \times 7)/2$ = $28$

### Initial Population
Genetic algorithm dimulai dengan menginisialisasi populasi yang terdiri atas $k$ state random.

### Successor Function
Successor state pada genetic algorithm merupakan populasi generasi berikutnya yang dihasilkan dengan operator seleksi, *crossover*, dan mutasi.

Berikut adalah pseudocode dari genetic algorithm.
```
function GENETIC-ALGORITHM(population, fitness) returns an individual
	repeat
		weights <- WEIGHTED-BY(population, fitness)
		population2 <- empty list
		for i = 1 to SIZE(population) do
			parent1, parent2 <- WEIGHTED-RANDOM-CHOICES(population, weights, 2)
			child <- REPRODUCE(parent1, parent2)
			if (small random probability) then child <- MUTATE(child)
			add child to population2
		population <- population2
	until some individuals is fit enough, or enough time has elapsed
	return the best individual in population, according to fitness

function REPRODUCE(parent1, parent2) returns an individual
	n <- LENGTH(parent1)
	c <- random number from 1 to n
	return APPEND(SUBSTRING(parent1, 1, c), SUBSTRING(parent2, c + 1, n))
```