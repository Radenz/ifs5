# Classical vs Local Search

## Classical Search
*Classical search* dirancang untuk lingkungan yang *observable* dan *deterministic*. Contoh dari classical search adalah BFS dan DFS. Classical search melakukan eksplorasi ruang pencarian secara sistematis sehingga dihasilkan solusi berupa *path* atau urutan aksi. Akan tetapi, pada beberapa problem, solusi path menuju goal tidak relevan, misalnya pada *N-Queens Problem*.

## Local Search
*Local search* merupakan alternatif kelas algoritma pencarian ketika path menuju goal atau sekuens aksi tidak penting. Secara umum, local search juga memiliki state, tetapi state yang dimaksud berupa konfigurasi "lengkap". Teknik ini hanya menyimpan satu *current state*, bukan path. Pencarian dilakukan dengan mencari state terbaik dengan berpindah ke *neighbor* dari current state secara iteratif sehingga dihasilkan solusi berupa *final state/configuration*. Dengan demikian, local search memiliki karakteristik berikut.
- Tidak ada *path cost*, hanya ada *state value*. State value menentukan state mana yang lebih baik dari current state.
- Tidak ada *goal test*, hanya diketahui state value maksimum.