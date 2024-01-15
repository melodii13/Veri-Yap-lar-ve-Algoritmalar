def tersine_cevir(liste):
    ters_cevrilmis_alt_listeler = [eleman[::-1] if isinstance(eleman, list) else eleman for eleman in liste]
    return ters_cevrilmis_alt_listeler[::-1]

kullanici_girisi = input("Lütfen bir liste girin : ")
girilen_liste = eval(kullanici_girisi)
ters_cevrilmis_liste = tersine_cevir(girilen_liste)
print(ters_cevrilmis_liste)
