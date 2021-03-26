print("KODE YANG SEHARUSNYA!!")
s = "Disini banyak tikus!"
# Panjangnya harusnya 20
print("panjang dari s = %d" % len(s))
# huruf pertama ‘a’ harusnya di index no 8
print("Kemunculan pertama a = %d" % s.index("a"))
# jumlah huruf a harusnya 2
print("a muncul sebanyak %d kali" % s.count("a"))
# memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5]) # Start to 5
print("Lima karakter berikutnya adalah '%s'" % s[5:10]) # 5 to 10
print("Karakter ketiga belas adalah '%s'" % s[12]) # Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" %s[1::2]) #(0-based indexing)
print("Lima karakter terakhir adalah '%s'" % s[-5:]) # 5th-from-last to end
# konversikan ke upercase
print("String dalam huruf besar: %s" % s.upper())
# konversikan ke lowercase
print("String dalam huruf kecil: %s" % s.lower())
# cek bagaimana string itu dimulai
if s.startswith("Di"):
    print("String dimulai dengan 'Di'. Mantap!")
# cek bagaimana string itu diakhiri
if s.endswith("kus!"):
    print("String diakhiri dengan 'kus!'. Mantap!")
# Pisahkan string menjadi tiga string yang terpisah, masing-masing hanya berisi satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))