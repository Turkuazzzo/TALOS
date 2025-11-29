
```python
**Logical Operators**
giris_yapti_mi = True
print(giris_yapti_mi)
print(not giris_yapti_mi)
print(not 1)
print(not "")
print(not "yigit")
name = "" or "yigit"
print(name)
name = "" and "yigit"
print(name)
```

```python
**String Methods**
 print("kodla".upper())
print(" yigit ".strip())
print(len("yigit"))
print("yigit".capitalize())
print("yigit".swapcase())
```

```python
**Variable List**
import keyword
print(keyword.kwlist)
# Python'a ait özel kelimelerdir değişken isimleri olarak kullanılamazlar
# Değişken isimlerinde boşluk, özel harf gibi karakterler kullanılamaz
# keyword listesindekiler Python'a ait özel değişkenlerdir

total_score = 5
total score = 5

MAX_USERS = 5 # Sabitse büyük harf
_korumali_ = 3 # Dışarıdan değiştirilmemesi gerektiğinde böyle yazılmalı
türkçe_örnek = "Turkce Ornek" # Türkçe harfler kullanılmamaya özen gösterilmeli
```

```python
**Arithmetic Methods**
a = 20
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)
import math

print(math.sqrt(25))

print(math.pow(2,3))

print(math.ceil(4.5))

print(math.floor(4.5))

print(math.sin(math.radians(45)))

print(math.cos(math.radians(45)))

print(math.tan(math.radians(45)))

print(math.tan(math.radians(45))**-1)
print(math.pi)

print(math.e)
import random

random.seed(5)

print(random.randint(1, 10))
```

```python
**Assignment Methods**
a = 5

a = a + 5

a += 5
a -= 5
a /= 5
a *= 5
*Yinelemeli problemler çözme*
```

```python
**Boolean**
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
print(bool("kodla"))
print(bool(""))
giris_yapti_mi = True
giris_yapti_mi = False
giris_yapti_mi
```

```python
**Comparision Operators**
print(4 == 4)
print(4 != 5)
print(3 > 5)
print(4 < 5)
print(5 == 5.0)
print("a" == "a")
print("aa" == "aA")
x = 5
print(3 < x < 10)
a = 0.1
b = 0.2
print( a+b == 0.3)

# a ve b nin toplamı tam olarak 0.3 olmaz 0.3000000004 gibi çok ufak sapmaya sahiptir bu yüzden false çıkar
```

```python
**Conditional Expressions**
yagmurlu = False
gunesli = True

if yagmurlu:
   print("Ceket giy")

elif gunesli:
    print("ceket giyme")
x = 12

if x > 10:
    print("x 5'ten büyük")
x = 5

if x > 6:
    print("x 6'ten büyük")
elif x < 3:
    print("x 3'dan küçük")
else:
    print("x 3 ile 6 arasında bi sayıdır")
x = 7
y = 10

if x > 5 and y > 5:
    print("x ve ye ikisi de 5'ten büyük")
if x > 5 or y < 5:
    print("x 5'ten büyük veya y 5'ten küçük")
if not x < 5:
    print("x 5'ten küçük değil")
x = 7

if x > 5:
    print("x 5 ten büyük")
    if x > 7:
        print("x 7den büyük")
    
    else:
        print("x ne la")
if koşul:
    # koşul doğruysa çalışacak kod
elif başka_koşul:
    # önceki koşullar yanlışsa ve bu doğruysa çalışacak kod
else:
    # diğer tüm durumlar için
*Mini Proje: “Sanal Banka Hesabı / ATM Simülasyonu”
Amaç

Kullanıcı girişine göre farklı durumları kontrol et.

if, elif, else ve mantıksal operatörleri kullan.

İç içe if ile ekstra kontroller ekle.

Özellikler

Kullanıcıdan şifre ve bakiye al.

Menü sun:

1 → Para yatır

2 → Para çek

3 → Bakiye görüntüle

4 → Çıkış

Koşullar:

Çekilecek para bakiyeden fazla olamaz

Negatif giriş kabul edilmez

Hatalı seçenek girilirse uyar
```

```python
**Escape Chars**
print("Merhaba","Dünya","Ben","Yigit", sep="_")
print("Merhaba \n Dünya")
print("MerhabaZ \r Dünya")
print("Ben yigit", end =".\n")
menu = (
    "\n==============================\n"
    "\t PYTHON MENÜSÜ \n"
    "==============================\n"
    "1 - Kullanıcı Ekle\n"
    "2 - Kullanıcı Sil\n"
    "3 - Çıkış\n"
    "==============================\n"
)

print(menu)

import time
import os

frames = [
    " o\n/|\\\n/ \\",
    " o\n/|\\\n | ",
    " o\n/|\\\n/ \\",
]

while True:
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        time.sleep(0.3)
json_text = "{\n\t\"name\": \"Yiğitcan\",\n\t\"age\": 23\n}"

print(json_text)

log = "2025-11-28\tINFO\tLog kaydı oluşturuldu\n"
with open("log.txt", "a") as f:
    f.write(log)
*Yükleme barı*
```

```python
**Float Numbers**
pi = 3.14

print(type(pi))

negatif_ondalikli = -2.5

x = float(5)
**Float sayılar bilgisayarda 64 bit olarak saklanır**

- 1 bit işaret

- 11 bit büyüklük

- 52 bit kesir
*Anlamlı sayı bulma*
```

```python
**Functions**
def fonksiyon_adi(parametre1, parametre2):
    # Kodlar buraya yazılır
    sonuc = parametre1 + parametre2
    return sonuc
def topla(a,b):
    return a+b

print(topla(5,3))
def selamla(isim):
    print("merhaba",isim)

selamla("yigit")
selamla("1")
selamla(1)
selamla(True)
selamla(list)
def merhaba():
    print("Merhaba Dünya!")

merhaba()
def selamla(isim="arkadas"):
    print("Merhaba", isim)

selamla()
selamla("s")
def carp(a,b):
    sonuc = a*b
    return sonuc

x = carp(4,5)
print(x)

carp(4,5)
def kare(n):
    return n ** 2

kare(2)
```

```python
**İnput Data**
isim = input()

print(isim)
yas = input("Lütfen yaşınızı giriniz")
print(yas)
yas = int(input("Lütfen yaşınızı giriniz"))
print(yas)
yas = int(input("Lütfen yaşınızı giriniz"))
print(yas)
**Type Casting**
yas = int(input("Lütfen yaşınızı giriniz"))

print(yas > 18)
kilo = float(input("Lütfen kilonuzu giriniz"))

if kilo > 70:
    print("cok kilolusun")
*Hesap Makinesi*
s1 = int(input("birinci sayi"))
s2 = int(input("ikinci sayi"))

print("toplama: ", s1 + s2)
print("cikarma: ", s1-s2)
print("bolme: ", s1/s2)
print("carpma: ", s1*s2)
isim = input("isminizi giriniz")
yas = int(input("yasinizi girin"))

print("isim: " + isim + " yas: " + str(yas))
```

```python
**Integer Methods**
yas = 35
print(type(yas))
negatif = -10
sıfır = 0
print(type(negatif))
print(type(sıfır))
sayi2 = "36"
print(type(sayi2))
int_sayi = int(45)
print(type(int_sayi))
float_sayi = float(36)
print(type(float_sayi))
```

```python
**List İndexing**
egzersizler = ["squat" , "deadlift" , "dips" , "barfiks"]

print(egzersizler[0])
print(egzersizler[1])
print(egzersizler[2])
print(egzersizler[3])

egzersizler[2] = "plank"

# print(egzersizler[5]) # Error

print(egzersizler)
**List Operations**
egzersizler = ["squat" , "deadlift" , "dips" , "barfiks"]

print(len(egzersizler))

print("plank" in egzersizler)

print("bench press" in egzersizler)

egzersizler.append("bench press")

egzersizler.insert(1, "curl") # 1. indekse ekledi

egzersizler
del egzersizler[1]

print(egzersizler)
egzersizler.remove("barfiks")
**Slicing**
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

list[:10]
list[1:4]
list[1:5:2]
list[:]
list[::-1]
list2 = ["a","b","c","d","e","f"]

print(list2[1:4])

print(id(list2))
siparisler = [
    ["mouse","kulaklık"],
    ["klavye","monitor"],
    ["ssd","ram"]
]

print(siparisler[1])
sinif = [
    ["ali", 
     [80, 90, 70]],
    ["ahmet",
     [50,60,70]],
    ["ayse",
     [40,90,70]]
]

kopya_sinif = sinif
print(kopya_sinif)
list1 = [1,2,3,4,"a","s","d","f"]

list2 = list(range(0,3,1))
list2
tekrarli_liste = [[0] * 3] * 3
tekrarli_liste
diller = "python java dart swift"

split_liste = diller.split()
split_liste
split_liste_2 = diller.split(",")
split_liste_2
```

```python
**Lists**
liste = []

sayi_listesi = [ 1,2,3,4,5,6,7,8,9,10]

print(sayi_listesi , liste)
kelimeler = ["kodla", "yigit"]

boolean = [True, True, False]

karisik = [42, "yigido", True, "True", ["yeni", "liste", "icinde", "liste", 2], 3]

print(boolean)
print(karisik)
print(kelimeler)
**Iterable**
len(karisik[4])
yigit = list("yigit")
yigit
```

```python
**Logical Operators**
giris_yapti_mi = True
print(giris_yapti_mi)
print(not giris_yapti_mi)
print(not 1)
print(not "")
print(not "yigit")
name = "" or "yigit"
print(name)
name = "" and "yigit"
print(name)
```

```python
**String Methods**
 print("kodla".upper())
print(" yigit ".strip())
print(len("yigit"))
print("yigit".capitalize())
print("yigit".swapcase())
*Bir metinde seçilmiş kelimeleri string metodları ile istenilen hale getirme*
```

```python
**Variable List**
import keyword
print(keyword.kwlist)
# Python'a ait özel kelimelerdir değişken isimleri olarak kullanılamazlar
# Değişken isimlerinde boşluk, özel harf gibi karakterler kullanılamaz
# keyword listesindekiler Python'a ait özel değişkenlerdir

total_score = 5
total score = 5

MAX_USERS = 5 # Sabitse büyük harf
_korumali_ = 3 # Dışarıdan değiştirilmemesi gerektiğinde böyle yazılmalı
türkçe_örnek = "Turkce Ornek" # Türkçe harfler kullanılmamaya özen gösterilmeli
```

```python
**Variables**
SelamVer = "Merhaba Dünya"

print(SelamVer)
print(id(SelamVer))
mesaj = "merhaba" # String
sayı = 42 # Integer
pi = 3.1415 # Float
OdemeYapıldı = True # Boolean
selam = "merhaba"
kopya = selam

print(id(selam))
print(id(kopya))
import sys
print(sys.getrefcount(selam))
yeni_kopya = selam
print(sys.getrefcount(yeni_kopya))
isim = "yigit"
isim[1]
*Kelimeleri ters çevirme, kaç kelime olduğunu bulma, kaç harfi olduğunu yazdırma*
```
