sayilar = [9, 12, 7, 9, 7, 515, 23]
harfler = ["e", "c,", "s", "f", "z"]

# listener eleman sayısını bulalım: len(liste)
# print(len(sayilar))
# print(len(harfler))

# listenin en küçük değerli elamanını bulalım
# print(min(sayilar))
# print(min(harfler))

# listenin en büyük değerli elemanını bulalım: max()
# print(max(sayilar))
# print(max(harfler))

# metin ve sayılardan oluşan listeleri birleştirip en büyüğünü bulalım
birlesmis = sayilar + harfler
# TypeError: '>' not supported between instances of 'str' and 'int'
# print(max(birlesmis))
# listenin sonuna yeni eleman ekleyelim: append()
sayilar.append(95)
# print(sayilar)

# listenin istediğimiz konumuna yeni eleman ekleyelim
harfler.insert(3, "b")
# print(harfler)

# listenin sonundakini elamanı silelim: pop()
harfler.pop()
print(harfler)
harfler.pop(3)  # belirli konumundaki b harfi silinir
print(harfler)


# listede belirli bir değere sahip elemanları silelim: remove("değer")
harfler.remove("a")
print(harfler)


# listedeki elemanları sırayalım: sort()
print(sayilar)
sayilar.sort()
print(sayilar)
sayilar.sort(reverse=True) # azalan sıralama yapar
print(sayilar)

# listedeki isimleri alfabetik sıraya göre sırayalım
isimler=["Eren", "Ersin", "Ahmet","Mehmet"]
isimler.sort()
print(isimler)
