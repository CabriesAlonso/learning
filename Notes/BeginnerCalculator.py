import tkinter as tk

def add():
    c1 = int(count1.get())
    c2 = int(count2.get())
    result ['text'] = str(c1+c2)
def sub():
    c1 = int (count1.get())
    c2 = int (count2.get())
    result ['text'] = str(c1-c2)
def multip():
    c1 = int (count1.get())
    c2 = int (count2.get())
    result ['text'] = str(c1*c2)
def div():
    c1 = float (count1.get())
    c2 = float (count2.get())
    result ['text'] = str(c1/c2) 


window = tk.Tk()
window.title("Calculator"),
window.geometry("300x300")

count1 = tk.Entry(width=10)
count1.place(x=10,y=20)
count2 = tk.Entry(width=10)
count2.place(x=100,y=20)

result = tk.Label(text="Result",fg="red",bg="white",font="Verdana 10 bold",width=10)
result.place(x=200,y=20)

addb = tk.Button(text="+",width=5,command=add)
addb.place(x=20,y=50)
subb = tk.Button(text="-",width=5,command=sub)
subb.place(x=70,y=50)
multb = tk.Button(text="*",width=5,command=multip)
multb.place(x=120,y=50)
divb = tk.Button(text="/",width=5,command=div)
divb.place(x=170,y=50)




window.mainloop()
