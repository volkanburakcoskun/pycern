from libs.urllib2 import * #Url'e ula�mak ve url'den dosya indirmek i�in kulland���m�z k�t�phane.
from PIL import ImageFile # Bunun �ok gere�i olmasa da,verilen web sitesindeki resimlerden baz�lar�n�n siteye eksik upload edilmesi sonucu eksik g�r�nt�lenmesi, pythonun bu resim dosyalar�n�
#okuyamamas�ndan dolay� bu t�r dosyalar� okurken bunu g�rmezden gelmesini s�yledik.
from libs.img2pdf import* #�ndirilen dosyalar� pdf e basarken kulland���m�z a��k kaynak k�t�phane.
sayi=0 #Bir saya� belirledik 0.pngden ba�lay�p 99.pngye kadar gitmesi i�in. �lk ba�ta 0 a e�itliyoruz
while sayi<100: #sayi 100den k���k oldu�u durumlarda:
    url = "http://atlas-live.cern.ch/archive/" #urlmizin ba�lang�c� bu sonundaki k�s�m ise resme g�re de�i�ecek. 100 adet resim aras�ndan se�ilecek.
    url=url+str(sayi)+".png" #Urlmizin sonuna sayac_degeri+.png ekliyoruz. Bu �ekilde linkimiz http://atlas-live.cern.ch/archive/sayac_degeri.png oluyor.
    file_name = "folder/"+url.split('/')[-1]#Dosya ad�n� da sonuncu '/' i�aretinden itibaren kesip otomatik olarak al�yoruz.
    u = urlopen(url) #urllib2 k�t�phanesindeki urlopen fonksiyonunu kullanarak web sitesine istek g�nderdik.
    f = open(file_name, 'wb') #resmimizi kaydetmek i�in bir dosya pointeri tan�mlad�k.
    meta = u.info() # urlye yollad���m�z iste�in sonucunu ve o anki di�er bilgileri tutuyor.
    file_size = int(meta.getheaders("Content-Length")[0])#Meta bilgisinden i�eri�in uzunlu�unu �ekiyor.
    print "�ndiriliyor: %s Byte: %s" % (file_name, file_size) # Dosyan�n ismini ve boyutunu g�r�nt�l�yor.
    file_size_dl = 0 #Dosyan�n anl�k boyutunu tutuyor.
    block_sz = 8192 #Dosyan�n ka�l� bloklar halinde al�nd���n� belirledik.
    while True: #Sonsuza dek bu i�lemi yap.Ama sonsuz d�ng�ye girmeyecek d�ng� i�indeki bir break sayesinde.
        buffer = u.read(block_sz) # Buffer'a maksimum blok boyutu kadar veriyi oku.
        if not buffer: #E�er bo�sa
            break #D�ng�y� durdur.
        file_size_dl += len(buffer) #Dosya boyutuna o anki buffer�n boyutunu ekle.
        f.write(buffer)#Buffer� dosyaya yaz.
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)#Dosyan�n indirme s�recini g�r�nt�ler.
        status = status + chr(8)*(len(status)+1)#Her buffer dosyaya yaz�ld�ktan sonra statusu art�raca��z.
        print status,#statusu ekrana bas.
    sayi+=1;#d�ng�y� bir ad�m ilerlet.
    f.close()#��lemler bittikten sonra dosyay� kapat.
sayi=0#�kinci d�ng�de indirdi�imiz dosyalar� pdf e basaca��m�z i�in yine bir sayaca ihtiya� duyaca��z. Farkl� isimde bir saya� kullanmak yerine eskisiyle i�imiz bitti�i i�in onu s�f�rlad�k.
list=[]#Bu list sayesinde dosyalar�n ismini bir b�t�n halinde tutabilece�iz. E�er bunu yapmasayd�k. img2pdf k�t�phanesinin convert fonksiyonuna s�ras�yla 100 resmi de (veya ne kadar resim
#varsa tek tek yazmak zorunda kalacakt�k.Yine liste kullanacakt�k ama elimizle yazacakt�k �u �ekilde:img2pdf.convert(['0.png','1.png',...].Bunun �n�ne ge�mek i�in hepsini d�ng�yle
#listimize ekleyip daha sonra o listi direkt olarak fonksiyonun i�erisinde kulland�k.
while sayi<100: #Sayac de�erimiz 100den k���k oldu�u s�rece
    list.append('folder/'+str(sayi)+'.png') #liste �u eleman� ekle.(Burada basit bir str birle�tirme i�lemi kulland�k.)
    sayi+=1;#D�ng�y� bir ad�m ilerlet.
    ImageFile.LOAD_TRUNCATED_IMAGES = True#K�t�phane tan�mlamalar�nda bahsetti�imiz eksik dosyalar�n y�klenmesi olay�na izin verdik.
print (list)#Listin elemanlar�n� yazd�rd�k.
pdf_bytes = convert(list)#Convert fonksiyonuna listemizi parametre olarak g�nderip pdf_bytes dosya pointer�na hatamas�n� s�yledik.
file = open("folder/name.pdf","wb")#Pdf dosyam�z� olu�turduk.
file.write(pdf_bytes)#Veriyi pdf dosyas�na bast�k.
file.close()#Dosyay� kapatt�k.
