"""
Simple on-screen keyboard using tkinter
Author : Ajinkya Padwad
Version 1.0
"""

from tkinter import *
import tkinter

kb = tkinter.Tk()

buttons = [
'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\\','7','8','9','BACK',
'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','[',']','4','5','6'
,'SHIFT',
'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','?','/','1','2','3','SPACE',
]

def select(value):
	if value == "BACK":
		entry2 = entry.get()
		pos = entry2.find(" ")
		pos2=entry2[pos:]
		entry.delete(pos2, tkinter.END)
	elif value == "SPACE":
		entry.insert(tkinter.END, ' ')
	elif value == " Tab ":
		entry.insert(tkinter.END, '    ')
	else :
		entry.insert(tkinter.END,value)



def HosoPop():

	varRow = 2
	varColumn = 0

	for button in buttons:

		command = lambda x=button: select(x)
		
		if button == "SPACE" or button == "SHIFT" or button == "BACK":
			tkinter.Button(kb,text= button,width=6, bg="#3c4987", fg="#ffffff",
				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
				pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)

		else:
			tkinter.Button(kb,text= button,width=4, bg="#3c4987", fg="#ffffff",
				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
				pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)


		varColumn +=1 

		if varColumn > 14 and varRow == 2:
			varColumn = 0
			varRow+=1
		if varColumn > 14 and varRow ==3:
			varColumn = 0
			varRow+=1

def main():

	
	kb.title("HosoKeys")
	kb.resizable(0,0)
	

	label1 = Label(kb,text='               ').grid(row=0,columnspan=15)

	global entry
	entry = Entry(kb,width=50)
	entry.grid(row=1,columnspan=15)
	# entry.pack()

	entry.bind("<Button-1>", lambda e: HosoPop())

	kb.mainloop()

main()