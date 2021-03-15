#length of English alphabet is equal to 26

def harfAnalizi(string):

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
                              'W': 0, 'X': 0, 'Y': 0,"Z":0}

    kucukHarfler=list(harfSozluguKucuk_count.keys())
    buyukHarfler=list(harfSozluguBuyuk_count.keys())
    for i in range(26):
        harfSozluguKucuk_count[i]=string.count(kucukHarfler[i])
        harfSozluguBuyuk_count[i]=string.count(buyukHarfler[i])
    #print(harfSozluguBuyuk_count)
    for key,value in harfSozluguBuyuk_count.items():
        print(key,"-->",value)

    print("********************\n"
          "********************")
    print(harfSozluguKucuk_count)

harfAnalizi("Hello world this is my first string application")

