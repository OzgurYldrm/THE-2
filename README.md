# TR
## Nasıl kullanılır
1. `cases.txt` ve `compare.py` dosyalarını indirin.
2. Dosyaları THE-2 çözüm kodunuzun olduğu klasöre taşıyın.
3. `compare.py` dosyasının ilk satırında kodunuzun path'ini verin. İkinci satırda indirdiğiniz `cases.txt` dosyasının path'ini verin.
4. `compare.py` dosyasını python ile çalıştırın.
## Notes
1. Debugging'i engellememek için kod try-except içerisine alınmamıştır. Kendi kodunuzda alacağınız hatalar terminale bastırılıcaktır.
2. `compare.py` dosyasını bulunduğunuz klasörün içerisinde çalıştırın. "[Errno 2] No such file or directory" hatası alıyorsanız bununla alakalı olabilir. Bir başka yöntem olarak koda absolute path verebilirsiniz. (ex: "D:\Projects\THE's\THE2.py")
3. Kod belirli olan değerlerin ("MARITAL_STATUS" / "SPECIAL_NEEDS" etc.) bütün kombinasyonlarını ve belirli olmayan değerlerin (CHILD NUMBER AND AGE / INCOME) rastgele atanmasını içeriyor. Burda karşılaşmadığınız test caseler ve hatalar değerlendirilme sırasında ortaya çıkabilir (ama düşük bi ihtimal :)
4. Eğer değerler aynı olmasına rağmen FALSE dönüyorsa ekrana kaç basamak yazdırdığınıza dikkat edin. En büyük tavsiye print satırlarını dökümandan copy-paste yapın.
5. Input içerisine yazacağınız string ifadeler ve ekrandaki gereksiz printler kodun yanlış değerlendirilmesine yol açacaktır. input('Değer girin:') gibi ifadeler yerine sadece input() yazıp bırakın.
6. Kod her bir test case için "CASE COUNT | TRUE OR FALSE | YOUR_OUTPUT | ACTUAL OUTPUT" şeklinde çıktı vermektedir. En sonda toplam case sayısı üzerinden kaç doğru olduğunu gösterir.
7. PARTIAL GRADING KODU DEĞİLDİR!!!!! SADECE SONUÇLARI KARŞILAŞTIRIR.
## IT'S NOT THE PERFECT CODE. GİVE FEEDBACK IF YOU THINK SOMETHING IS WRONG
