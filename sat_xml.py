#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 28, 2021 06:55:01 PM EEST  platform: Windows NT

import sys
from tkinter import StringVar

# from typing import Literal


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

import unknown_support
import os.path
from mainfunc import create_xml, download, unload_ftp, download_provider


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1(root)
    unknown_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    """Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' ."""
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#d9d9d9"  # X11 color: 'gray85'
        _ana1color = "#d9d9d9"  # X11 color: 'gray85'
        _ana2color = "#ececec"  # Closest X11 color: 'gray92'

        top.geometry("804x588+301+49")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Satellites.xml creator for enigma2 from LyngSat website")
        top.configure(background="#0080c0")
        top.iconbitmap("icon/satellites.ico")

        self.sat, self.longitude = [], []
        self.login = StringVar()
        self.password = StringVar()
        self.ip_adress = StringVar()
        self.path_satellites_xml = StringVar()
        self.path_satellites_xml.set("/etc/tuxbox/")
        self.login.set("root")

        self.Button1 = tk.Button(top)
        self.Button1.place(x=230, y=21, height=24, width=137)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text="""Download satellite list""")
        self.Button1.configure(command=self.down_sat_list)

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(x=30, y=60, height=349, width=739)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(selectmode="multiple")

        self.Label1 = tk.Label(top)
        self.Label1.place(x=60, y=410, height=21, width=84)
        self.Label1.configure(background="#0080c0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text="""Login box""")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(x=40, y=430, height=20, width=134)
        self.Entry1.configure(background="#c0c0c0")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=self.login)

        self.Label2 = tk.Label(top)
        self.Label2.place(x=60, y=450, height=21, width=86)
        self.Label2.configure(background="#0080c0")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text="""Pasword box""")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(x=40, y=470, height=20, width=184)
        self.Entry2.configure(background="#c0c0c0")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=self.password, show="*")

        self.Label3 = tk.Label(top)
        self.Label3.place(x=40, y=490, height=21, width=134)
        self.Label3.configure(background="#0080c0")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text="""Ip adress box""")

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(x=40, y=510, height=20, width=184)
        self.Entry3.configure(background="#c0c0c0")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=self.ip_adress)

        self.Label4 = tk.Label(top)
        self.Label4.place(x=50, y=530, height=21, width=144)
        self.Label4.configure(background="#0080c0")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text="""File satellites.xml""")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(x=40, y=550, height=20, width=184)
        self.Entry4.configure(background="#c0c0c0")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(textvariable=self.path_satellites_xml)

        self.Label5 = tk.Label(top)
        self.Label5.place(x=40, y=570, height=21, width=184)
        self.Label5.configure(background="#0080c0")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text="""/etc/tuxbox/""")

        self.Button2 = tk.Button(top)
        self.Button2.place(x=350, y=495, height=24, width=117)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text="""Create satellites.xml""")
        self.Button2.configure(command=self.create)

        self.Label6 = tk.Label(top)
        self.Label6.place(x=230, y=420, height=21, width=334)
        self.Label6.configure(background="#0080c0")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#ff8000")
        self.Label6.configure(
            text="""Select satellites from the list and click create satellites.xml"""
        )

        self.Button3 = tk.Button(top)
        self.Button3.place(x=330, y=560, height=24, width=157)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text="""Load satellites.xml into box""")
        self.Button3.configure(command=self.ftp_connection)

        self.Label7 = tk.Label(top)
        self.Label7.place(x=350, y=525, height=21, width=114)
        self.Label7.configure(background="#0080c0")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#003300")
        self.Label7.configure(text=""" """)

        self.Label8 = tk.Label(top)
        self.Label8.place(x=620, y=440, height=111, width=134)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "icon/satellites.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label8.configure(image=_img0)
        self.Label8.configure(text="""Label""")

        self.Button4 = tk.Button(top)
        self.Button4.place(x=260, y=470, height=24, width=57)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text="""Multiple""")
        self.Button4.configure(command=self.multiple)

        self.Button5 = tk.Button(top)
        self.Button5.place(x=500, y=470, height=24, width=67)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text="""Extended""")
        self.Button5.configure(command=self.extended)

        self.Button6 = tk.Button(top)
        self.Button6.place(x=430, y=21, height=24, width=137)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text="""Download provider list""")
        self.Button6.configure(command=self.down_povider_list)

        self.Label9 = tk.Label(top)
        self.Label9.place(x=460, y=440, height=21, width=134)
        self.Label9.configure(background="#0080c0")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text="""Choice immediately""")

        self.Label10 = tk.Label(top)
        self.Label10.place(x=230, y=440, height=21, width=125)
        self.Label10.configure(background="#0080c0")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text="""Choice one by one""")

        self.TPbar1 = ttk.Progressbar(top)
        self.TPbar1.configure(mode="indeterminate")
        self.TPbar1.configure(orient="horizontal")

    def multiple(self):
        self.Listbox1.configure(selectmode="multiple")

    def extended(self):
        self.Listbox1.configure(selectmode="extended")

    def down_sat_list(self):
        download(self.Listbox1, self.longitude, self.sat)

    def down_povider_list(self):
        download_provider(self.Listbox1, self.longitude)

    def create(self):
        self.TPbar1.place(
            relx=0.432, rely=0.910, relwidth=0.150, relheight=0.0, height=20
        )
        self.Button2.configure(text="Create satellites.xml")
        self.Button2.configure(background="#d9d9d9")
        create_xml(
            self.Listbox1, self.longitude, self.sat, self.TPbar1, root, self.Button2
        )

    def ftp_connection(self):
        self.Button3.configure(text="Load satellites.xml into box")
        self.Button3.configure(background="#d9d9d9")
        unload_ftp(
            self.ip_adress.get(),
            self.login.get(),
            self.password.get(),
            self.path_satellites_xml.get(),
            self.Button3,
        )


if __name__ == "__main__":
    vp_start_gui()
