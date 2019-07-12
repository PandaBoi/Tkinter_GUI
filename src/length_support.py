#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 12, 2019 01:45:40 AM IST  platform: Linux


import sys
sys.path.append('../')
from tools import distance_calcu
from tkinter import filedialog as fd,messagebox
import glob,pickle

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



files_list = {}

def open_file():
    global dir_path,file_path,files_list
    files_list = {}
    file_path = fd.askopenfilenames(initialdir = '/home/rohan/codes/LVP' , title = 'select Files',\
        filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
    dir_path = file_path[0].strip(file_path[0].split('/')[-1])
    names = [f.split('/')[-1] for f in file_path]
    check = glob.glob(dir_path+"distances.pkl")
    if len(check)==0:
        for f in file_path:
            name = f.split('/')[-1]
            files_list[name] = 0.0
    else :
        with open(check[0],'rb') as f:
            temp = pickle.load(f)
            for n in names:
                if n in temp.keys():
                    files_list[n] = temp[n]
                else:
                    files_list[n] = 0.0



    files = list(file_path)

    if len(files) ==0:
        messagebox.showinfo("Error", "Please select atleast one file!")

    else:
        pass

def save_stuff():

    with open(dir_path + 'distances.pkl','wb') as f:
        pickle.dump(files_list, f)

    messagebox.showinfo('Saved!',"The results until now have been saved!")

def calc_length(name):
    path = dir_path + name
    res = distance_calcu.input_file(path)
    files_list[name] = round(res, 4)
    res = round(res, 4)
    return res

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import length
    length.vp_start_gui()




