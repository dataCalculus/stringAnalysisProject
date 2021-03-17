#v1 --> gamification ve düzenleme yapılacak
#v2 --> harf analiziyle string manipulationı ardışıl hale getirmek...
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


YeniString=StringMuhendisi("   string Analiz projesi için preprocessing işlemi. "\
                           "muhtemelen m büyük harfle başlayacak , gerçekleştiren methodları barındırır.    ")
