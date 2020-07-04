#Github Linki :
#Soru 1
c = int(input("Gün Giriniz:"))
a = int(input("Ay Giriniz:"))
n = int(input("Yıl Giriniz:"))
b = {1: "Ocak", 2: 'Şubat', 3: 'Mart', 4: 'Nisan', 5: 'Mayıs', 6: 'Haziran',  7: "Temmuz", 8: 'Ağustos', 9: 'Eylül', 10: 'Ekim', 11: 'Kasım', 12: 'Aralık'}
print("1. Sorunun Çıktısı:", c, b[a], n)

#Soru 2
from functools import reduce
n = []
c = int(input("1-16 Arasında Bir Sayı Giriniz"))
if (9 <= c <16):
    for a in range(2, (c*2)+1, 2):
        n.append(a)
    print("2. Sorunun Çıktısı:", reduce(lambda b, s: b+s, n))
elif(9 > c >= 0):
    if (c == 0):
        print(1)
    else:
        for a in range(1, c+1):
            n.append(a)
    print("2. Sorunun Çıktısı:", reduce(lambda b, s: b*s, n)*3)
else:
    print("2. Sorunun Çıktısı:", "Girdiğiniz Sayı 15'den Büyük veya Negatif Bir Sayıdır ")

#Soru 4
b = []
c = 9
for a in range(1, c+1):
    n = a % 2
    if (n == 1):
        b.append(a)
print("Öğrenci Numaramın Son 2 Hanesi (09) 4. Sorunun Çıktısı: ", b)