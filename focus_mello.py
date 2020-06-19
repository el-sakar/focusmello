#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   This program name is 'focus_mello'.You can focus on your task with use it.
#
#    Copyright (C) 2019  Emrah Gürbüz.

#This program is free software: you can redistribute it and/or modify it under
#the terms of the GNU General Public License as published by the Free Software
#Foundation, either version 3 of the License, or (at your option) any later
#version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY
#WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#PARTICULAR PURPOSE.  See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with
#this program.  If not, see https://www.gnu.org/licenses

#**************************************************************************

import os
import time
import sys
from datetime import timedelta
from tkinter import *
from tkinter import ttk
#from threading import Event
text_lecense= """
   This program name is 'focus_mello'.You can focus on your task with use it.

    Copyright (C) 2019  Emrah Gürbüz.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see https://www.gnu.org/licenses"""

text_credits = """
    Copyright (C) 2019  Emrah Gürbüz.
    Thanks to Ali Sığa and Ece Gürbüz for supports .

"""
class Ktime(object):
    def __init__(self,*args,**kwargs):
        self.combo_num = []
        self.combo_num_2 = []
        self.set_box = []
        self.getime = 0
        self.getime_backup = 0
        self.pomodoro_backup = 0
        self.hour = 0
        self.inbox = '00'
        self.plat = sys.platform
        self.gui_tool()

    def geo(self):
        if self.plat == 'linux':
            root.geometry('230x185+30+40')
        elif self.plat == 'win32':
            root.geometry('270x185+30+40')


    def gui_tool(self):
        self.geo()
        root.resizable(width=FALSE, height=FALSE)
        root.title('f-mello')
        root.bind('<Escape>',self.powoff)
        root.bind('<Alt-s>',self.stop)
        root.bind('<Alt-p>',self.pause)
        root.bind('<Alt-r>',self.run)
        root.bind('<Control-p>',self.pomodoro)
        root.bind('<Control-s>',self.short)
        root.bind('<Control-l>',self.long)
        root.bind('<Alt-i>',self.info_help)
        self.lb = ttk.Label(text='focus-mello')
        self.lb['font'] = 'arial 11'
        self.lb.grid(column=1,row=0,sticky=N)

        self.fr = ttk.Frame(root)
        self.fr['borderwidth'] = 2
        self.fr['relief'] ='groove'
        self.fr.grid(column=1,padx=2,pady=5)


        self.wt_combo()

        self.fr_2 = ttk.Frame(root) #for buttons
        self.fr_2['borderwidth'] = 2
        self.fr_2['relief'] = 'groove'
        self.fr_2.place(relx=0.0,rely=0.7)

        self.boldStyle = ttk.Style ()

        self.boldStyle.configure("Bold.TButton",height=2,
                                 font = ('arial','9','bold'))



        self.info =ttk.Button(root,text='i',width=2,
                              style='Bold.TButton',
                              command=self.info_help)
        self.info.grid(column=2,row=1,padx=1)

        self.btn = ttk.Button(self.fr_2,text='pause',
                              style='Bold.TButton',command=self.pause)
        self.btn.grid(column=0,row=0,padx=1,pady=1)

        self.btn_2 = ttk.Button(self.fr_2,text='run'
                                ,style='Bold.TButton', command=self.run)
        self.btn_2.grid(column=1,row=0,padx=1,pady=1)

        self.btn_3 = ttk.Button(self.fr_2,text='stop'
                                ,style='Bold.TButton', command=self.stop)
        self.btn_3.grid(column=2,row=0,padx=1,pady=1)


        self.boldButton = ttk.Button(self.fr_2, text = "short",
                                     style="Bold.TButton",command=self.short)
        self.boldButton.grid(column=0,row=1,padx=1,pady=1)
        self.boldButton = ttk.Button(self.fr_2, text = "pomodoro",
                                     style="Bold.TButton",command=self.pomodoro)
        self.boldButton.grid(column=1,row=1,padx=1,pady=1)
        self.boldButton = ttk.Button(self.fr_2, text = "long",
                                     style="Bold.TButton",command=self.long)
        self.boldButton.grid(column=2,row=1,padx=1,pady=1)


        self.num_0 = StringVar()
        self.num_0.set('00:00:00')

        self.lbl_2 = ttk.Label(root,textvariable=self.num_0,font='Helvetica 25')
        self.lbl_2.grid(column=1,row=2)

    def wt_combo(self):
        self.counter(1,59)
        self.combo_num_2.extend(self.combo_num)
        self.cb_val = ttk.Combobox(self.fr,width=6)
        self.cb_val['value'] = (self.combo_num_2)
        self.cb_val.insert(END,self.inbox)
        self.cb_val.pack(side='left',pady=3)

        self.cb_val_2 = ttk.Combobox(self.fr,width=6)
        self.cb_val_2['value'] = (self.combo_num_2)
        self.cb_val_2.insert(END,self.inbox)
        self.cb_val_2.pack(side='left',pady=3)

        self.cb_val_3 = ttk.Combobox(self.fr,width=6)
        self.cb_val_3['value'] = (self.combo_num_2)
        self.cb_val_3.insert(END,self.inbox)
        self.cb_val_3.pack(side='left',pady=3)

    def wt_combo_zero(self):
        self.cb_val.delete(0,END)
        self.cb_val_2.delete(0,END)
        self.cb_val_3.delete(0,END)
        self.cb_val.insert(END,self.inbox)
        self.cb_val_2.insert(END,self.inbox)
        self.cb_val_3.insert(END,self.inbox)

    def info_help(self,event=None,*args):
        self.info_box = Toplevel(root)
        self.info_box.title('about f-mello')
        self.info_box.resizable(width=FALSE, height=FALSE)
        self.info_box.bind('<Escape>',self.info_destroy)
        self.info_box.geometry('200x250+265+40')
        self.short_cuts = ['Alt-s:\tstop',
                            'Alt-r:\trun',
                            'Alt-p:\tpause',
                            'Control-p:\tpomodoro',
                            'Control-s:\tshort',
                            'Control-l:\tlong',
                           'Alt-i:\ti\n',
                           'version:\tfocus_mello.v1',
                          'dev:gemrahburak@gmail.com\n']
        self.column = 0
        self.row = 0
        self.param = StringVar()
        for i in self.short_cuts:
            self.param.set(self.short_cuts)
            self.lbl_3 = ttk.Label(self.info_box,text=i)
            self.lbl_3.grid(column=self.column,row=self.row,sticky=W)
            self.row += 1
        self.btn_4 = ttk.Button(self.info_box,text='license',
                                style="Bold.TButton",command=self.license)
        self.btn_5 = ttk.Button(self.info_box,text='credits',
                                style='Bold.TButton',command=self.credits)
        if self.plat == 'linux':
            self.btn_4.grid(column=0,row=10,padx=5,sticky=W)
            self.btn_5.grid(column=0,row=10,padx=5,sticky=SE)
        elif self.plat == 'win32':
            self.btn_4.place(relx=0.0,rely=0.8)
            self.btn_5.place(relx=0.5,rely=0.8)


    def license(self):
        self.license_box = Toplevel(self.info_box)
        self.license_box.title('license')
        if self.plat == 'linux':
            self.license_box.geometry('590x300')
        elif self.plat == 'win32':
            self.license_box.geometry('640x300')
        self.license_box.resizable(width=FALSE, height=FALSE)
        self.license_box.bind('<Escape>',self.license_destroy)
        self.text = Frame(self.license_box)
        self.text['bd'] = 2
        self.text['relief'] = GROOVE
        self.text['bg'] = 'white'
        self.text.pack(expand=YES,fill=BOTH)
        self.lbl_4 = Text(self.text)
        self.lbl_4.insert(1.0,text_lecense)
        self.lbl_4.pack(expand=YES,fill=BOTH)
        self.lbl_4.configure(state='disabled')

    def credits(self):
        self.credits_box = Toplevel(self.info_box)
        self.credits_box.title('credits')
        if self.plat == 'linux':
            self.credits_box.geometry('400x150')
        elif self.plat == 'win32':
            self.credits_box.geometry('430x150')
        self.credits_box.resizable(width=FALSE,height=FALSE)
        self.credits_box.bind('<Escape>',self.credits_destroy)
        self.text_2 = Frame(self.credits_box)
        self.text_2['bd'] = 2
        self.text_2['relief'] = GROOVE
        self.text_2['bg'] = 'white'
        self.text_2.pack(expand=YES,fill=BOTH)
        self.lbl_5 = Text(self.text_2)
        self.lbl_5.insert(1.0,text_credits)
        self.lbl_5.pack(expand=YES,fill=BOTH)
        self.lbl_5.configure(state='disabled')




class Launcher(Ktime):
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.run_st = True
        self.pause_st = True
        self.pomodoro_st = False
        self.pomodoro_pause = False
        self.double_run = 0
        self.t1 = int(self.cb_val.get())
        self.t2 = int(self.cb_val_2.get())
        self.t3 = int(self.cb_val_3.get())


    def counter(self,num, end_num):
        self.combo_num.append(str(num).zfill(2))
        if num == end_num:
            return None
        else:
            return self.counter(num+1, end_num)




    def format_time(self):
            self.timeformat = str(timedelta(seconds=self.getime))
            if len(self.timeformat) == 7:
                self.timeformat = '0'+self.timeformat

            #self.timeformat = "{0:02d}:{1:02d}:{2:02d}".format(self.t1,self.t2,self.t3)
            self.num_0.set(self.timeformat)


    def countdown_best(self):
        if self.run_st:
            self.format_time()
            if self.getime > 0:
                    self.getime -= 1
            elif self.getime == 0:
                self.stop()
                self.noise()
            root.after(1000,self.countdown_best)

    def countdown_cool(self):
        self.run_st = False
        if self.pomodoro_st == True:
            self.format_time()
            if self.getime > 0:
                self.getime -= 1
            elif self.getime == 0:
                self.stop()
                self.noise()
            root.after(1000,self.countdown_cool)

    def pause(self,event=None):
        # on pause can not axes new run input
        self.pause_st = False
        self.run_st = False
        self.double_run = 0
        if self.pomodoro_st == True:
            self.pomodoro_backup = self.getime_backup
            self.pomodoro_st = False
            self.pomodoro_pause = True
        self.swap_time = self.getime
        pass

    def stop(self,event=None):
        self.run_st = False
        self.pause_st = True
        self.pomodoro_st = False
        self.double_run = 0
        if self.pomodoro_pause == True:
            self.getime = self.pomodoro_backup
            self.pomodoro_pause = False
        else:
            if self.getime_backup:
                self.getime = self.getime_backup
        self.format_time()


    def short(self,event=None):
        self.pomodoro_st = True
        self.getime = 300
        self.run_check()

    def pomodoro(self,event=None):
        self.pomodoro_st = True
        self.getime = 1500
        self.run_check()

    def long(self,event=None):
        self.pomodoro_st = True
        self.getime = 600
        self.run_check()

    def math_master(self):
        self.t1 = int(self.cb_val.get())*60*60
        self.t2 = int(self.cb_val_2.get())*60
        self.t3 = int(self.cb_val_3.get())*1
        if self.t1+self.t2+self.t3 > 0:
            self.getime = self.t1+self.t2+self.t3
        else:
            self.getime = self.getime_backup

    def run_check(self):
        if bool(self.getime):
            self.getime_backup = self.getime
            if self.pomodoro_st == True:
                if self.double_run == 0:
                    self.countdown_cool()
            else:
                self.countdown_best()
            self.double_run = 1
        elif bool(self.getime) == False:
            self.double_run = 0
            self.pause_st = True


    def run(self,event=None):
        self.run_st = True
        if self. pause_st == True:
            if self.double_run == 0:
                self.math_master()
                self.run_check()
                self.wt_combo_zero()
        elif self.pause_st == False:
            if self.double_run == 0:
                if self.pomodoro_st == True:
                    return self.run_check()
                else:
                    self.getime = self.swap_time
                    self.run_check()
    def noise(self):
        if self.plat == 'linux':
            duration = 0.5  # second
            duration_2 = 1.1
            freq = 440  # Hz
           # self.control = os.system('play -q -n synth 0.4 sin 440 || echo -e "\a"')
           # self.control = os.system('play -q -n synth 0.4 sin 440 || echo -e "\a"')
           # self.control = os.system('play -q -n synth 1.0 sin 440 || echo -e "\a"')
            self.control = os.system('mplayer ./shakuachi-short.mp3')
            # if ~ sudo apt install sox
            # code is here

           # os.system('play --no-show-progress --null --channels 1 synth %s sine %f' %(duration,
           #                                                                            freq))
           # os.system('play --no-show-progress --null --channels 1 synth %s sine %f' %(duration,
           #                                                                            freq))
           # os.system('play --no-show-progress --null --channels 1 synth %s sine %f' %(duration_2,
                                                         #                              freq))


        elif self.plat =='win32':
            import winsound
            duration = 500  # millisecond
            duration_2 = 1100
            freq = 440  # Hz
            self.beep = winsound.Beep(freq, duration)
            self.beep = winsound.Beep(freq, duration)
            self.beep = winsound.Beep(freq, duration_2)


    def powoff(self,event=None):
        return root.destroy()

    def minimize(self,event=None):
        return root.iconify()

    def info_destroy(self,event=None):
        return self.info_box.destroy()

    def license_destroy(self,event=None):
        return self.license_box.destroy()

    def credits_destroy(self,event=None):
        return self.credits_box.destroy()


if __name__ == '__main__':
    root = Tk()
    app = Launcher()
    mainloop()

