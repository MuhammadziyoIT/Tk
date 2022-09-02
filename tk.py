from tkinter import*
oyna=Tk()
oyna.title("Ranglar dasturi")
oyna.maxsize(600,500)
oyna.minsize(600,500)


def qizil():
	oyna.config(bg='red')

def oq():
	oyna.config(bg='white')

def qora():
	oyna.config(bg='black')

def kok():
	oyna.config(bg='blue')
def pink():
	oyna.config(bg='pink')


def violet():
	oyna.config(bg='violet')

def orange():
	oyna.config(bg='orange')

def kulirang():
	oyna.config(bg='#96948f')


button1=Button(oyna,text="Qizil",bg="red",command=qizil)
button1.place(x=60,y=100,width=60,height=30)

button2=Button(oyna,text="Oq",bg="white",command=oq)
button2.place(x=60,y=150,width=60,height=30)

button3=Button(oyna,text="Qora",bg="black",command=qora,fg='#333')
button3.place(x=60,y=200,width=60,height=30)

button4=Button(oyna,text="kok",bg="blue",command=kok)
button4.place(x=60,y=250,width=60,height=30)

button5=Button(oyna,text="pink",bg="pink",command=pink)
button5.place(x=200,y=100,width=60,height=30)

button6=Button(oyna,text="Siyoh rang",bg="violet",command=violet)
button6.place(x=300,y=100,width=60,height=30)

button7=Button(oyna,text="Sabzi rang",bg="orange",command=orange)
button7.place(x=400,y=100,width=60,height=30)

button8=Button(oyna,text="kuli rang",bg="#96948f",command=kulirang)
button8.place(x=500,y=100,width=60,height=30)

oyna.mainloop()