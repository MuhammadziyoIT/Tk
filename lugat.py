from tkinter import*
lugat={
	'ism':'name',
	'famailiya':'forneme',
	"salom": "hello",
	"dunyo": "world",
	"hayot": "life",
	"deraza":"window",
	"qogirchoq":"barbie",
}

oyna=Tk()

oyna.geometry('600x500')

entry=Entry(oyna)
entry.place(x=100,y=40,width=100,height=35)
label=Label(oyna,bg="white",fg="black")
label.place(x=350,y=60)
def ol():
	label.config(text=entry.get(),bg='white',fg="black")
	if len(entry.get())==0:
		label.config(text="Biron narsa kiriting",bg='white',fg="red")

	if  entry==lugat:
		bll=Label(oyna,text=lugat.get())
		bll.place(x=100,y=300)
	else:
		lbl=Label(oyna,text="Bunday narsa yoq")
		lbl.place(x=10,y=200)
		lugat.get("ism",default="mavjud emas")

	
olish=Button(oyna,text="olish",bg="yellow",command=ol)
olish.place(x=300,y=40)
oyna.mainloop()