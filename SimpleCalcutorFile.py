from tkinter import*
master=Tk()
Label(master,text="Enter first number:").grid(row=0)
Label(master,text="Enter Second number:").grid(row=1)
Label(master,text="Output:").grid(row=4)

e3=StringVar(master)
e4=StringVar(master)
e5=StringVar(master)
e1=Entry(master,textvariable=e3)
e2=Entry(master,textvariable=e4)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def addition():
	x=float(e1.get())
	y=float(e2.get())
	d=x+y
	output.insert(END,str(d)+"\n")
	
def subtration():
	x=float(e1.get())
	y=float(e2.get())
	d=x-y
	output.insert(END,str(d)+"\n")
	
def multication():
	x=float(e1.get())
	y=float(e2.get())
	d=x*y
	output.insert(END,str(d)+"\n")
	
def divition():
	x=float(e1.get())
	y=float(e2.get())
	d=x/y
	output.insert(END,str(d)+"\n")
	
def clear():
	e3.set(' ')
	e4.set(' ')
	
	

output=Text(master,width=9,height=10)
output.grid(row=4,column=1)

Button(master,text="ADD",command=addition).grid(row=2,column=0)
Button(master,text="SUB",command=subtration).grid(row=2,column=1)
Button(master,text="MULTI",command=multication).grid(row=3,column=0)
Button(master,text="DIV",command=divition).grid(row=3,column=1)
Button(master,text="Quit",command=master.quit,bg='red').grid(row=6,column=1)
Button(master,text="Clear",command=clear,bg="white").grid(row=5,column=0)



mainloop()


