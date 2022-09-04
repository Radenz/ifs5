# Simulated Annealing

*Simulated Annealing* adalah algoritma yang menggabungkan hill climbing search (efisien) dengan *random walk* (komplit). Simulated annealing tidak memilih pergerakan yang terbaik, tetapi memilih pergerakan *random*. Jika pergerakan tersebut menghasilkan state yang lebih baik, maka akan selalu diterima. Jika tidak, algoritma tersebut akan menerima pergerakan dengan suatu probabilitas kurang dari 1. Probabilitas ini berkurang secara eksponensial berdasarkan "*badness*" pergerakan, besarnya $\Delta E$ yang memperburuk evaluasi. Probabilitas tersebut juga berkurang seiring menurunnya "temperatur" $T$: pergerakan yang buruk lebih mungkin untuk diperbolehkan di awal ketika nilai $T$ tinggi, dan semakin jarang diperbolehkan seiring menurunnya $T$. Simulated annealing merupakan versi stochastic hill climbing search dengan beberapa pergerakan *downhill* diperbolehkan.

Berikut adalah pseudocode algoritma simulated annealing.
```
function SIMULATED-ANNEALING(problem, schedule) returns a solution state
	current <- problem.INITIAL
	for t = 1 to ∞ do
		T <- schedule(t)
		if T = 0 then return current
		// Stochastic hill climbing search
		next <- a randomly selected successor of current
		ΔE <- VALUE(current) - VALUE(next)
		if ΔE > 0 then current <- next
		else current <- next only with probability e^(-ΔE/T)
```
