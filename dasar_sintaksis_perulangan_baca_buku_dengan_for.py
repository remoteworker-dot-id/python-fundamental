"""
Program perulangan membaca buku dengan for
"""
jumlah_buku = 10
print('Ibu berkata, "Bacalah semua bukumu!"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print("Perulangan dengan for")
for jumlah_buku_yang_sudah_dibaca in range (1, jumlah_buku+1):
    print(f"Buku ke{jumlah_buku_yang_sudah_dibaca} sudah dibaca.")

print(f'\nJumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')
