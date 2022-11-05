"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    "ad": "Eren"
    "soyad": "Özdal"
"""

# belirili bir numaraya sahip olan öğrenciyi bulma işlemini liste ile yapalım
numaralar = [66,75]
isimler = ["Ahmet", "Mehmet"]
# numara = int(input("Öğrenci numarasını yazınız : "))
# konum = numaralar.index(numara)
# print(isimler[konum])

# belirili bir numaraya sahip olan öğrenciyi bulma işlemini dictionary  ile yapalım
# ogrenciler = {66: "Ahmet", 75:"Mehmet"}
# print(ogrenciler[numara])

kisiler = {
    1: {
        "ad":"Mehmet",
        "sayad":"Karagüler",
        "cinsiyet":"Erkek",

    },
    45: {
        "ad":"Ali",
        "soyad":"Karagüler",
        "cinsiyet":"Erkek",
    }
}

print(kisiler[45]["cinsiyet"])



