
print("=== APOTEK SEHAT ===")
print("PROGRAM OPERATOR PEMBANDING HARGA OBAT")

print("\nDAFTAR HARGA OBAT")
print("1. Paracetamol       = Rp5.000")
print("2. Ibuprofen         = Rp8.000")
print("3. Antasida          = Rp4.000")
print("4. Vitamin C         = Rp10.000")
print("5. CTM               = Rp3.000")
print("6. Loratadine        = Rp7.000")
print("7. Cetirizine        = Rp6.000")
print("8. Oralit            = Rp2.500")
print("9. Domperidone       = Rp9.000")
print("10. Vitamin B Complex = Rp12.000")

print("\nPILIH DUA OBAT UNTUK DIBANDINGKAN")

obat1 = int(input("Masukkan harga obat pertama: "))
obat2 = int(input("Masukkan harga obat kedua: "))

print("\n=== HASIL PERBANDINGAN ===")

print("Obat pertama lebih mahal:", obat1 > obat2)
print("Obat pertama lebih murah:", obat1 < obat2)
print("Harga kedua obat sama:", obat1 == obat2)
print("Harga kedua obat berbeda:", obat1 != obat2)
print("Obat pertama lebih mahal atau sama:", obat1 >= obat2)
print("Obat pertama lebih murah atau sama:", obat1 <= obat2)
