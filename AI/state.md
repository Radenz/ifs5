# State: Value, Successor, and Neighbor

## State Value
Dalam local search, state merupakan konfigurasi lengkap atau semua variabelnya sudah diberi nilai. Setiap state dalam local search memiliki nilai heuristik atau cost ($h$). Sebagai contoh, dalam persoalan N-Queens, $h$ didefinisikan sebagai *negatif dari banyaknya pasangan queen yang saling menyerang satu sama lain, baik secara langsung maupun tidak langsung*<sup>[1]</sup>. Nilai negatif diberikan karena ini merupakan fungsi cost. Dengan demikian, state solusi dari personalan ini memilki nilai $h = 0$.

<sup>[1]</sup>"Tidak langsung" berarti queen bisa menyerang satu sama lain dengan *discovered attack*.

## Neigbor & Successor
Setelah mengetahui state value, local search mencari state terbaik yang memliki nilai global optimum dengan cara pindah ke *neighbor* yang lebih baik. Neighbor erat kaitannya dengan *successor*. Dalam persoalan N-Queens, neighbor dapat berupa **highest-valued successor** atau **random successor**.

### Neighbor sebagai highest-valued sucessor
Jika neighbor merupakan successor dengan value tertinggi, *successor function* akan mengembalikan semua state dengan memindahkan 1 queen ke kotak lain dalam kolom yang sama. Karena terdapat $8$ queen dan $7$ baris lain, maka terdapat $8 \times 7 = 56$ successor. Jika ada lebih dari 1 successor yang memliki nilai state terbaik, maka pilih salah satu secara acak.

### Neighbor sebagai random successor
Jika neighbor merupakan random successor, maka successor function hanya menghasilkan 1 successor dengan memilih 1 queen secara acak dan memindahkannya ke baris lain pada kolom yang sama.