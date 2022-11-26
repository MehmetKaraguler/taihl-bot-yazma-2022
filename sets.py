"""
sets listeleri süslü parantezler '{}' içinde tanımlanır.
sets liste elemanlarına indeks numaraları ile ulaşılamaz.
sets liste elemanlarına döngü içinde ulaşılır.
sets listeleri içinde aynı eleman birden fazla yer alamaz.
"""

# sets listesi oluşturalım
sets_liste = {1, 2, 3, 4}
# sets listesinin içindeki nir elemana ulaşalım
# print(sets_liste[0]) hata verdi
# sets liste elemanlarına döngü ile ulaşalım
# sets listesinin içindeki bir elemana ulaşalım
for eleman in sets_liste:
    print(eleman)

# sets listesine bir eleman ekleyelim: add()
sets_liste.add(5)
print(sets_liste)

# sets listesine bir veya birden fazla elaman ekleyelim: update([])
sets_liste.update([19, 20, 21])
print(sets_liste)
# tekrarlayan elamanı olan bir listeyi sets listesine dönüştürelim
liste = [1,2,3,1,15,16,16,1]
sets_liste = set(liste)