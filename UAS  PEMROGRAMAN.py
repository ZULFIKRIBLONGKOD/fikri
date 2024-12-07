menu = {
    "nasi kuning":10000,
    "ayam geprek":12000,
    "ikan goreng":8000,
    "lalapan":15000,
    "nutrisari":5000
}
print("daftar menu")
for i in menu:
    print("daftar menu : ", i,"\t harga : ",menu [i])
print("pembelian diatas Rp70.000,- mendapatkan diskon 10%")    
print("==================================================")
beli = input("pilih menu : ")
jumlah = int(input("jumlah pesanan : "))
bayar = jumlah * menu [beli] 

if bayar > 70000:
    diskon = bayar*10/100
    total = bayar - diskon 
else:
    total = bayar

print("detail pembayaran")
print("menu yang dipesan        : ",beli)  
print("jumlah yang dipesan      : ",jumlah)  
print("total biaya : ",bayar)
print("total yang harus dibayar : ",total)
