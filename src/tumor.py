#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 09, 2019 01:13:40 AM IST  platform: Linux

import sys
from tkinter import messagebox
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

import tumor_support

def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	top = tumor (root)
	tumor_support.init(root, top)
	root.lift()
	root.wm_attributes('-topmost',True)
	root.after_idle(root.attributes,'-topmost',False)
	root.mainloop()

w = None
def create_tumor(root, *args, **kwargs):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = tk.Toplevel (root)
	top = tumor (w)
	tumor_support.init(w, top, *args, **kwargs)
	return (w, top)

def destroy_tumor():
	global w
	w.destroy()
	w = None

class tumor:
	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		self.style = ttk.Style()
		if sys.platform == "win32":
			self.style.theme_use('winnative')
		self.style.configure('.',background=_bgcolor)
		self.style.configure('.',foreground=_fgcolor)
		self.style.map('.',background=
			[('selected', _compcolor), ('active',_ana2color)])

		top.geometry("600x450+521+160")
		top.title("Tumor Estimation")
		top.configure(highlightcolor="black")

		self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
		top.configure(menu = self.menubar)

		self.sub_menu = tk.Menu(top,tearoff=0)
		self.menubar.add_cascade(menu=self.sub_menu,
				activebackground="#ececec",
				activeforeground="#000000",
				background="#d9d9d9",
				font="TkMenuFont",
				foreground="#000000",
				label="File")
		self.sub_menu.add_command(label = 'Open_Dir',command = lambda : tumor_support.tumor_dir())
		
		self.files_list = ScrolledListBox(top)
		self.files_list.place(relx=0.217, rely=0.111, relheight=0.773
				, relwidth=0.443)
		self.files_list.configure(background="white")
		self.files_list.configure(font="TkFixedFont")
		self.files_list.configure(highlightcolor="#d9d9d9")
		self.files_list.configure(selectbackground="#c4c4c4")
		self.files_list.configure(takefocus="0")
		self.files_list.configure(width=10)
		self.files_list.bind('<<ListboxSelect>>',lambda e: self.click(e))

		self.Button1 = tk.Button(top)
		self.Button1.place(relx=0.7, rely=0.356, height=31, width=64)
		self.Button1.configure(takefocus="0")
		self.Button1.configure(text='''LOAD''')
		self.Button1.configure(command = self.file_l)
		
		self.Button2 = tk.Button(top)
		self.Button2.place(relx=0.7, rely=0.511, height=41, width=71)
		self.Button2.configure(text='''SAVE''')
		self.Button2.configure(width=71)
		self.Button2.configure(command = tumor_support.save_stuff)

		self.Button3 = tk.Button(top)
		self.Button3.place(relx=0.367, rely=0.867, height=41, width=181)
		self.Button3.configure(text='''Calculate Volume''')
		self.Button3.configure(width=181)
		self.Button3.configure(command = tumor_support.calc_vol)

	def file_l(self):
		# print(tumor_support.file_list)
		lis = tumor_support.file_list
		for l in lis.keys():
			self.files_list.insert('end',(l ,"\t\t\t",lis[l]))

		

	def click(self,e): 	
		print("click")
		lol = e.widget
		idx = lol.curselection()
		print("select",idx[0])
		value = lol.get(idx[0])
		value = value[0]
		print(value)
		res = tumor_support.draw_on_it(value)
		print("back with",res)
		lol.delete(idx[0])
		lol.insert(idx[0],(value,"\t\t\t\t",res))


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
	'''Configure the scrollbars for a widget.'''

	def __init__(self, master):
		#  Rozen. Added the try-except clauses so that this class
		#  could be used for scrolled entry widget for which vertical
		#  scrolling is not supported. 5/7/14.
		try:
			vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
		except:
			pass
		hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

		#self.configure(yscrollcommand=_autoscroll(vsb),
		#    xscrollcommand=_autoscroll(hsb))
		try:
			self.configure(yscrollcommand=self._autoscroll(vsb))
		except:
			pass
		self.configure(xscrollcommand=self._autoscroll(hsb))

		self.grid(column=0, row=0, sticky='nsew')
		try:
			vsb.grid(column=1, row=0, sticky='ns')
		except:
			pass
		hsb.grid(column=0, row=1, sticky='ew')

		master.grid_columnconfigure(0, weight=1)
		master.grid_rowconfigure(0, weight=1)

		# Copy geometry methods of master  (taken from ScrolledText.py)
		if py3:
			methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
				  | tk.Place.__dict__.keys()
		else:
			methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
				  + tk.Place.__dict__.keys()

		for meth in methods:
			if meth[0] != '_' and meth not in ('config', 'configure'):
				setattr(self, meth, getattr(master, meth))

	@staticmethod
	def _autoscroll(sbar):
		'''Hide and show scrollbar as needed.'''
		def wrapped(first, last):
			first, last = float(first), float(last)
			if first <= 0 and last >= 1:
				sbar.grid_remove()
			else:
				sbar.grid()
			sbar.set(first, last)
		return wrapped

	def __str__(self):
		return str(self.master)

def _create_container(func):
	'''Creates a ttk Frame with a given master, and use this new frame to
	place the scrollbars and the widget.'''
	def wrapped(cls, master, **kw):
		container = ttk.Frame(master)
		container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
		container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
		return func(cls, container, **kw)
	return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
	'''A standard Tkinter Text widget with scrollbars that will
	automatically show/hide as needed.'''
	@_create_container
	def __init__(self, master, **kw):
		tk.Listbox.__init__(self, master, **kw)
		AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
	child = widget.winfo_children()[0]
	if platform.system() == 'Windows' or platform.system() == 'Darwin':
		child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
		child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
	else:
		child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
		child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
		child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
		child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
	if platform.system() == 'Windows' or platform.system() == 'Darwin':
		widget.unbind_all('<MouseWheel>')
		widget.unbind_all('<Shift-MouseWheel>')
	else:
		widget.unbind_all('<Button-4>')
		widget.unbind_all('<Button-5>')
		widget.unbind_all('<Shift-Button-4>')
		widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
	if platform.system() == 'Windows':
		widget.yview_scroll(-1*int(event.delta/120),'units')
	elif platform.system() == 'Darwin':
		widget.yview_scroll(-1*int(event.delta),'units')
	else:
		if event.num == 4:
			widget.yview_scroll(-1, 'units')
		elif event.num == 5:
			widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
	if platform.system() == 'Windows':
		widget.xview_scroll(-1*int(event.delta/120), 'units')
	elif platform.system() == 'Darwin':
		widget.xview_scroll(-1*int(event.delta), 'units')
	else:
		if event.num == 4:
			widget.xview_scroll(-1, 'units')
		elif event.num == 5:
			widget.xview_scroll(1, 'units')

if __name__ == '__main__':
	vp_start_gui()





