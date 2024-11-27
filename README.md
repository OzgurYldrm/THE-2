# TR
## Nasıl kullanılır
1. `cases.txt` ve `compare.py` dosyalarını indirin.
2. Yeni bir klasör oluşturup içerisine `cases.txt` ve `compare.py` dosyalarını taşıyın. Çözümünüzün bulunduğu dosyayı aynı klasörün içerisine `THE2.py` ismiyle kopyalayın.
2.1. ALTERNATİF (üstteki çalışmazsa deneyin): `compare.py` dosyasının ilk iki satırında kodunuzun ve `cases.txt` dosyasının absolute path'ini değişkenlere verin (kodun içerisinde örnek olarak bulunmakta).
5. `compare.py` dosyasını python ile çalıştırın.
## Notes
1. Debugging'i engellememek için kod try-except içerisine alınmamıştır. Kendi kodunuzda alacağınız hatalar terminale bastırılıcaktır.
2. `compare.py` dosyasını bulunduğu klasörün içerisinde çalıştırın. "[Errno 2] No such file or directory" hatası alıyorsanız bununla alakalı olabilir. Bir başka yöntem olarak koda absolute path verebilirsiniz (ex: "D:\Projects\THE's\THE2.py"). 
3. "Unicode Error 'unicodeescape' codec can't decode bytes" Hatası alıyorsanız verdiğiniz path'deki "\" işaretlerini "/" ile değiştirmeyi deneyin
4. Kod belirli olan değerlerin ("MARITAL_STATUS" / "SPECIAL_NEEDS" etc.) bütün kombinasyonlarını ve belirli olmayan değerlerin (CHILD NUMBER AND AGE / INCOME) rastgele atanmasını içeriyor. Burda karşılaşmadığınız test caseler ve hatalar değerlendirilme sırasında ortaya çıkabilir (ama düşük bi ihtimal :) . Total 5184 Test Case bulunmakta.
5. Eğer değerler aynı olmasına rağmen FALSE dönüyorsa ekrana kaç basamak yazdırdığınıza dikkat edin. En büyük tavsiye print satırlarını dökümandan copy-paste yapın.
6. Input içerisine yazacağınız string ifadeler ve ekrandaki gereksiz printler kodun yanlış değerlendirilmesine yol açacaktır. input('Değer girin:') gibi ifadeler yerine sadece input() yazıp bırakın.
7. Kod her bir test case için "CASE COUNT | TRUE OR FALSE | YOUR_OUTPUT | ACTUAL OUTPUT" şeklinde çıktı vermektedir. En sonda toplam case sayısı üzerinden kaç doğru olduğunu gösterir.
8. PARTIAL GRADING KODU DEĞİLDİR!!!!! SADECE SONUÇLARI KARŞILAŞTIRIR.
## IT'S NOT THE PERFECT CODE. GIVE FEEDBACK IF YOU THINK SOMETHING IS WRONG
