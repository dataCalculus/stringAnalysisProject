# length of English alphabet is equal to 26
from collections import OrderedDict
from matplotlib import pyplot as plt

#string analizi için gamificationa gerek görülmeyecek şekilde constructorda düzenleme yapıldı..
#v1 --> string girişleri hafızalı olabilir.
#v2 --> hafızalı string girişleri enumerate edilerek tercihe bağlı plotlar yapılabilir
#v3 --> tercihe bağlı plotlar subplotlar haline getirilebilir (başka bir gamification)
class StringMuhendisi():
    def __init__(self,string):
        self.string = string
        self.pureLength = len(string)
        print("String Muhendisine hos geldiniz...\n"\
              "Lütfen strip edilecek yöntemi seçiniz...both , left , right")
        stripType = input("")
        self.string=self.removeWhitespace(self.string,stripType)
        self.string=self.splitSentecesAndCapitalize(self.string)
        print("case conversion yapmak ister misiniz ?")
        yesORno = input("y or n ?")
        if yesORno == "y":
            print("case conversion a karar verdiniz..."\
                  "lütfen seçim yapınız l or u")
            selection = input("")
            self.string = self.caseConversion(self.string,selection)
        else:
            pass
        self.newLength = len(self.string)
        print(self.getReducedAmountOfStringLength())
    def removeWhitespace(self,string,stripType="both"):
        if stripType == "left":
            self.string = self.string.lstrip()
            return self.string
        elif stripType == "right":
            self.string = self.string.rstrip()
            return self.string
        else:
            self.string = self.string.strip()  # remove from both left and right
            return self.string

    #parçala noktadan sonraki harfleri büyük harf yap
    #split ". " separator
    def splitSentecesAndCapitalize(self,string):
        stringList = self.string.split(". ")
        newString=""
        counter = 0
        for i in stringList:
            if counter == 0:
                newString = newString + i.capitalize()
            else :
                newString=newString+". "+i.capitalize()
            counter+=1
        return newString


    #********* istege bagli *********
    #lower , upper
    def caseConversion(self,string,selection):
        """
        selection == l  --> lower
        selection == u  --> upper
        """
        if selection=="l":
            self.string = self.string.lower()
            return self.string
        elif selection=="u":
            self.string = self.string.upper()
            return self.string

        #in order to eliminate error
        else:
            return self.string
    def getString(self):
        return self.string
    def getReducedAmountOfStringLength(self):
        print("eski uzunluk {}".format(self.pureLength))
        print("yeni uzunluk {}".format(self.newLength))
        reduction = self.pureLength - self.newLength
        return  reduction
    def __str__(self):
        return"String Analiz projesi için preprocessing işlemi gerçekleştiren methodları barındırır.\n"\
        "Ayrıca optional case conversion işlemi de bulunur..."






# kullanılmayan harflerin gösterildiği seçenekler eklendi
class HarfAnalizMuhendisi():
    harfSozluguKucuk_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0,
                              'e': 0, 'f': 0, 'g': 0, 'h': 0,
                              'i': 0, 'j': 0, 'k': 0, 'l': 0,
                              'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0,
                              'r': 0, 's': 0,
                              't': 0, 'u': 0, 'v': 0,
                              'w': 0, 'x': 0, 'y': 0, 'z': 0}
    harfSozluguKucuk_count = OrderedDict(harfSozluguKucuk_count)
    harfSozluguBuyuk_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0,
                              'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                              'L': 0, 'M': 0, 'N': 0, 'O': 0,
                              'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                              'W': 0, 'X': 0, 'Y': 0, "Z": 0}
    harfSozluguBuyuk_count = OrderedDict(harfSozluguBuyuk_count)
    kucukHarfler = list(harfSozluguKucuk_count.keys())
    buyukHarfler = list(harfSozluguBuyuk_count.keys())

    def __init__(self, string):
        self.string = string  # analiz gerçekleştirilecek string

    def gercekle_kucukHarfAnalizi(self):
        for k in self.kucukHarfler:
            self.harfSozluguKucuk_count[k] = self.string.count(k)

    def gercekle_buyukHarfAnalizi(self):
        for k in self.buyukHarfler:
            self.harfSozluguBuyuk_count[k] = self.string.count(k)

    def gercekle_butunHarfAnalizi(self):
        for k in self.kucukHarfler:
            self.harfSozluguKucuk_count[k] = self.string.count(k)
        for l in self.buyukHarfler:
            self.harfSozluguBuyuk_count[l] = self.string.count(l)

    def gosterBuyukHarfAnalizi(self):
        for key, value in self.harfSozluguBuyuk_count.items():
            print("{:1s}   {:2d}".format(key,value))

    def gosterKucukHarfAnalizi(self):
        for key, value in self.harfSozluguKucuk_count.items():
            print("{:1s}   {:2d}".format(key,value))

    def gosterString(self):
        print(self.string)

    def gosterGrafik_kucukHarf(self):
        fig = plt.figure()
        values = self.harfSozluguKucuk_count.values()
        plt.bar(self.kucukHarfler, values)
        plt.show()

    def gosterGrafik_buyukHarf(self):
        fig = plt.figure()
        values = self.harfSozluguBuyuk_count.values()
        plt.bar(self.buyukHarfler, values)
        plt.show()
    def goster_kucukHarf_kullanilmayan(self):
        print("Kullanılmayan küçük harfler şunlardır...")
        for i in range(26):
            if self.harfSozluguKucuk_count[(self.kucukHarfler[i])] ==0:
                print(self.kucukHarfler[i],self.harfSozluguKucuk_count[(self.kucukHarfler[i])])
        print("*********************************")
    def goster_buyukHarf_kullanilmayan(self):
        print("Kullanılmayan büyük harfler şunlardır...")
        for i in range(26):
            if (self.harfSozluguBuyuk_count[self.buyukHarfler[i]] == 0):
                print(self.kucukHarfler[i],self.harfSozluguBuyuk_count[(self.buyukHarfler[i])])
        print("*********************************")
    def __str__(self):
        return "Constructorda girilen stringe harf analizi yapan ve plot ile ifade eden bir Sınıf" \
               "tan türetilen obje"


if __name__ == '__main__':
    # 1=kucukharf analizi 2=buyukharf analizi
    # 3=butunHarf analizi
    # 4=goster kucukharf analizi 5=buyukharfAnalizi
    # 6=goster String
    # 7=cıkıs
    # 8=plot kucuk harf , 9=plot buyuk harf
    # 10=kullanılmayan kucukHarfler
    # 11=kullanılmayan buyukHarfler
    print("String Analizi Programına hoşgeldiniz...\n"\
          "Lütfen işlem gerçekleştirilmek istenen stringi giriniz...")
    stringg = input("")




    CreatorOfPython = HarfAnalizMuhendisi(StringMuhendisi(stringg).getString())

    while (True):
        #eliminate error
        while True:
            try:
                print("0=Class hakkında bilgi...\n"
                      "1=kucukharf analizi 2=buyukharf analizi\n" \
                      "3=butunHarf analizi\n" \
                      "4=goster kucukharf analizi 5=buyukharfAnalizi\n" \
                      "6=goster String\n" \
                      "7=cıkıs\n"\
                      "8=kucukHarf bar plot\n"\
                      "9=buyukHarf bar plot\n"\
                      "10=goster kullanılmayan kucukHarfler\n"\
                      "11=goster kullanılmayan buyukHarfler")
                selection = int(input())
            except ValueError:
                print('Please enter a valid integer')
                continue
            break
        if selection == 1:
            CreatorOfPython.gercekle_kucukHarfAnalizi()
            print("Kucuk harf analizi tamamlandı...")
            continue
        elif selection == 2:
            CreatorOfPython.gercekle_buyukHarfAnalizi()
            print("Buyuk harf analizi tamamlandı...")
            continue
        elif selection == 3:
            CreatorOfPython.gercekle_butunHarfAnalizi()
            print("Butun harf analizi tamamlandı...")
            continue
        elif selection == 4:
            CreatorOfPython.gosterKucukHarfAnalizi()
            continue
        elif selection == 5:
            CreatorOfPython.gosterBuyukHarfAnalizi()
            continue
        elif selection == 6:
            CreatorOfPython.gosterString()
            continue
        elif selection == 7:
            print("Programdan çıkılıyor...")
            break
        elif selection == 8:
            CreatorOfPython.gosterGrafik_kucukHarf()
            continue
        elif selection == 9:
            CreatorOfPython.gosterGrafik_buyukHarf()
            continue
        elif selection == 0:
            print(CreatorOfPython)
            continue
        elif selection == 10:
            CreatorOfPython.goster_kucukHarf_kullanilmayan()
            continue
        elif selection == 11:
            CreatorOfPython.goster_buyukHarf_kullanilmayan()
            continue
        else :
            print("Geçersiz seçim...Lütfen 0-11 arasında bir seçim yapınız.")