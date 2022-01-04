"""
Tiga sintaksis dasar dalam pemrograman adalah:
1. Sekuensial
2. Percabangan
3. Perulangan
"""

# Sekuensial
print('Ibu berkata, "Pergi belanja ke toko."')
print('Budi menjawab, "Baik Bu, apa yang harus saya beli?"')
print('Ibu menjawab, "Beli 1 botol susu dan jika ada telur, beli 6."')
print('Maka Budi berangkat ke toko dan mulai berbelanja.')

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1500

print(f"Jumlah susu yang ada di toko: {jumlah_botol_susu} botol.")
print(f"Jumlah telur yang ada di toko: {jumlah_telur} butir.")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya dan ternyata uangnya cukup.")
    if jumlah_botol_susu == 0:
        print("Budi membeli 1 botol susu.")
    else:
        print("Budi membeli 6 botol susu.")
else:
    print("Budi tidak jadi membeli satu 1 susu.")

print("Budi pulang ke rumah.")
print("Menyampaikan hasilnya kepada ibu.")
