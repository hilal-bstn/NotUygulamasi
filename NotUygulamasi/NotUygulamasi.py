def Hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')

    ogrenciAdi=liste[0] 
    notlar=liste[1].split(",")

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not1+not2+not3)/3
    if ortalama>=90 and ortalama<=100:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BA"
    elif ortalama>=80 and ortalama<=84:
        harf="BB"
    elif ortalama>=75 and ortalama<=79:
        harf="CB"
    elif ortalama>=70 and ortalama<=74:
        harf="CC"
    elif ortalama>=65 and ortalama<=69:
        harf="DC"
    elif ortalama>=60 and ortalama<=64:
        harf="DD"
    elif ortalama>=50 and ortalama<=59:
        harf="FD"
    else:
        harf="FF"
    return ogrenciAdi + ": "+harf+"\n" 



def Ortalamalar():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(Hesapla(satir))
def NotEkle():
    name=input('Öğrenci adı: ')
    surname=input('Öğrenci soyadı: ')
    not1=input('Not 1: ')
    not2=input('Not 2: ')
    not3=input('Not 3: ')
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(name+' '+surname+' : '+not1+','+not2+','+not3+'\n')

def NotKayit():

    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(Hesapla(i))
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem=input(' 1-Notları oku \n 2-Not gir \n 3-Notları Kayıt et \n 4-çıkış \n')
    if islem=='1':
        Ortalamalar()
    elif islem=='2':
        NotEkle()
    elif islem=='3':
        NotKayit()
    else:
        break
