daftar_buku = ['Seven Habits', 'How to Influence People','First thing first', '4DX']
print('\nTampilkan semua daftar_buku:')
print(daftar_buku)

print('\nProses semua dengan for in:')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu:')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan isi dengan for in range:')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan isi dengan for in range, di mana data tiap elemen berbeda:')
daftar_buku = [15, 'Kuma Kuma Bear', -11, 3.14]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to Influence People','First thing first', '4DX']
print('\nMenambahkan 1 buku baru dengan perintah append:')
daftar_buku.append('Kuma Kuma Bear')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah pop:')
daftar_buku = ['Seven Habits', 'How to Influence People','First thing first', '4DX']
daftar_buku.pop(-4)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
