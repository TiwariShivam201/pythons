from tkinter import*
import tkinter.messagebox
master=Tk()
#master.title("TikTakToe"')
click=True
def chaker(buttons):
	global click
	if buttons["text"]==" " and click==True:
		buttons["text"]="X"
		click=False
	elif buttons["text"]==" " and click==False:
		buttons["text"]="O"
		click=True
	elif (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" or button1["text"]=="X" and button3["text"]=="X" and button7["text"]=="X" or button2["text"]=="X" and button4["text"]=="X" and button6["text"]=="X" or button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
		tkinter.messagebox.showinfo("Winner X","You have just won a game")
		
	elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" or button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
		tkinter.messagebox.showinfo("Winner O","You have won just a game")
		
			
		
									
		
buttons=StringVar()

button1=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button1))
button1.grid(row=1,column=0)
button2=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button2))
button2.grid(row=1,column=1)
button3=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button3))
button3.grid(row=1,column=2)
button4=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button4))
button4.grid(row=2,column=0)
button5=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button5))
button5.grid(row=2,column=1)
button6=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button6))
button6.grid(row=2,column=2)
button7=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button7))
button7.grid(row=3,column=0)
button8=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button8))
button8.grid(row=3,column=1)
button9=Button(master,text=" ",font=('Times 26 bold'),height=1,width=2,command=lambda:chaker(button9))
button9.grid(row=3,column=2)

Label(master,text="First Hit=X",font=('Times 7 bold')).grid(row=5,column=1)
Label(master,text="Second Hit=O",font=('Times 7 bold')).grid(row=6,column=1)



mainloop()
