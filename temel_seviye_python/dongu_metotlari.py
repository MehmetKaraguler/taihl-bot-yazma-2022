# METOT: range()
# range() fonksiyonunu belli bir aralıkta bulunan sayıları
# dödürmek için kulalanırız


# 1-10 arasındaki sayılardan oluşan bir liste
liste = list(range(1,10))
print(liste)
# Ekrana 50 tane phyton yazıdralım
# ÖRNEK: 1. Python
for sayi in range(1,51):
    print(f"{sayi}. Phyton")

# METOT: enumerate()
# İngilizcede enumerate kelimesi "numaralandırmak"anlamına gelir
# Fonksiyonun görevi nesne elemanlarını numaralndırarak dönüştürmek

# "python" kelimesininin karakterlerini enumarete
# ile numaralandırıp ekrana yazdıralım
kelime = "python"
kelime_enum = list(enumerate(kelime))
print(kelime_enum)
for index, harf in enumerate(kelime):
    print(index, harf)

# METOT: zip()
# zip listelerini birleştirme işlemini yapar
# satılardan o sayıların okunuşlarından oluşan 2 liste oluşturalım
sayilar = [1, 2, 3]
okunuslar = ["bir", "iki","üç"]

sayilar_zip = list(zip(sayilar, okunuslar))
print(sayilar_zip)
# for döngüsü içindde sayıları ve okunuişları ekrana yazdıralım
for sayi,okunus in zip(sayilar, okunuslar):
    print(sayilar_zip, okunus)