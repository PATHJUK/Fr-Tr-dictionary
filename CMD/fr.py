def hoşGeldin():
    inp1 = input("Başlamak için 'Başla', çıkmak için 'Çık', tüm kelimeleri görmek için 'Sözlük' yaz.\n")
    if inp1 == "Başla":
        istekNe()
    elif inp1 == "Çık":
        print("Program sonlandırılıyor...")
        exit(0)
    elif inp1 == "Sözlük":
        alfabetikSıra()
        f = open("fr.txt", "r")
        print(f.read())
        hoşGeldin()
    else:
        hoşGeldin()

def detaylıbilgi(inp1, inp2):
    if inp2 == "frkelime.txt":
        with open(inp2) as enter:
            for line in enter:
                if line.startswith("%s" % inp1):
                    print("Fransızcası ==> %s|\n" % inp1)
                    a = enter.readline()
                    b = enter.readline()
                    print("Okunuşu ==> %s" % a)
                    print("Türkçesi ==> %s" % b)
                    hoşGeldin()
    if inp2 == "frfiil.txt":
        with open(inp2) as enter:
            for line in enter:
                if line.startswith("%s" % inp1):
                    print("Fransızcası ==> %s\n" % inp1)
                    a = enter.readline()
                    b = enter.readline()
                    c = enter.readline()
                    d = enter.readline()
                    e = enter.readline()
                    f = enter.readline()
                    g = enter.readline()
                    h = enter.readline()
                    print("Okunuşu ==> %s" % a)
                    print("Türkçesi ==> %s" % b)
                    print("1. tekil şahıs çekimi ==> %s" % c)
                    print("2. tekil şahıs çekimi ==> %s" % d)
                    print("3. tekil şahıs çekimi ==> %s" % e)
                    print("1. çoğul şahıs çekimi ==> %s" % f)
                    print("2. çoğul şahıs çekimi ==> %s" % g)
                    print("3.çoğul şahıs çekimi ==> %s" % h)
                    hoşGeldin()

def kelimevar(inp1, inp3):
    inp2 = input("%s kelime deposunda.\nDetaylı bilgi ister misin?\n" % inp1)
    if inp2 == "Evet":
        detaylıbilgi(inp1, inp3)
    if inp2 == "Hayır":
        hoşGeldin()
    else:
        print("'Evet' veya 'Hayır' olarak cevap ver.\n")
        kelimevar(inp1, inp3)

def kelimeyok(inp1):
    inp2 = input("%s kelimesi sözlükte yok.\nEklemek ister misin?\n" % inp1)
    if inp2 == "Evet":
        yeniSözcük()
    if inp2 == "Hayır":
        hoşGeldin()
    else:
        print("'Evet' veya 'Hayır' olarak cevap ver.\n")
        kelimeyok(inp1)

def kelimearat(inp2):
    if inp2 == "frkelime.txt":
        inp1 = input("Aratmak istediğin kelimeyi yaz.\n")
        if inp1 in open(inp2).read():
            kelimevar(inp1, inp2)
        else:
            kelimeyok(inp1)
    if inp2 == "frfiil.txt":
        inp1 = input("Aratmak istediğin fiili yaz.\n")
        if inp1 in open(inp2).read():
            kelimevar(inp1, inp2)
        else:
            kelimeyok(inp1)

def depoCheck():
    inp1 = input("Fiil aratmak için 'Fiil', kelime aratmak için 'Kelime' yaz.\n")
    if inp1 == "Fiil":
        kelimearat("frfiil.txt")
    if inp1 == "Kelime":
        kelimearat("frkelime.txt")
    else:
        depoCheck()

def istekNe():
    inp1 = input("Kelime aramak için 'Arat', Kelime eklemek için 'Yeni' yaz.\n")
    if inp1 == "Arat":
        depoCheck()
    elif inp1 == "Yeni":
        yeniSözcük()
    elif inp1 != "Yeni" or "Arat":
        istekNe()

def kelimeekle():
    inp1 = input("Eklemek istediğin kelimenin Fransızcasını yaz.\n")
    inp2 = input("%s kelimesinin okunuşunu yaz.\n" % inp1)
    inp3 = input("%s kelimesinin Türkçesini yaz.\n" % inp1)
    kelimeara(inp1, "frkelime.txt")
    kelimeara(inp2, "frkelime.txt")
    kelimeson(inp3, "frkelime.txt")
    kelimesözlük = ("%s : %s" % (inp1, inp3))
    kelimeson(kelimesözlük, "fr.txt")
    alfabetikSıra()
    print("Kelime eklendi...")
    hoşGeldin()

def fiilekle():
    inp1 = input("Eklemek istediğin fiilin Fransızcasını yaz.\n")
    inp2 = input("%s fiilinin okunuşunu yaz.\n" % inp1)
    inp3 = input("%s fiilinin Türkçesini yaz.\n" % inp1)
    inp4 = input("%s fiilinin çekimlemek istediğin zamanı yaz.\n" % inp1)
    inp5 = input("1. tekil şahıs çekimini yaz.\n")
    inp6 = input("2. tekil şahıs çekimini yaz.\n")
    inp7 = input("3. tekil şahıs çekimini yaz.\n")
    inp8 = input("1. çoğul şahıs çekimini yaz.\n")
    inp9 = input("2. çoğul şahıs çekimini yaz.\n")
    inp10 = input("3. çoğul şahıs çekimini yaz.\n")
    kelimeara(inp1, "frfiil.txt")
    kelimeara(inp2, "frfiil.txt")
    kelimeara(inp3, "frfiil.txt")
    kelimeara(inp4, "frfiil.txt")
    kelimeara(inp5, "frfiil.txt")
    kelimeara(inp6, "frfiil.txt")
    kelimeara(inp7, "frfiil.txt")
    kelimeara(inp8, "frfiil.txt")
    kelimeara(inp9, "frfiil.txt")
    kelimeson(inp10, "frfiil.txt")
    kelimesözlük = ("%s : %s" % (inp1, inp3))
    kelimeson(kelimesözlük, "fr.txt")
    alfabetikSıra()
    print("Fiil eklendi...")
    hoşGeldin()

def yeniSözcük():
    inp1 = input("Kelime eklemek için 'Kelime', fiil eklemek için 'Fiil' yaz.\n")
    if inp1 == "Kelime":
        kelimeekle()
    if inp1 == "Fiil":
        fiilekle()
    else:
        yeniSözcük()

def kelimeara(inp1, text):
    wlw = open(text, "a")
    wlw.write("%s\n" % inp1)

def kelimeson(inp1, text):
    wlw = open(text, "a")
    for i in range(1):
        wlw.write("%s\r\n" % inp1)

def alfabetikSıra():
    fr = list()
    with open("fr.txt") as fin:
        for line in fin:
            fr.append(line)
    fr.sort()
    with open("fr.txt", "w") as fout:
        for band in fr:
            fout.write(band)


print("Fransızca kelime deposuna hoşgeldin!\n")
hoşGeldin()
