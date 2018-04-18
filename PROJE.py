from libs.urllib2 import * #Url'e ulaþmak ve url'den dosya indirmek için kullandýðýmýz kütüphane.
from PIL import ImageFile # Bunun çok gereði olmasa da,verilen web sitesindeki resimlerden bazýlarýnýn siteye eksik upload edilmesi sonucu eksik görüntülenmesi, pythonun bu resim dosyalarýný
#okuyamamasýndan dolayý bu tür dosyalarý okurken bunu görmezden gelmesini söyledik.
from libs.img2pdf import* #Ýndirilen dosyalarý pdf e basarken kullandýðýmýz açýk kaynak kütüphane.
sayi=0 #Bir sayaç belirledik 0.pngden baþlayýp 99.pngye kadar gitmesi için. Ýlk baþta 0 a eþitliyoruz
while sayi<100: #sayi 100den küçük olduðu durumlarda:
    url = "http://atlas-live.cern.ch/archive/" #urlmizin baþlangýcý bu sonundaki kýsým ise resme göre deðiþecek. 100 adet resim arasýndan seçilecek.
    url=url+str(sayi)+".png" #Urlmizin sonuna sayac_degeri+.png ekliyoruz. Bu þekilde linkimiz http://atlas-live.cern.ch/archive/sayac_degeri.png oluyor.
    file_name = "folder/"+url.split('/')[-1]#Dosya adýný da sonuncu '/' iþaretinden itibaren kesip otomatik olarak alýyoruz.
    u = urlopen(url) #urllib2 kütüphanesindeki urlopen fonksiyonunu kullanarak web sitesine istek gönderdik.
    f = open(file_name, 'wb') #resmimizi kaydetmek için bir dosya pointeri tanýmladýk.
    meta = u.info() # urlye yolladýðýmýz isteðin sonucunu ve o anki diðer bilgileri tutuyor.
    file_size = int(meta.getheaders("Content-Length")[0])#Meta bilgisinden içeriðin uzunluðunu çekiyor.
    print "Ýndiriliyor: %s Byte: %s" % (file_name, file_size) # Dosyanýn ismini ve boyutunu görüntülüyor.
    file_size_dl = 0 #Dosyanýn anlýk boyutunu tutuyor.
    block_sz = 8192 #Dosyanýn kaçlý bloklar halinde alýndýðýný belirledik.
    while True: #Sonsuza dek bu iþlemi yap.Ama sonsuz döngüye girmeyecek döngü içindeki bir break sayesinde.
        buffer = u.read(block_sz) # Buffer'a maksimum blok boyutu kadar veriyi oku.
        if not buffer: #Eðer boþsa
            break #Döngüyü durdur.
        file_size_dl += len(buffer) #Dosya boyutuna o anki bufferýn boyutunu ekle.
        f.write(buffer)#Bufferý dosyaya yaz.
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)#Dosyanýn indirme sürecini görüntüler.
        status = status + chr(8)*(len(status)+1)#Her buffer dosyaya yazýldýktan sonra statusu artýracaðýz.
        print status,#statusu ekrana bas.
    sayi+=1;#döngüyü bir adým ilerlet.
    f.close()#Ýþlemler bittikten sonra dosyayý kapat.
sayi=0#Ýkinci döngüde indirdiðimiz dosyalarý pdf e basacaðýmýz için yine bir sayaca ihtiyaç duyacaðýz. Farklý isimde bir sayaç kullanmak yerine eskisiyle iþimiz bittiði için onu sýfýrladýk.
list=[]#Bu list sayesinde dosyalarýn ismini bir bütün halinde tutabileceðiz. Eðer bunu yapmasaydýk. img2pdf kütüphanesinin convert fonksiyonuna sýrasýyla 100 resmi de (veya ne kadar resim
#varsa tek tek yazmak zorunda kalacaktýk.Yine liste kullanacaktýk ama elimizle yazacaktýk þu þekilde:img2pdf.convert(['0.png','1.png',...].Bunun önüne geçmek için hepsini döngüyle
#listimize ekleyip daha sonra o listi direkt olarak fonksiyonun içerisinde kullandýk.
while sayi<100: #Sayac deðerimiz 100den küçük olduðu sürece
    list.append('folder/'+str(sayi)+'.png') #liste þu elemaný ekle.(Burada basit bir str birleþtirme iþlemi kullandýk.)
    sayi+=1;#Döngüyü bir adým ilerlet.
    ImageFile.LOAD_TRUNCATED_IMAGES = True#Kütüphane tanýmlamalarýnda bahsettiðimiz eksik dosyalarýn yüklenmesi olayýna izin verdik.
print (list)#Listin elemanlarýný yazdýrdýk.
pdf_bytes = convert(list)#Convert fonksiyonuna listemizi parametre olarak gönderip pdf_bytes dosya pointerýna hatamasýný söyledik.
file = open("folder/name.pdf","wb")#Pdf dosyamýzý oluþturduk.
file.write(pdf_bytes)#Veriyi pdf dosyasýna bastýk.
file.close()#Dosyayý kapattýk.
