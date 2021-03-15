#length of English alphabet is equal to 26

class HarfAnalizMuhendisi():
    harfSozluguKucuk_count = {'a': 0, 'c': 0, 'b': 0, 'e': 0,
                              'd': 0, 'g': 0, 'f': 0, 'i': 0,
                              'h': 0, 'k': 0, 'j': 0, 'm': 0,
                              'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0,
                              's': 0, 'r': 0,
                              'u': 0, 't': 0, 'w': 0,
                              'v': 0, 'y': 0, 'x': 0, 'z': 0}
    harfSozluguBuyuk_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0,
                              'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                              'L': 0, 'M': 0, 'N': 0, 'O': 0,
                              'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                              'W': 0, 'X': 0, 'Y': 0, "Z": 0}
    kucukHarfler = list(harfSozluguKucuk_count.keys())
    buyukHarfler = list(harfSozluguBuyuk_count.keys())
    def __init__(self,string):
        self.string=string #analize tabii tutulacak string
    def gercekle_kucukHarfAnalizi(self):
        for i in range(26):
            self.harfSozluguKucuk_count[i] = self.string.count(kucukHarfler[i])
    def gercekle_buyukHarfAnalizi(self):
        for i in range(26):
            self.harfSozluguBuyuk_count[i] =self.string.count(buyukHarfler[i])
    def gercekle_butunHarfAnalizi(self):
        for i in range(26):
            self.harfSozluguKucuk_count[i] = self.string.count(self.kucukHarfler[i])
        for i in range(26):
            self.harfSozluguBuyuk_count[i] = self.string.count(self.buyukHarfler[i])
    def gosterBuyukHarfAnalizi(self):
        for key, value in self.harfSozluguBuyuk_count.items():
            print(key, "-->", value)
    def gosterKucukHarfAnalizi(self):
        for key, value in self.harfSozluguKucuk_count.items():
            print(key, "-->", value)


CreatorOfPython = HarfAnalizMuhendisi("If you're talking about Java in particular, Python "\
                    "is about the best fit you can get amongst all the other languages. "\
                    "Yet the funny thing is, from a language point of view, JavaScript has a lot in c"\
                    "ommon with Python, but it is sort of a restricted subset")

CreatorOfPython.gercekle_butunHarfAnalizi()
CreatorOfPython.gosterKucukHarfAnalizi()