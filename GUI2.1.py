from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
import tkinter.messagebox as mb
import webbrowser as wb
import clipboard as cb
import sys
import os

LARGE_FONT = ("Verdana", 12)
fontHeader = "Helvetica 16 bold italic"


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Dictionary(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.resizable(width=FALSE, height=FALSE)
        self.title("Fransızca-Türkçe Sözlük")
        self.geometry("800x600+283+50")
        self.decoding_tr = "utf-8"
        self.decoding_fr = "latin-1"
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.French = open("fr.txt").read().lower().split("\n")
        self.Turkish = open("tr.txt").read().lower().split("\n")
        for F in (PageWelcome, PageSearch, PageDictionary, PageCredits, PageAdd, PageAddWord, PageAddVerb):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(PageWelcome)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def check_exists(self, combo, entry, scrolledtext):
        word = entry.get()
        from_to = combo.get()
        st = scrolledtext
        language = None
        lang = None
        word = word.lower()
        st.delete(1.0, END)
        if from_to == "Türkçe ==> Fransızca" or from_to == "Fransızca ==> Türkçe":
            if from_to == "Türkçe ==> Fransızca":
                language = open("tr.txt", "r").read().lower().split("\n")
                lang = "tr"
                print(language)
            elif from_to == "Fransızca ==> Türkçe":
                language = open("fr.txt", "rb").read().decode(self.decoding_fr).lower().split("\n")
                lang = "fr"
            if word in language:
                print("1")
                text = self.print_word(word, lang)
                st.insert(END, text)
            elif ("(v)" + word) in language:
                text = self.print_verb(word, lang)
                st.insert(END, text)
            else:
                text = word + " Sözlükte bulunmuyor. Sözcüğünün yazılışından eminseniz lütfen yeni sözcük kaydı " \
                       "oluşturunuz."
                st.insert(END, text)
        else:
            text = "Lütfen dil seçiniz"
            st.insert(END, text)

    @staticmethod
    def print_verb(word, language):
        list_to_print = []
        lang = []
        if language is "tr":
            lang = ["Türkçe", "Fransızca"]
            list_to_print = open("verb\\tr\\" + word + ".txt").read().lower().split("\n")
        elif language is "fr":
            lang = ["Fransızca", "Türkçe"]
            list_to_print = open("verb\\fr\\" + word + ".txt").read().lower().split("\n")
        return word + " fiili " + lang[0] + " dilindedir, " + lang[1] + " dilinde " + list_to_print[1] + \
               " demektir. Telaffuzu " + list_to_print[2] + " şeklindedir. " + list_to_print[3] + \
               " tarafından eklenmiştir.\nIndicatif présent çekimleri:\n" + list_to_print[4] + "\n" + \
               list_to_print[5] + "\n" + list_to_print[6] + "\n" + list_to_print[7] + "\n" + list_to_print[8] + "\n" + \
               list_to_print[9] + "\nIndicatif passé composé çekimleri:\n" + list_to_print[10] + "\n" + \
               list_to_print[11] + "\n" + list_to_print[12] + "\n" + list_to_print[13] + "\n" + list_to_print[14] + \
               "\n" + list_to_print[15] + "\nIndicatif passé simple çekimleri:\n" + list_to_print[16] + "\n" + \
               list_to_print[17] + "\n" + list_to_print[18] + "\n" + list_to_print[19] + "\n" + list_to_print[20] + \
               "\n" + list_to_print[21] + "\nIndicatif futur çekimleri:\n" + list_to_print[22] + "\n" + \
               list_to_print[23] + "\n" + list_to_print[24] + "\n" + list_to_print[25] + "\n" + list_to_print[26] + \
               "\n" + list_to_print[27] + "\n"

    @staticmethod
    def print_word(word, language):
        list_to_print = []
        lang = []
        if language is "tr":
            lang = ["Türkçe", "Fransızca"]
            list_to_print = open("word\\tr\\" + word + ".txt").read().lower().split("\n")
            print(list_to_print)
        elif language is "fr":
            lang = ["Fransızca", "Türkçe"]
            list_to_print = open("word\\fr\\" + word + ".txt").read().lower().split("\n")
        return word + " kelimesi " + lang[0] + " dilindedir, " + lang[1] + " dilinde " + list_to_print[2] + \
               " demektir. Telaffuzu " + list_to_print[1] + " şeklindedir.\n" + list_to_print[3] + \
               " tarafından eklenmiştir."

    @staticmethod
    def add_word(turkish, french, pronounciation, adder):
        tr = turkish.get()
        fr = french.get()
        p = pronounciation.get()
        a = adder.get()
        open("tr.txt", "a").write(tr + "\n")
        open("fr.txt", "a").write(fr + "\n")
        open("word\\tr\\" + tr + ".txt", "w+").write(tr + "\n" + p + "\n" + fr + "\n" + a)
        open("word\\fr\\" + fr + ".txt", "w+").write(fr + "\n" + p + "\n" + tr + "\n" + a)
        mb.showinfo(title="Kelime eklendi", message="Kelime başarı ile eklendi")

    @staticmethod
    def add_verb(tr_fr_p_a, list_of):
        filetr = open("verb\\tr\\" + tr_fr_p_a[0].get() + ".txt", "a+")
        filefr = open("verb\\fr\\" + tr_fr_p_a[1].get() + ".txt", "a+")
        for i in range(2):
            filetr.write("%s\n" % tr_fr_p_a[i + 2].get())
            filefr.write("%s\n" % tr_fr_p_a[i + 2].get())
        for i in range(len(list_of)):
            filetr.write("%s\n" % list_of[i].get())
            filefr.write("%s\n" % list_of[i].get())
        filetr.close()
        filefr.close()
        tr = open("tr.txt", "a+")
        tr.write("(v)%s\n" % tr_fr_p_a[0].get())
        tr.close()
        fr = open("fr.txt", "a+")
        fr.write("(v)%s\n" % tr_fr_p_a[1].get())
        fr.close()
        mb.showinfo(title="Fiil eklendi", message="Fiil başarı ile eklendi")


def open_site(url):
    wb.open_new_tab(url)


def on_closing():
    if mb.askyesno("Çıkmak istediğinize emin misiniz?", "Çıkmak istediğinize emin misiniz?"):
        app.destroy()


def support_me():
    if mb.askyesno(title="Bağış yapmak ister misiniz?", message="Bağış yapmak ister misiniz?"):
        mb.showinfo(title="Bağış Yap", message="EFT ile bağış yapabilirsiniz.\n" +
                                               "EFT'nin yapılacağı banka: ING BANK - Banka Kodu: 99\n" +
                                               "Şube: İstanbul / Genel Müdürlük - Şube Kodu: 1\n" +
                                               "Alıcı hesap no: 5157 5570 2193 8385\n" +
                                               "Alıcı isim - Soyisim: Ahmet Ertuğrul KAYA\n" +
                                               "Tutar: 300 TLye kadar para gönderebilirsiniz\n" +
                                               "NOT: Tamam'a basmaya devam edin ve otomatik" +
                                               " olarak bilgiler kopyalanacaktır.")
        cb.copy("ING BANK")
        mb.showinfo(title="Kopyalandı", message="Banka adı: ING BANK")
        cb.copy("99")
        mb.showinfo(title="Kopyalandı", message="Banka kodu: 99")
        cb.copy("5157 5570 2193 8385")
        mb.showinfo(title="Kopyalandı", message="Alıcı hesap no: 5157 5570 2193 8385")
        cb.copy("Ahmet Ertuğrul KAYA")
        mb.showinfo(title="Kopyalandı", message="Alıcı isim - Soyisim: Ahmet Ertuğrul KAYA")
        mb.showinfo(title="Destekleriniz için teşekkür ederim", message="Projelerimi desteklediğiniz için teşekkürler.")
    else:
        mb.showinfo(title="Bağış yapmak ister misin?", message="Umarım bir dahaki sefere destek olabilirsiniz.")


class PageWelcome(Frame):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self, parent)
        label1 = Label(self, text="FRANSIZCA-TÜRKÇE SÖZLÜĞÜNE HOŞGELDİNİZ", font=fontHeader)
        label1.place(x=150, y=90)
        label2 = Label(self, text="Başlamak için 'Başla'ya, sözlüğü görmek için 'Sözlük'e, çıkmak için 'Çık'a basınız.")
        label2.place(x=185, y=160)
        button1 = Button(self, text="Başla", width=10, command=lambda: controller.show_frame(PageSearch))
        button1.place(x=130, y=225)
        button2 = Button(self, text="Sözlük", width=10, command=lambda: controller.show_frame(PageDictionary))
        button2.place(x=360, y=225)
        button3 = Button(self, text="Hakkımda", width=10, command=lambda: controller.show_frame(PageCredits))
        button3.place(x=721, y=574)
        button4 = Button(self, text="Çık", width=10, command=lambda: on_closing())
        button4.place(x=610, y=225)


class PageSearch(Frame):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self, parent)
        label = Label(self, text="E-SÖZLÜK", font=fontHeader)
        label.place(x=330, y=40)
        label2 = Label(self, text="Kelimeyi yazdıktan sonra aratabilir veya yeni kelime ekleyebilirsiniz.")
        label2.place(x=215, y=90)
        entry1 = Entry(self, width=21)
        entry1.place(x=130, y=200)
        v = ["Türkçe ==> Fransızca", "Fransızca ==> Türkçe"]
        combo1 = Combobox(self, values=v, width=21)
        combo1.set("Çeviri dilini seçiniz")
        combo1.bind("<Key>", "break")
        combo1.place(x=580, y=200)
        stext1 = ScrolledText(self, width=50, height=20)
        stext1.place(x=210, y=265)
        stext1.config(wrap=WORD)
        stext1.bind("<Key>", "break")
        button1 = Button(self, text="Çevir", command=lambda: controller.check_exists(combo1, entry1, stext1))
        button1.place(x=360, y=210)
        button2 = Button(self, text="Ekle", width=10, command=lambda: controller.show_frame(PageAdd))
        button2.place(x=130, y=120)
        button3 = Button(self, text="Ana Sayfa", width=10, command=lambda: controller.show_frame(PageWelcome))
        button3.place(x=360, y=120)
        button4 = Button(self, text="Çık", width=10, command=lambda: on_closing())
        button4.place(x=580, y=120)


class PageDictionary(Frame):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self, parent)
        label1 = Label(self, text="İÇİNDEKİLER", font=fontHeader)
        label1.place(x=330, y=30)
        label2 = Label(self, text="Daha fazlası için web sayfam ==> pathjuk.tk")
        label2.place(x=290, y=80)
        button1 = Button(self, text="Ana Sayfa", width=10, command=lambda: controller.show_frame(PageWelcome))
        button1.place(x=130, y=120)
        button2 = Button(self, text="Arat", width=10, command=lambda: controller.show_frame(PageSearch))
        button2.place(x=360, y=120)
        button3 = Button(self, text="Çık", width=10, command=lambda: on_closing())
        button3.place(x=580, y=120)
        text = open("hepsi.txt").read()
        scrolledtext = ScrolledText(self, width=50, height=20)
        scrolledtext.place(x=200, y=200)
        scrolledtext.bind("<Key>", lambda e: "break")
        scrolledtext.insert(END, text)
        scrolledtext.config(wrap=WORD)


class PageCredits(Frame):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self, parent)
        label1 = Label(self, text="HAKKIMDA", font=fontHeader)
        label1.place(x=350, y=50)
        label2 = Label(self, text="Daha fazlası için web sayfam ==> pathjuk.tk")
        label2.place(x=290, y=110)
        button1 = Button(self, text="pathjuk.tk", width=10, command=lambda: open_site("www.pathjuk.tk"))
        button1.place(x=380, y=150)
        button2 = Button(self, text="Ana Sayfa", width=10, command=lambda: controller.show_frame(PageWelcome))
        button2.place(x=280, y=210)
        button3 = Button(self, text="Çık", width=10, command=lambda: on_closing())
        button3.place(x=480, y=210)
        button4 = Button(self, text="Destek ol", width=10, command=lambda: support_me())
        button4.place(x=721, y=574)
        scrolledtext = ScrolledText(self, width=50, height=20)
        text = open("hakkımda.txt").read()
        scrolledtext.place(x=210, y=265)
        scrolledtext.bind("<Key>", lambda e: "break")
        scrolledtext.insert(END, text)
        scrolledtext.config(wrap=WORD)


class PageAdd(Frame):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self, parent)
        label1 = Label(self, text="SÖZCÜK EKLE", font=fontHeader)
        label1.place(x=320, y=70)
        label2 = Label(self, text="Eklemek istediğiniz sözcüğün türünü seçiniz.")
        label2.place(x=250, y=140)
        button1 = Button(self, text="Arat", width=10, command=lambda: controller.show_frame(PageSearch))
        button1.place(x=185, y=190)
        button2 = Button(self, text="Ana Sayfa", width=10, command=lambda: controller.show_frame(PageWelcome))
        button2.place(x=360, y=190)
        button3 = Button(self, text="Çık", width=10, command=lambda: on_closing())
        button3.place(x=535, y=190)
        button4 = Button(self, text="Kelime", width=10, command=lambda: controller.show_frame(PageAddWord))
        button4.place(x=280, y=300)
        button5 = Button(self, text="Fiil", width=10, command=lambda: controller.show_frame(PageAddVerb))
        button5.place(x=455, y=300)


class PageAddWord(Frame):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self, parent)
        label1 = Label(self, text="KELİME EKLE", font=fontHeader)
        label1.place(x=320, y=60)
        label2 = Label(self, text="Aşağıdaki formu doldurunuz")
        label2.place(x=310, y=120)
        button1 = Button(self, text="Arat", width=10, command=lambda: controller.show_frame(PageSearch))
        button1.place(x=185, y=170)
        button2 = Button(self, text="Ana Sayfa", width=10, command=lambda: controller.show_frame(PageWelcome))
        button2.place(x=360, y=170)
        button3 = Button(self, text="Çık", width=10, command=lambda: on_closing())
        button3.place(x=535, y=170)
        x = 330
        y = 200
        y_accrual = 25
        label3 = Label(self, text="Fransızca")
        label3.place(x=x, y=y + y_accrual)
        entry1 = Entry(self, width=21)
        entry1.place(x=x, y=y + (2 * y_accrual))
        label4 = Label(self, text="Türkçe")
        label4.place(x=x, y=y + (3 * y_accrual))
        entry2 = Entry(self, width=21)
        entry2.place(x=x, y=y + (4 * y_accrual))
        label5 = Label(self, text="Telaffuz")
        label5.place(x=x, y=y + (5 * y_accrual))
        entry3 = Entry(self, width=21)
        entry3.place(x=x, y=y + (6 * y_accrual))
        label6 = Label(self, text="Ekleyen kişi?")
        label6.place(x=x, y=y + (7 * y_accrual))
        entry4 = Entry(self, width=21)
        entry4.place(x=x, y=y + (8 * y_accrual))
        button4 = Button(self, text="Ekle", width=10, command=lambda: controller.add_word(entry2, entry1,
                                                                                          entry3, entry4))
        button4.place(x=x, y=y + (9 * y_accrual))


class PageAddVerb(Frame):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self, parent)
        button1 = Button(self, text="Arat", width=10, command=lambda: controller.show_frame(PageSearch))
        button1.place(x=170, y=140)
        button2 = Button(self, text="Ana Sayfa", width=10, command=lambda: controller.show_frame(PageWelcome))
        button2.place(x=350, y=140)
        button3 = Button(self, text="Çık", width=10, command=lambda: on_closing())
        button3.place(x=540, y=140)

        #Ekleyen Fransızca Türkçe Telaffuz
        entry1 = Entry(self, width=15)
        entry1.place(x=30, y=280)
        entry2 = Entry(self, width=15)
        entry2.place(x=30, y=330)
        entry3 = Entry(self, width=15)
        entry3.place(x=30, y=380)
        entry4 =Entry(self, width=15)
        entry4.place(x=30, y=430)

        #Indicatif Présent
        entry5 = Entry(self, width=15)
        entry5.place(x=170, y=240)
        entry6 = Entry(self, width=15)
        entry6.place(x=170, y=290)
        entry7 = Entry(self, width=15)
        entry7.place(x=170, y=340)
        entry8 = Entry(self, width=15)
        entry8.place(x=170, y=390)
        entry9 = Entry(self, width=15)
        entry9.place(x=170, y=440)
        entry10 = Entry(self, width=15)
        entry10.place(x=170, y=490)

        #Indicatif Passé Composé
        entry11 = Entry(self, width=15)
        entry11.place(x=320, y=240)
        entry12 = Entry(self, width=15)
        entry12.place(x=320, y=290)
        entry13 = Entry(self, width=15)
        entry13.place(x=320, y=340)
        entry14 = Entry(self, width=15)
        entry14.place(x=320, y=390)
        entry15 = Entry(self, width=15)
        entry15.place(x=320, y=440)
        entry16 = Entry(self, width=15)
        entry16.place(x=320, y=490)

        #Indicatif Passé Simple
        entry17 = Entry(self, width=15)
        entry17.place(x=480, y=240)
        entry18 = Entry(self, width=15)
        entry18.place(x=480, y=290)
        entry19 = Entry(self, width=15)
        entry19.place(x=480, y=340)
        entry20 = Entry(self, width=15)
        entry20.place(x=480, y=390)
        entry21 = Entry(self, width=15)
        entry21.place(x=480, y=440)
        entry22 = Entry(self, width=15)
        entry22.place(x=480, y=490)

        #Indicatif futur
        entry23 = Entry(self, width=15)
        entry23.place(x=640, y=240)
        entry24 = Entry(self, width=15)
        entry24.place(x=640, y=290)
        entry25 = Entry(self, width=15)
        entry25.place(x=640, y=340)
        entry26 = Entry(self, width=15)
        entry26.place(x=640, y=390)
        entry27 = Entry(self, width=15)
        entry27.place(x=640, y=440)
        entry28 = Entry(self, width=15)
        entry28.place(x=640, y=490)

        #add_verb bileşenleri
        tr_fr_p_a = [entry3, entry2, entry4, entry1]
        list_of = [entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13, entry14, entry15, entry16, 
                   entry17, entry18, entry19, entry20, entry21, entry22, entry23, entry24, entry25, entry26, entry27, entry28]

        #Hepsini bağla
        button4 = Button(self, text="Ekle", width=10, command=lambda: controller.add_verb(tr_fr_p_a=tr_fr_p_a, list_of=list_of))
        button4.place(x=50, y=470)

        label1 = Label(self, text="FİİL EKLE", font=fontHeader)
        label1.place(x=290, y=40)
        label2 = Label(self, text="Aşağıdaki formu doldurunuz")
        label2.place(x=310, y=80)
        label3 = Label(self, text="Indicatif Présent")
        label3.place(x=180, y=190)
        label4 = Label(self, text="Indicatif Passé Composé")
        label4.place(x=320, y=190)
        label5 = Label(self, text="Indicatif Passé Simple")
        label5.place(x=480, y=190)
        label6 = Label(self, text="Indicatif futur")
        label6.place(x=660, y=190)
        label7 = Label(self, text="Ekleyen")
        label7.place(x=70, y=260)
        label8 = Label(self, text="Fransızca")
        label8.place(x=60, y=310)
        label9 = Label(self, text="Türkçe")
        label9.place(x=70, y=360)
        label10 = Label(self, text="Telaffuz")
        label10.place(x=70, y=410)
        label11 = Label(self, text="Je")
        label11.place(x=220, y=220)
        label12 = Label(self, text="Tu")
        label12.place(x=220, y=270)
        label13 = Label(self, text="Il/Elle")
        label13.place(x=220, y=320)
        label14 = Label(self, text="Nous")
        label14.place(x=220, y=370)
        label15 = Label(self, text="Vous")
        label15.place(x=220, y=420)
        label16 = Label(self, text="Ils/Elles")
        label16.place(x=220, y=470)
        label17 = Label(self, text="Je")
        label17.place(x=370, y=220)
        label18 = Label(self, text="Tu")
        label18.place(x=370, y=270)
        label19 = Label(self, text="Il/Elle")
        label19.place(x=370, y=320)
        label20 = Label(self, text="Nous")
        label20.place(x=370, y=370)
        label21 = Label(self, text="Vous")
        label21.place(x=370, y=420)
        label22 = Label(self, text="Ils/Elles")
        label22.place(x=370, y=470)        
        label23 = Label(self, text="Je")
        label23.place(x=530, y=220)
        label24 = Label(self, text="Tu")
        label24.place(x=530, y=270)
        label25 = Label(self, text="Il/Elle")
        label25.place(x=530, y=320)
        label26 = Label(self, text="Nous")
        label26.place(x=530, y=370)
        label27 = Label(self, text="Vous")
        label27.place(x=530, y=420)
        label28 = Label(self, text="Ils/Elles")
        label28.place(x=530, y=470)
        label29 = Label(self, text="Je")
        label29.place(x=680, y=220)
        label30 = Label(self, text="Tu")
        label30.place(x=680, y=270)
        label31 = Label(self, text="Il/Elle")
        label31.place(x=680, y=320)
        label32 = Label(self, text="Nous")
        label32.place(x=680, y=370)
        label33 = Label(self, text="Vous")
        label33.place(x=680, y=420)
        label34 = Label(self, text="Ils/Elles")
        label34.place(x=680, y=470)


app = Dictionary()

app.wm_protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
