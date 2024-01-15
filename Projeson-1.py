def duzlestir(liste):
    duz_liste = []
    for eleman in liste:
        if isinstance(eleman, list):
            duz_liste.extend(duzlestir(eleman))
        else:
            duz_liste.append(eleman)
    return duz_liste

try:
    kullanici_girisi = input("Lütfen bir liste girin : ")
    kullanici_listesi = eval(kullanici_girisi) 
    duz_liste = duzlestir(kullanici_listesi)
    print("Düzleştirilmiş Liste:", duz_liste)

except Exception as e:
    print(f"Hata: {str(e)}")
