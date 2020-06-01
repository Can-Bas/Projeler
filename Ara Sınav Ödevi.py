#Soru 2

c = []

for a in range(6):
    import random
    c.append(random.randint(1, 50))


if (c[0]!=c[1] and c[1]!=c[2] and c[2]!=c[3] and c[3]!=c[4] and c[4]!=c[5]):
    print("Soru 2 Ekran Çıktısı :", c)

#Soru 3


try:
    can = open(file='Ara Sınav Ödevi.txt', mode='w+', encoding="utf-8")
    c = int(input("0-100 Arasında Bir Sayı Giriniz"))
    print("SORU 3 BİLGİLENDİRME : Girdiğiniz Sayının Ekran Çıktısı Dosyadadır")
except FileNotFoundError:
    print("Dosya Bulunamadı")

if (0< c <=99):
    for n in range(0, c+1):
        a = n//10 + n % 10
        b = a % 2
        if(b == 1):
            can.write(str(n) + "    ")
else:
    print("Girdiğiniz Sayı 0-100 Arasında Değildir")

#Soru 4
from functools import reduce

soyad = ['Aygun', 'Çiçek', 'Deniz', 'Atar', 'Dener', 'Yılmaz']
toplam_satis_miktari = [['Ayse', 3, 6, 7], ['Ece', 5, 2, 4], ['Arya', 6, 5], ['Ali', 3], ['Can', 5, 7, 9, 11], ['Aybar', 2, 3]]
adsoyad = map(lambda c, a: [a[0]+" "+c], soyad, toplam_satis_miktari)
kişisatışları = list(map(lambda n: n[1:], toplam_satis_miktari))

c = []
c = reduce(lambda c, a: c+a, kişisatışları[0])
a = []
a = reduce(lambda c, a: c+a, kişisatışları[1])
n = []
n = reduce(lambda c, a: c+a, kişisatışları[2])
b = []
b = reduce(lambda c, a: c+a, kişisatışları[3])
aa = []
aa = reduce(lambda c, a: c+a, kişisatışları[4])
s = []
s = reduce(lambda c, a: c+a, kişisatışları[5])
toplamsatışları = [c, a, n, b, aa, s]
print("Soru 4 Ekran Çıktısı : ", list(zip(adsoyad, toplamsatışları)))