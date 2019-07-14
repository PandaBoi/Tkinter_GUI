#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 11, 2019 01:31:55 AM IST  platform: Linux

import sys

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

try:
	import ttk
	py3 = False
except ImportError:
	import tkinter.ttk as ttk
	py3 = True

import orbital_support
from tkinter import messagebox

def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	top = orbital (root)
	orbital_support.init(root, top)
	root.lift()
	root.wm_attributes('-topmost',True)
	root.after_idle(root.attributes,'-topmost',False)
	root.mainloop()

w = None
def create_orbital(root, *args, **kwargs):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = tk.Toplevel (root)
	top = orbital (w)
	orbital_support.init(w, top, *args, **kwargs)
	return (w, top)

def destroy_Toplevel1():
	global w
	w.destroy()
	w = None

class orbital:

	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'

		top.geometry("600x450+719+255")
		top.title("Orbital")
		top.configure(background="#b14fe2")
		top.configure(highlightcolor="black")

		self.Frame1 = tk.Frame(top)
		self.Frame1.place(relx=0.017, rely=0.089, relheight=0.878
				, relwidth=0.958)
		self.Frame1.configure(relief='groove')
		self.Frame1.configure(borderwidth="2")
		self.Frame1.configure(relief="groove")
		self.Frame1.configure(background="#52c6d8")
		self.Frame1.configure(width=575)

		self.Listbox1 = tk.Listbox(self.Frame1)
		self.Listbox1.place(relx=0.104, rely=0.177, relheight=0.471
				, relwidth=0.407)
		self.Listbox1.configure(background="white")
		self.Listbox1.configure(font="TkFixedFont")
		self.Listbox1.configure(selectbackground="#c4c4c4")
		self.Listbox1.configure(width=234)
		self.Listbox1.bind('<<ListboxSelect>>',lambda e: self.click(e))

		self.Button1 = tk.Button(self.Frame1)
		self.Button1.place(relx=0.643, rely=0.228, height=41, width=81)
		self.Button1.configure(text='''LOAD''')
		self.Button1.configure(width=81)
		self.Button1.configure(command = self.file_l)

		self.Button2 = tk.Button(self.Frame1)
		self.Button2.place(relx=0.643, rely=0.506, height=41, width=81)
		self.Button2.configure(activebackground="#f9f9f9")
		self.Button2.configure(text='''SAVE''')
		self.Button2.configure(command = orbital_support.save_stuff)
		
		self.Button3 = tk.Button(self.Frame1)
		self.Button3.place(relx=0.313, rely=0.734, height=61, width=161)
		self.Button3.configure(text='''Calculate Volume''')
		self.Button3.configure(width=161)
		self.Button3.configure(command = orbital_support.calc_vol)

		self.menubar = tk.Menu(top,font="TkMenuFont",bg='#d8d8ba',fg=_fgcolor)
		top.configure(menu = self.menubar)

		self.sub_menu = tk.Menu(top,tearoff=0)
		self.menubar.add_cascade(menu=self.sub_menu,
				activebackground="#ececec",
				activeforeground="#000000",
				background="#d87c66",
				compound="left",
				font="TkMenuFont",
				foreground="#000000",
				label="File")
		self.sub_menu.add_command(command = orbital_support.open_file,
				activebackground="#ececec",
				activeforeground="#000000",
				background="#d9d9d9",
				compound="left",
				font="TkMenuFont",
				foreground="#000000",
				label="Open File")

	def file_l(self):
		# print(tumor_support.file_list)
		self.Listbox1.delete('0','end')
		lis = orbital_support.files_list
		for l in lis.keys():
			self.Listbox1.insert('end',(l ,"=>=>=>=>",lis[l]))

	def click(self,e): 	
		print("click")
		# try:
		lol = e.widget
		idx = lol.curselection()
		print("select",idx[0])
		value = lol.get(idx[0])
		value = value[0]
		print(value)
		res = orbital_support.draw_orb(value)
		print("back with",res)
		lol.delete(idx[0])
		lol.insert(idx[0],(value,"=>=>=>=>",res))
		# except Exception as ex:
		# 	print("error", type(ex).__name__)
			
		# 	messagebox.showinfo('Error',"Please make a vaild selection")




if __name__ == '__main__':
	vp_start_gui()




