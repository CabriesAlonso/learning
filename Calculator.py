import tkinter as tk
def topla():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc ['text'] = str(s1+s2)
def cikar():
    s1 = int (sayi1.get())
    s2 = int (sayi2.get())
    sonuc ['text'] = str(s1-s2)
def carp():
    s1 = int (sayi1.get())
    s2 = int (sayi2.get())
    sonuc ['text'] = str(s1*s2)
def bol():
    s1 = float (sayi1.get())
    s2 = float (sayi2.get())
    sonuc ['text'] = str(s1/s2) 




pencere = tk.Tk()
pencere.title("Hesap Makinesi"),
pencere.geometry("300x300")

sayi1 = tk.Entry(width=10)
sayi1.place(x=10,y=20)
sayi2 = tk.Entry(width=10)
sayi2.place(x=100,y=20)

sonuc = tk.Label(text="Sonuc",fg="red",bg="white",font="Verdana 10 bold",width=10)
sonuc.place(x=200,y=20)

toplab = tk.Button(text="+",width=5,command=topla)
toplab.place(x=20,y=50)
cikarb = tk.Button(text="-",width=5,command=cikar)
cikarb.place(x=70,y=50)
carpb = tk.Button(text="*",width=5,command=carp)
carpb.place(x=120,y=50)
bolb = tk.Button(text="/",width=5,command=bol)
bolb.place(x=170,y=50)




pencere.mainloop()