# Pemeriksaan bagasi di bandara Kertajaya
batas_berat_lbs = 50

print("Silahkan letakkan bagasi Anda")
satuan_massa = input("Satuan tersedia \n1. kg\n2. lbs\npilih satuan (angka):")
if satuan_massa == str(1):
    berat_bagasi = float(input("Berat bagasi Anda:"))*2.205
elif satuan_massa == str(2):
    berat_bagasi = float(input("Berat bagasi anda:"))
else :
    print("masukkan ulang satuan yang dipilih")
    exit()
if berat_bagasi <= batas_berat_lbs:
    print("Silahkan melanjutkan perjalanan")
else :
    print("berat bagasi melewati batas, bagasi dikembalikan")

bagasi_1 = float(111 * 2.205)
a = 110 * 2.205
print('berat bagasi anda:',bagasi_1)
if bagasi_1 > a:
    print("hasil pemeriksaan bagasi 1:", bagasi_1 < batas_berat_lbs,", berat melewati batas")
else :
    print('error')
bagasi_2 = 49*2.205
print('berat bagasi anda:',bagasi_2)
if bagasi_2 > batas_berat_lbs :
    print("hasil pemeriksaan bagasi 2:", bagasi_2 < batas_berat_lbs, ", berat melewati batas")
else:
    print('error')