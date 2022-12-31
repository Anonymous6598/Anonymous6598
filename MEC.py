import tkinter as tk
from cgitb import text
from tkinter import *
from tkinter import ttk
import math as mt
from math import *
import numpy as np
from numpy import *
import customtkinter as ctk
from customtkinter import *

def exit(event):
    sc.destroy()

def fullscreen(event):
    global clicks
    clicks +=1
    if clicks % 2 == 0:
        sc.attributes("-fullscreen", True)
    else:
        sc.attributes("-fullscreen", False)

def b_1_clicked():
    sc_b_1 = CTk()
    sc_b_1.title("version info")
    sc_b_1.attributes("-toolwindow", True)
    sc_b_1.resizable(False, False)
    
    b_1_text = CTkLabel(sc_b_1, text="Ово је за тебе ћале", font=("Roboto Bold", 36))
    b_1_text.grid(column=0, row=0)

    version_info = CTkLabel(sc_b_1, text="Версија: 1.0.0", font=("Times New Roman", 16))
    version_info.grid(row=1, column=0)
    
    sc_b_1.mainloop()

def b_2_clicked():
    b_2_1_firstdata.place(x=312, y=52)
    b_2_1_firstdata_text1.place(x=195, y=52)
    b_2_1_firstdata_text2.place(x=515, y=52)

    b_2_1_seconddata.place(x=312, y=92)
    b_2_1_seconddata_text1.place(x=12, y=92)
    b_2_1_seconddata_text2.place(x=515, y=92)

    b_2_1_thirddata.place(x=312, y=126)
    b_2_1_thirddata_text1.place(x=15, y=126)
    b_2_1_thirddata_text2.place(x=515, y=126)

    b_2_1_fourthdata.place(x=312, y=148)
    b_2_1_fourthdata_text1.place(x=68, y=148)
    b_2_1_fourthdata_text2.place(x=515, y=148)

    b_2_1_fifthdata.place(x=312, y=170)
    b_2_1_fifthdata_text1.place(x=62, y=170)
    b_2_1_fifthdata_text2.place(x=515, y=170)

    b_2_2_text1.place(x=600, y=52)

    b_2_2_text2.place(x=845, y=52)   

    b_2_2_firstdata.place(x=784, y=92)
    b_2_2_firstdata_text1.place(x=540, y=92)
    b_2_2_firstdata_text2.place(x=985, y=92)

    b_2_2_seconddata.place(x=784, y=126)
    b_2_2_seconddata_text1.place(x=540, y=126)
    b_2_2_seconddata_text2.place(x=985, y=126)

    b_2_3_text.place(x=380, y=194)

    b_2_3_firstdata.place(x=312, y=220)
    b_2_3_firstdata_text1.place(x=195, y=220)
    b_2_3_firstdata_text2.place(x=515, y=220)

    b_2_3_seconddata.place(x=312, y=250)
    b_2_3_seconddata_text1.place(x=225, y=250)
    b_2_3_seconddata_text2.place(x=515, y=250)

    b_2_4_text.place(x=380, y=275)

    b_2_4_firstdata.place(x=312, y=300)
    b_2_4_firstdata_text1.place(x=175, y=300)
    b_2_4_firstdata_text2.place(x=515, y=300)

    b_2_4_seconddata.place(x=312, y=330)
    b_2_4_seconddata_text1.place(x=227, y=330)
    b_2_4_seconddata_text2.place(x=515, y=330)      

    b_2_4_thirddata.place(x=312, y=360) 
    b_2_4_thirddata_text1.place(x=156, y=360)
    b_2_4_thirddata_text2.place(x=515, y=360)

    b_2_5_text.place(x=780, y=260)

    b_2_5_firstdata.place(x=772, y=290)
    b_2_5_firstdata_text1.place(x=639, y=290)
    b_2_5_firstdata_text2.place(x=974, y=290)

    b_2_5_seconddata.place(x=772, y=320)
    b_2_5_seconddata_text1.place(x=691, y=320)
    b_2_5_seconddata_text2.place(x=974, y=320) 

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()
    
    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_2_3_1_logic(event):
    b_2_1_firstdata_data = b_2_1_firstdata.get()
    b_2_1_seconddata_data = b_2_1_seconddata.get()
    b_2_2_firstdata_data = b_2_2_firstdata.get()
    calculation_result = 0.336 * float(b_2_1_firstdata_data) * (float(b_2_1_seconddata_data) - float(b_2_2_firstdata_data))
    result = str(calculation_result)
    b_2_3_firstdata.insert(0, result)

def b_2_3_2_logic(event):
    b_2_3_firstdata_data = b_2_3_firstdata.get()
    b_2_1_fourthdata_data = b_2_1_fourthdata.get()
    calculation_result = float(b_2_3_firstdata_data) * (0.86 / float(b_2_1_fourthdata_data)) 
    result = str(calculation_result)
    b_2_3_seconddata.insert(0, result)

def b_2_4_1_logic(event):
    b_2_1_firstdata_data = b_2_1_firstdata.get()
    b_2_1_thirddata_data = b_2_1_thirddata.get()
    b_2_2_seconddata_data = b_2_2_seconddata.get()
    calculation_result = 0.336 * float(b_2_1_firstdata_data) * (float(b_2_2_seconddata_data) - float(b_2_1_thirddata_data))
    result = str(calculation_result)
    b_2_4_firstdata.insert(0, result)

def b_2_4_2_logic(event):
    b_2_4_firstdata_data = b_2_4_firstdata.get()
    b_2_1_fifthdata_data = b_2_1_fifthdata.get()
    calculation_result = float(b_2_4_firstdata_data) * (0.86 / float(b_2_1_fifthdata_data))
    result = str(calculation_result)
    b_2_4_seconddata.insert(0, result)

def b_2_4_3_logic(event):
    b_2_4_firstdata_data = b_2_4_firstdata.get()
    b_2_1_fifthdata_data = b_2_1_fifthdata.get()
    calculation_result = (float(b_2_4_firstdata_data) * 0.86) / (1.042 * 0.87 * float(b_2_1_fifthdata_data))
    result = str(calculation_result)
    b_2_4_thirddata.insert(0, result)

def b_2_5_2_logic(event):
    b_2_5_firstdata_data = b_2_5_firstdata.get()
    b_2_1_fifthdata_data = b_2_1_fifthdata.get()
    calculation_result = float(b_2_5_firstdata_data) * (0.86 / float(b_2_1_fifthdata_data))
    result = str(calculation_result)
    b_2_5_seconddata.insert(0, result)

def b_3_clicked():
    b_3_firstdata.place(x=312, y=52)
    b_3_firstdata_text1.place(x=246, y=52)
    b_3_firstdata_text2.place(x=515, y=52)

    b_3_seconddata.place(x=312, y=92)
    b_3_seconddata_text1.place(x=246, y=92)
    b_3_seconddata_text2.place(x=515, y=92)

    b_3_thirddata.place(x=312, y=126)
    b_3_thirddata_text1.place(x=146, y=126)
    b_3_thirddata_text2.place(x=515, y=126)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()

    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()
    
    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()

    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()
    
    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_3_logic(event):
    b_3_firstdata_data = b_3_firstdata.get()
    b_3_seconddata_data = b_3_seconddata.get()
    calculation_result = (2 * float(b_3_firstdata_data) * float(b_3_seconddata_data))/(float(b_3_firstdata_data) + float(b_3_seconddata_data))
    result = str(calculation_result)
    b_3_thirddata.insert(0, result)

def b_4_clicked():
    b_4_firstdata.place(x=312, y=52)
    b_4_firstdata_text1.place(x=193, y=52)
    b_4_firstdata_text2.place(x=515, y=52)

    b_4_seconddata.place(x=312, y=92)
    b_4_seconddata_text1.place(x=193, y=92)
    b_4_seconddata_text2.place(x=515, y=92)

    b_4_thirddata.place(x=312, y=126)
    b_4_thirddata_text1.place(x=175, y=126)
    b_4_thirddata_text2.place(x=515, y=126)

    b_4_fourthdata.place(x=312, y=200)
    b_4_fourthdata_text1.place(x=204, y=200)
    b_4_fourthdata_text2.place(x=515, y=200)

    b_4_fifthdata.place(x=312, y=250)
    b_4_fifthdata_text1.place(x=193, y=250)
    b_4_fifthdata_text2.place(x=515, y=250)

    b_4_data_table_text.place(x=900, y=52)

    b_4_data_table.place(x=900, y=72)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()

    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()
    
    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()

    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()
    
    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_4_logic(event):
    b_4_firstdata_data = b_4_firstdata.get()
    b_4_seconddata_data = b_4_seconddata.get()
    b_4_thirddata_data = b_4_thirddata.get()
    b_4_fourthdata_data = b_4_fourthdata.get()
    calculation_result = float(b_4_firstdata_data) / (0.278 * float(b_4_fourthdata_data) * (float(b_4_thirddata_data) - float(b_4_seconddata_data)))
    result = str(calculation_result)
    b_4_fifthdata.insert(0, result)

def b_5_clicked():
    b_5_1_firstdata.place(x=312, y=52)
    b_5_1_firstdata_text1.place(x=195, y=52)
    b_5_1_firstdata_text2.place(x=515, y=52)

    b_5_1_seconddata.place(x=312, y=92)
    b_5_1_seconddata_text1.place(x=68, y=92)
    b_5_1_seconddata_text2.place(x=515, y=92)

    b_5_1_thirddata.place(x=312, y=126)
    b_5_1_thirddata_text1.place(x=229, y=126)
    b_5_1_thirddata_text2.place(x=515, y=126)

    b_5_2_firstdata.place(x=312, y=164)
    b_5_2_firstdata_text1.place(x=60, y=164)
    b_5_2_firstdata_text2.place(x=515, y=164)

    b_5_2_seconddata.place(x=312, y=208)
    b_5_2_seconddata_text1.place(x=130, y=208)
    b_5_2_seconddata_text2.place(x=515, y=208)

    b_5_2_thirddata.place(x=312, y=248)
    b_5_2_thirddata_text1.place(x=229, y=248)
    b_5_2_thirddata_text2.place(x=515, y=248)

    b_5_2_fourthdata.place(x=312, y=288)
    b_5_2_fourthdata_text1.place(x=153, y=288)
    b_5_2_fourthdata_text2.place(x=515, y=288)

    b_5_3_firstdata.place(x=772, y=52)
    b_5_3_firstdata_text1.place(x=687, y=52)
    b_5_3_firstdata_text2.place(x=976, y=52)

    b_5_3_seconddata.place(x=772, y=92)
    b_5_3_seconddata_text1.place(x=703, y=92)
    b_5_3_seconddata_text2.place(x=976, y=92)

    b_5_3_thirddata.place(x=772, y=126)
    b_5_3_thirddata_text1.place(x=653, y=126)
    b_5_3_thirddata_text2.place(x=976, y=126)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()
    
    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_5_1_3_logic(event):
    b_5_1_firstdata_data = b_5_1_firstdata.get()
    b_5_1_seconddata_data = b_5_1_seconddata.get()
    calculation_result = (float(b_5_1_firstdata_data) * 0.86) / float(b_5_1_seconddata_data)
    result = str(calculation_result)
    b_5_1_thirddata.insert(0, result)

def b_5_2_3_logic(event):
    b_5_2_firstdata_data = b_5_2_firstdata.get()
    b_5_2_seconddata_data = b_5_2_seconddata.get()
    calculation_result = (float(b_5_2_seconddata_data) * 0.86) / float(b_5_2_firstdata_data)
    result = str(calculation_result)
    b_5_2_thirddata.insert(0, result)

def b_5_2_4_logic(event):
    b_5_2_firstdata_data = b_5_2_firstdata.get()
    b_5_2_seconddata_data = b_5_2_seconddata.get()
    calculation_result = (float(b_5_2_seconddata_data) * 0.86) / (1.042 * 0.87 * float(b_5_2_firstdata_data))
    result = str(calculation_result)
    b_5_2_fourthdata.insert(0, result)

def b_5_3_3_logic(event):
    b_5_3_firstdata_data = b_5_3_firstdata.get()
    b_5_3_seconddata_data = b_5_3_seconddata.get()
    calculation_result = (float(b_5_3_firstdata_data) * float(b_5_3_seconddata_data)) / 0.86
    result = str(calculation_result)
    b_5_3_thirddata.insert(0, result)

def b_6_clicked():
    b_6_1_firstdata.place(x=312, y=52)    
    b_6_1_firstdata_text1.place(x=182, y=52)
    b_6_1_firstdata_text2.place(x=515, y=52)

    b_6_1_seconddata.place(x=312, y=92)
    b_6_1_seconddata_text1.place(x=263, y=92)
    b_6_1_seconddata_text2.place(x=515, y=92)

    b_6_1_thirddata.place(x=312, y=126)
    b_6_1_thirddata_text1.place(x=262, y=126)
    b_6_1_thirddata_text2.place(x=515, y=126)

    b_6_2_firstdata.place(x=772, y=52)
    b_6_2_firstdata_text1.place(x=719, y=52)
    b_6_2_firstdata_text2.place(x=976, y=52)

    b_6_2_seconddata.place(x=772, y=92)
    b_6_2_seconddata_text1.place(x=719, y=92)
    b_6_2_seconddata_text2.place(x=976, y=92)

    b_6_2_thirddata.place(x=772, y=126)
    b_6_2_thirddata_text1.place(x=710, y=126)
    b_6_2_thirddata_text2.place(x=976, y=126)

    b_6_3_firstdata.place(x=312, y=164)
    b_6_3_firstdata_text1.place(x=262, y=164)
    b_6_3_firstdata_text2.place(x=515, y=164)

    b_6_3_seconddata.place(x=312, y=208)
    b_6_3_seconddata_text1.place(x=252, y=208)
    b_6_3_seconddata_text2.place(x=515, y=208)

    b_6_3_thirddata.place(x=312, y=248)
    b_6_3_thirddata_text1.place(x=262, y=248)
    b_6_3_thirddata_text2.place(x=515, y=248)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()
    
    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_6_1_3_logic(event):
    b_6_1_firstdata_data = b_6_1_firstdata.get()
    b_6_1_seconddata_data = b_6_1_seconddata.get()
    calculation_result = float(b_6_1_seconddata_data) / (900 * ((float(b_6_1_firstdata_data) / 1000) ** 2) * mt.pi)
    result = str(calculation_result)
    b_6_1_thirddata.insert(0, result)

def b_6_2_3_logic(event):
    b_6_2_firstdata_data = b_6_2_firstdata.get()
    b_6_2_seconddata_data = b_6_2_seconddata.get()
    calculation_result = np.sqrt(float(b_6_2_seconddata_data) / (900 * float(b_6_2_firstdata_data) * mt.pi)) * 1000
    result = str(calculation_result)
    b_6_2_thirddata.insert(0, result)

def b_6_3_3_logic(event):
    b_6_3_firstdata_data = b_6_3_firstdata.get()
    b_6_3_seconddata_data = b_6_3_seconddata.get()
    calculation_result = ((float(b_6_3_seconddata_data) / 1000) ** 2) * mt.pi * 900 * float(b_6_3_firstdata_data)
    result = str(calculation_result)
    b_6_3_thirddata.insert(0, result)

def b_7_clicked():
    b_7_1_text.place(x=0, y=39)

    b_7_1_1_1_text.place(x=90, y=57)
    
    b_7_1_2_1_text.place(x=162, y=57)

    b_7_1_3_1_text.place(x=223, y=57)

    b_7_1_4_1_text.place(x=288, y=57)

    b_7_1_5_1_text.place(x=354, y=57)

    b_7_1_1_2_text.place(x=0, y=77)

    b_7_1_2_2_text.place(x=0, y=97)

    b_7_1_3_2_text.place(x=0, y=117)

    b_7_1_1.place(x=87, y=77)

    b_7_1_2.place(x=87, y=97)

    b_7_1_3.place(x=87, y=117)

    b_7_1_4.place(x=150, y=77)

    b_7_1_5.place(x=150, y=97)

    b_7_1_6.place(x=150, y=117)

    b_7_1_7.place(x=213, y=77)

    b_7_1_8.place(x=213, y=97)

    b_7_1_9.place(x=213, y=117)

    b_7_1_10.place(x=276, y=77)

    b_7_1_11.place(x=276, y=97)

    b_7_1_12.place(x=276, y=117)

    b_7_1_13.place(x=340, y=77)

    b_7_1_14.place(x=340, y=97)

    b_7_1_15.place(x=340, y=117)

    b_7_2_text.place(x=0, y=141)

    b_7_2_1_1_text.place(x=90, y=157)
    
    b_7_2_2_1_text.place(x=162, y=157)

    b_7_2_3_1_text.place(x=223, y=157)

    b_7_2_4_1_text.place(x=288, y=157)

    b_7_2_5_1_text.place(x=354, y=157)

    b_7_2_1_2_text.place(x=0, y=177)

    b_7_2_2_2_text.place(x=0, y=197)

    b_7_2_3_2_text.place(x=0, y=217)

    b_7_2_1.place(x=87, y=177)

    b_7_2_2.place(x=87, y=197)

    b_7_2_3.place(x=87, y=217)

    b_7_2_4.place(x=150, y=177)

    b_7_2_5.place(x=150, y=197)

    b_7_2_6.place(x=150, y=217)

    b_7_2_7.place(x=213, y=177)

    b_7_2_8.place(x=213, y=197)

    b_7_2_9.place(x=213, y=217)

    b_7_2_10.place(x=276, y=177)

    b_7_2_11.place(x=276, y=197)

    b_7_2_12.place(x=276, y=217)

    b_7_2_13.place(x=340, y=177)

    b_7_2_14.place(x=340, y=197)

    b_7_2_15.place(x=340, y=217)

    b_7_3_text.place(x=0, y=241)

    b_7_3_1_1_text.place(x=90, y=257)
    
    b_7_3_2_1_text.place(x=162, y=257)

    b_7_3_3_1_text.place(x=223, y=257)

    b_7_3_4_1_text.place(x=288, y=257)

    b_7_3_5_1_text.place(x=354, y=257)

    b_7_3_1_2_text.place(x=0, y=277)

    b_7_3_2_2_text.place(x=0, y=297)

    b_7_3_3_2_text.place(x=0, y=317)

    b_7_3_1.place(x=87, y=277)

    b_7_3_2.place(x=87, y=297)

    b_7_3_3.place(x=87, y=317)

    b_7_3_4.place(x=150, y=277)

    b_7_3_5.place(x=150, y=297)

    b_7_3_6.place(x=150, y=317)

    b_7_3_7.place(x=213, y=277)

    b_7_3_8.place(x=213, y=297)

    b_7_3_9.place(x=213, y=317)

    b_7_3_10.place(x=276, y=277)

    b_7_3_11.place(x=276, y=297)

    b_7_3_12.place(x=276, y=317)

    b_7_3_13.place(x=340, y=277)

    b_7_3_14.place(x=340, y=297)

    b_7_3_15.place(x=340, y=317)

    b_7_4_text.place(x=0, y=341)

    b_7_4_1_1_text.place(x=90, y=357)
    
    b_7_4_2_1_text.place(x=162, y=357)

    b_7_4_3_1_text.place(x=223, y=357)

    b_7_4_4_1_text.place(x=288, y=357)

    b_7_4_5_1_text.place(x=354, y=357)

    b_7_4_6_1_text.place(x=418, y=357)

    b_7_4_7_1_text.place(x=482, y=357)

    b_7_4_1_2_text.place(x=0, y=377)

    b_7_4_2_2_text.place(x=0, y=397)

    b_7_4_3_2_text.place(x=0, y=417)

    b_7_4_1.place(x=87, y=377)

    b_7_4_2.place(x=87, y=397)

    b_7_4_3.place(x=87, y=417)

    b_7_4_4.place(x=150, y=377)

    b_7_4_5.place(x=150, y=397)

    b_7_4_6.place(x=150, y=417)

    b_7_4_7.place(x=213, y=377)

    b_7_4_8.place(x=213, y=397)

    b_7_4_9.place(x=213, y=417)

    b_7_4_10.place(x=276, y=377)

    b_7_4_11.place(x=276, y=397)

    b_7_4_12.place(x=276, y=417)

    b_7_4_13.place(x=340, y=377)

    b_7_4_14.place(x=340, y=397)

    b_7_4_15.place(x=340, y=417)

    b_7_4_16.place(x=404, y=377)

    b_7_4_17.place(x=404, y=397)

    b_7_4_18.place(x=404, y=417)

    b_7_4_19.place(x=468, y=377)

    b_7_4_20.place(x=468, y=397)

    b_7_4_21.place(x=468, y=417)

    b_7_5_text.place(x=0, y=441)

    b_7_5_1_1_text.place(x=90, y=457)
    
    b_7_5_2_1_text.place(x=162, y=457)

    b_7_5_3_1_text.place(x=223, y=457)

    b_7_5_4_1_text.place(x=288, y=457)

    b_7_5_5_1_text.place(x=354, y=457)

    b_7_5_6_1_text.place(x=418, y=457)

    b_7_5_7_1_text.place(x=482, y=457)

    b_7_5_1_2_text.place(x=0, y=477)

    b_7_5_2_2_text.place(x=0, y=497)

    b_7_5_3_2_text.place(x=0, y=517)

    b_7_5_1.place(x=87, y=477)

    b_7_5_2.place(x=87, y=497)

    b_7_5_3.place(x=87, y=517)

    b_7_5_4.place(x=150, y=477)

    b_7_5_5.place(x=150, y=497)

    b_7_5_6.place(x=150, y=517)

    b_7_5_7.place(x=213, y=477)

    b_7_5_8.place(x=213, y=497)

    b_7_5_9.place(x=213, y=517)

    b_7_5_10.place(x=276, y=477)

    b_7_5_11.place(x=276, y=497)

    b_7_5_12.place(x=276, y=517)

    b_7_5_13.place(x=340, y=477)

    b_7_5_14.place(x=340, y=497)

    b_7_5_15.place(x=340, y=517)

    b_7_5_16.place(x=404, y=477)

    b_7_5_17.place(x=404, y=497)

    b_7_5_18.place(x=404, y=517)

    b_7_5_19.place(x=468, y=477)

    b_7_5_20.place(x=468, y=497)

    b_7_5_21.place(x=468, y=517)
    
    b_7_6_text.place(x=0, y=541)

    b_7_6_1_1_text.place(x=90, y=557)
    
    b_7_6_2_1_text.place(x=162, y=557)

    b_7_6_3_1_text.place(x=223, y=557)

    b_7_6_4_1_text.place(x=288, y=557)

    b_7_6_5_1_text.place(x=354, y=557)

    b_7_6_6_1_text.place(x=418, y=557)

    b_7_6_7_1_text.place(x=482, y=557)

    b_7_6_1_2_text.place(x=0, y=577)

    b_7_6_2_2_text.place(x=0, y=597)

    b_7_6_3_2_text.place(x=0, y=617)

    b_7_6_1.place(x=87, y=577)

    b_7_6_2.place(x=87, y=597)

    b_7_6_3.place(x=87, y=617)

    b_7_6_4.place(x=150, y=577)

    b_7_6_5.place(x=150, y=597)

    b_7_6_6.place(x=150, y=617)

    b_7_6_7.place(x=213, y=577)

    b_7_6_8.place(x=213, y=597)

    b_7_6_9.place(x=213, y=617)

    b_7_6_10.place(x=276, y=577)

    b_7_6_11.place(x=276, y=597)

    b_7_6_12.place(x=276, y=617)

    b_7_6_13.place(x=340, y=577)

    b_7_6_14.place(x=340, y=597)

    b_7_6_15.place(x=340, y=617)

    b_7_6_16.place(x=404, y=577)

    b_7_6_17.place(x=404, y=597)

    b_7_6_18.place(x=404, y=617)

    b_7_6_19.place(x=468, y=577)

    b_7_6_20.place(x=468, y=597)

    b_7_6_21.place(x=468, y=617)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()

    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()
    
    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()

    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()
    
    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_7_2_1_logic(event):
    b_7_1_1_data = b_7_1_1.get()
    calculation_result = (float(b_7_1_1_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_1.insert(0, result)

def b_7_2_2_logic(event):
    b_7_1_2_data = b_7_1_2.get()
    calculation_result = (float(b_7_1_2_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_2.insert(0, result)

def b_7_2_3_logic(event):
    b_7_1_3_data = b_7_1_3.get()
    calculation_result = (float(b_7_1_3_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_3.insert(0, result)

def b_7_2_4_logic(event):
    b_7_1_4_data = b_7_1_4.get()
    calculation_result = (float(b_7_1_4_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_4.insert(0, result)

def b_7_2_5_logic(event):
    b_7_1_5_data = b_7_1_5.get()
    calculation_result = (float(b_7_1_5_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_5.insert(0, result)

def b_7_2_6_logic(event):
    b_7_1_6_data = b_7_1_6.get()
    calculation_result = (float(b_7_1_6_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_6.insert(0, result)

def b_7_2_7_logic(event):
    b_7_1_7_data = b_7_1_7.get()
    calculation_result = (float(b_7_1_7_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_7.insert(0, result)

def b_7_2_8_logic(event):
    b_7_1_8_data = b_7_1_8.get()
    calculation_result = (float(b_7_1_8_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_8.insert(0, result)

def b_7_2_9_logic(event):
    b_7_1_9_data = b_7_1_9.get()
    calculation_result = (float(b_7_1_9_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_9.insert(0, result)

def b_7_2_10_logic(event):
    b_7_1_10_data = b_7_1_10.get()
    calculation_result = (float(b_7_1_10_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_10.insert(0, result)

def b_7_2_11_logic(event):
    b_7_1_11_data = b_7_1_11.get()
    calculation_result = (float(b_7_1_11_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_11.insert(0, result)

def b_7_2_12_logic(event):
    b_7_1_12_data = b_7_1_12.get()
    calculation_result = (float(b_7_1_12_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_12.insert(0, result)

def b_7_2_13_logic(event):
    b_7_1_13_data = b_7_1_13.get()
    calculation_result = (float(b_7_1_13_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_13.insert(0, result)

def b_7_2_14_logic(event):
    b_7_1_14_data = b_7_1_14.get()
    calculation_result = (float(b_7_1_14_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_14.insert(0, result)

def b_7_2_15_logic(event):
    b_7_1_15_data = b_7_1_15.get()
    calculation_result = (float(b_7_1_15_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_2_15.insert(0, result)

def b_7_3_1_logic(event):
    b_7_1_1_data = b_7_1_1.get()
    calculation_result = (float(b_7_1_1_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_1.insert(0, result)

def b_7_3_2_logic(event):
    b_7_1_2_data = b_7_1_2.get()
    calculation_result = (float(b_7_1_2_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_2.insert(0, result)

def b_7_3_3_logic(event):
    b_7_1_3_data = b_7_1_3.get()
    calculation_result = (float(b_7_1_3_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_3.insert(0, result)

def b_7_3_4_logic(event):
    b_7_1_4_data = b_7_1_4.get()
    calculation_result = (float(b_7_1_4_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_4.insert(0, result)

def b_7_3_5_logic(event):
    b_7_1_5_data = b_7_1_5.get()
    calculation_result = (float(b_7_1_5_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_5.insert(0, result)

def b_7_3_6_logic(event):
    b_7_1_6_data = b_7_1_6.get()
    calculation_result = (float(b_7_1_6_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_6.insert(0, result)

def b_7_3_7_logic(event):
    b_7_1_7_data = b_7_1_7.get()
    calculation_result = (float(b_7_1_7_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_7.insert(0, result)

def b_7_3_8_logic(event):
    b_7_1_8_data = b_7_1_8.get()
    calculation_result = (float(b_7_1_8_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_8.insert(0, result)

def b_7_3_9_logic(event):
    b_7_1_9_data = b_7_1_9.get()
    calculation_result = (float(b_7_1_9_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_9.insert(0, result)

def b_7_3_10_logic(event):
    b_7_1_10_data = b_7_1_10.get()
    calculation_result = (float(b_7_1_10_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_10.insert(0, result)

def b_7_3_11_logic(event):
    b_7_1_11_data = b_7_1_11.get()
    calculation_result = (float(b_7_1_11_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_11.insert(0, result)

def b_7_3_12_logic(event):
    b_7_1_12_data = b_7_1_12.get()
    calculation_result = (float(b_7_1_12_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_12.insert(0, result)

def b_7_3_13_logic(event):
    b_7_1_13_data = b_7_1_13.get()
    calculation_result = (float(b_7_1_13_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_13.insert(0, result)

def b_7_3_14_logic(event):
    b_7_1_14_data = b_7_1_14.get()
    calculation_result = (float(b_7_1_14_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_14.insert(0, result)

def b_7_3_15_logic(event):
    b_7_1_15_data = b_7_1_15.get()
    calculation_result = (float(b_7_1_15_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_3_15.insert(0, result)

def b_7_5_1_logic(event):
    b_7_4_1_data = b_7_4_1.get()
    calculation_result = (float(b_7_4_1_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_1.insert(0, result)

def b_7_5_2_logic(event):
    b_7_4_2_data = b_7_4_2.get()
    calculation_result = (float(b_7_4_2_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_2.insert(0, result)

def b_7_5_3_logic(event):
    b_7_4_3_data = b_7_4_3.get()
    calculation_result = (float(b_7_4_3_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_3.insert(0, result)

def b_7_5_4_logic(event):
    b_7_4_4_data = b_7_1_4.get()
    calculation_result = (float(b_7_4_4_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_4.insert(0, result)

def b_7_5_5_logic(event):
    b_7_4_5_data = b_7_4_5.get()
    calculation_result = (float(b_7_4_5_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_5.insert(0, result)

def b_7_5_6_logic(event):
    b_7_4_6_data = b_7_4_6.get()
    calculation_result = (float(b_7_4_6_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_6.insert(0, result)

def b_7_5_7_logic(event):
    b_7_4_7_data = b_7_4_7.get()
    calculation_result = (float(b_7_4_7_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_7.insert(0, result)

def b_7_5_8_logic(event):
    b_7_4_8_data = b_7_4_8.get()
    calculation_result = (float(b_7_4_8_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_8.insert(0, result)

def b_7_5_9_logic(event):
    b_7_4_9_data = b_7_4_9.get()
    calculation_result = (float(b_7_4_9_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_9.insert(0, result)

def b_7_5_10_logic(event):
    b_7_4_10_data = b_7_4_10.get()
    calculation_result = (float(b_7_4_10_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_10.insert(0, result)

def b_7_5_11_logic(event):
    b_7_4_11_data = b_7_4_11.get()
    calculation_result = (float(b_7_4_11_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_11.insert(0, result)

def b_7_5_12_logic(event):
    b_7_4_12_data = b_7_4_12.get()
    calculation_result = (float(b_7_4_12_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_12.insert(0, result)

def b_7_5_13_logic(event):
    b_7_4_13_data = b_7_4_13.get()
    calculation_result = (float(b_7_4_13_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_13.insert(0, result)

def b_7_5_14_logic(event):
    b_7_4_14_data = b_7_4_14.get()
    calculation_result = (float(b_7_4_14_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_14.insert(0, result)

def b_7_5_15_logic(event):
    b_7_4_15_data = b_7_4_15.get()
    calculation_result = (float(b_7_4_15_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_15.insert(0, result)

def b_7_5_16_logic(event):
    b_7_4_16_data = b_7_4_16.get()
    calculation_result = (float(b_7_4_16_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_16.insert(0, result)

def b_7_5_17_logic(event):
    b_7_4_17_data = b_7_4_17.get()
    calculation_result = (float(b_7_4_17_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_17.insert(0, result)

def b_7_5_18_logic(event):
    b_7_4_18_data = b_7_4_18.get()
    calculation_result = (float(b_7_4_18_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_18.insert(0, result)

def b_7_5_19_logic(event):
    b_7_4_19_data = b_7_4_19.get()
    calculation_result = (float(b_7_4_19_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_19.insert(0, result)

def b_7_5_20_logic(event):
    b_7_4_20_data = b_7_4_20.get()
    calculation_result = (float(b_7_4_20_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_20.insert(0, result)

def b_7_5_21_logic(event):
    b_7_4_21_data = b_7_4_21.get()
    calculation_result = (float(b_7_4_21_data) * 10) / 0.86
    result = str(calculation_result)
    b_7_5_21.insert(0, result)

def b_7_6_1_logic(event):
    b_7_4_1_data = b_7_4_1.get()
    calculation_result = (float(b_7_4_1_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_1.insert(0, result)

def b_7_6_2_logic(event):
    b_7_4_2_data = b_7_4_2.get()
    calculation_result = (float(b_7_4_2_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_2.insert(0, result)

def b_7_6_3_logic(event):
    b_7_4_3_data = b_7_4_3.get()
    calculation_result = (float(b_7_4_3_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_3.insert(0, result)

def b_7_6_4_logic(event):
    b_7_4_4_data = b_7_1_4.get()
    calculation_result = (float(b_7_4_4_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_4.insert(0, result)

def b_7_6_5_logic(event):
    b_7_4_5_data = b_7_4_5.get()
    calculation_result = (float(b_7_4_5_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_5.insert(0, result)

def b_7_6_6_logic(event):
    b_7_4_6_data = b_7_4_6.get()
    calculation_result = (float(b_7_4_6_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_6.insert(0, result)

def b_7_6_7_logic(event):
    b_7_4_7_data = b_7_4_7.get()
    calculation_result = (float(b_7_4_7_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_7.insert(0, result)

def b_7_6_8_logic(event):
    b_7_4_8_data = b_7_4_8.get()
    calculation_result = (float(b_7_4_8_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_8.insert(0, result)

def b_7_6_9_logic(event):
    b_7_4_9_data = b_7_4_9.get()
    calculation_result = (float(b_7_4_9_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_9.insert(0, result)

def b_7_6_10_logic(event):
    b_7_4_10_data = b_7_4_10.get()
    calculation_result = (float(b_7_4_10_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_10.insert(0, result)

def b_7_6_11_logic(event):
    b_7_4_11_data = b_7_4_11.get()
    calculation_result = (float(b_7_4_11_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_11.insert(0, result)

def b_7_6_12_logic(event):
    b_7_4_12_data = b_7_4_12.get()
    calculation_result = (float(b_7_4_12_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_12.insert(0, result)

def b_7_6_13_logic(event):
    b_7_4_13_data = b_7_4_13.get()
    calculation_result = (float(b_7_4_13_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_13.insert(0, result)

def b_7_6_14_logic(event):
    b_7_4_14_data = b_7_4_14.get()
    calculation_result = (float(b_7_4_14_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_14.insert(0, result)

def b_7_6_15_logic(event):
    b_7_4_15_data = b_7_4_15.get()
    calculation_result = (float(b_7_4_15_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_15.insert(0, result)

def b_7_6_16_logic(event):
    b_7_4_16_data = b_7_4_16.get()
    calculation_result = (float(b_7_4_16_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_16.insert(0, result)

def b_7_6_17_logic(event):
    b_7_4_17_data = b_7_4_17.get()
    calculation_result = (float(b_7_4_17_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_17.insert(0, result)

def b_7_6_18_logic(event):
    b_7_4_18_data = b_7_4_18.get()
    calculation_result = (float(b_7_4_18_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_18.insert(0, result)

def b_7_6_19_logic(event):
    b_7_4_19_data = b_7_4_19.get()
    calculation_result = (float(b_7_4_19_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_19.insert(0, result)

def b_7_6_20_logic(event):
    b_7_4_20_data = b_7_4_20.get()
    calculation_result = (float(b_7_4_20_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_20.insert(0, result)

def b_7_6_21_logic(event):
    b_7_4_21_data = b_7_4_21.get()
    calculation_result = (float(b_7_4_21_data) * 20) / 0.86
    result = str(calculation_result)
    b_7_6_21.insert(0, result)

def b_8_clicked():
    b_8_text1.place(x=1, y=41)
    
    b_8_text2.place(x=53, y=41)
    
    b_8_text3.place(x=319, y=41)
    
    b_8_1_1.place(x=1, y=61)
    
    b_8_1_2.place(x=1, y=81)
    
    b_8_1_3.place(x=1, y=101)
    
    b_8_1_4.place(x=1, y=121)
    
    b_8_1_5.place(x=1, y=141)
    
    b_8_1_6.place(x=1, y=161)
    
    b_8_1_7.place(x=1, y=181)
    
    b_8_1_8.place(x=1, y=201)
    
    b_8_1_9.place(x=1, y=221)
    
    b_8_1_10.place(x=1, y=241)
    
    b_8_1_11.place(x=1, y=261)
    
    b_8_1_12.place(x=1, y=281)
    
    b_8_2_1.place(x=50, y=61)
    
    b_8_2_2.place(x=50, y=81)
    
    b_8_2_3.place(x=50, y=101)
    
    b_8_2_4.place(x=50, y=121)
    
    b_8_2_5.place(x=50, y=141)
    
    b_8_2_6.place(x=50, y=161)
    
    b_8_2_7.place(x=50, y=181)
    
    b_8_2_8.place(x=50, y=201)
    
    b_8_2_9.place(x=50, y=221)
    
    b_8_2_10.place(x=50, y=241)
    
    b_8_2_11.place(x=50, y=261)
    
    b_8_2_12.place(x=50, y=281)
    
    b_8_3_1.place(x=317, y=61)
    
    b_8_3_2.place(x=317, y=81)
    
    b_8_3_3.place(x=317, y=101)
    
    b_8_3_4.place(x=317, y=121)
    
    b_8_3_5.place(x=317, y=141)
    
    b_8_3_6.place(x=317, y=161)
    
    b_8_3_7.place(x=317, y=181)
    
    b_8_3_8.place(x=317, y=201)
    
    b_8_3_9.place(x=317, y=221)
    
    b_8_3_10.place(x=317, y=241)
    
    b_8_3_11.place(x=317, y=261)
    
    b_8_3_12.place(x=317, y=281)

    b_8_firstdata.place(x=312, y=313)
    b_8_firstdata_text1.place(x=118, y=313)
    b_8_firstdata_text2.place(x=515, y=313)

    b_8_seconddata.place(x=312, y=345)
    b_8_seconddata_text1.place(x=86, y=345)
    b_8_seconddata_text2.place(x=515, y=345)

    b_8_thirddata.place(x=312, y=377)
    b_8_thirddata_text1.place(x=128, y=377)
    b_8_thirddata_text2.place(x=515, y=377)
    
    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()
    
    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_8_3_1_logic(event):
    b_8_2_1_data = b_8_2_1.get()
    calculation_result = (mt.pi * (float(b_8_2_1_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_1.insert(0, result)

def b_8_3_2_logic(event):
    b_8_2_2_data = b_8_2_2.get()
    calculation_result = (mt.pi * (float(b_8_2_2_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_2.insert(0, result)

def b_8_3_3_logic(event):
    b_8_2_3_data = b_8_2_3.get()
    calculation_result = (mt.pi * (float(b_8_2_3_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_3.insert(0, result)

def b_8_3_4_logic(event):
    b_8_2_4_data = b_8_2_4.get()
    calculation_result = (mt.pi * (float(b_8_2_4_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_4.insert(0, result)

def b_8_3_5_logic(event):
    b_8_2_5_data = b_8_2_5.get()
    calculation_result = (mt.pi * (float(b_8_2_5_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_5.insert(0, result)

def b_8_3_6_logic(event):
    b_8_2_6_data = b_8_2_6.get()
    calculation_result = (mt.pi * float(b_8_2_6_data) ** 2) / 4
    result = str(calculation_result)
    b_8_3_6.insert(0, result)

def b_8_3_7_logic(event):
    b_8_2_7_data = b_8_2_7.get()
    calculation_result = (mt.pi * (float(b_8_2_7_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_7.insert(0, result)

def b_8_3_8_logic(event):
    b_8_2_8_data = b_8_2_8.get()
    calculation_result = (mt.pi * (float(b_8_2_8_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_8.insert(0, result)

def b_8_3_9_logic(event):
    b_8_2_9_data = b_8_2_9.get()
    calculation_result = (mt.pi * (float(b_8_2_9_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_9.insert(0, result)

def b_8_3_10_logic(event):
    b_8_2_10_data = b_8_2_10.get()
    calculation_result = (mt.pi * (float(b_8_2_10_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_10.insert(0, result)

def b_8_3_11_logic(event):
    b_8_2_11_data = b_8_2_11.get()
    calculation_result = (mt.pi * (float(b_8_2_11_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_11.insert(0, result)

def b_8_3_12_logic(event):
    b_8_2_12_data = b_8_2_12.get()
    calculation_result = (mt.pi * (float(b_8_2_12_data) ** 2)) / 4
    result = str(calculation_result)
    b_8_3_12.insert(0, result)

def b_8_1_logic(event):
    b_8_3_1_data = b_8_3_1.get()
    b_8_3_2_data = b_8_3_2.get()
    b_8_3_3_data = b_8_3_3.get()
    b_8_3_4_data = b_8_3_4.get()
    b_8_3_5_data = b_8_3_5.get()
    b_8_3_6_data = b_8_3_6.get()
    b_8_3_7_data = b_8_3_7.get()
    b_8_3_8_data = b_8_3_8.get()
    b_8_3_9_data = b_8_3_9.get()
    b_8_3_10_data = b_8_3_10.get()
    b_8_3_11_data = b_8_3_11.get()
    b_8_3_12_data = b_8_3_12.get()
    list = [float(b_8_3_1_data), float(b_8_3_2_data), float(b_8_3_3_data), float(b_8_3_4_data), float(b_8_3_5_data), float(b_8_3_6_data), float(b_8_3_7_data), float(b_8_3_8_data), float(b_8_3_9_data), float(b_8_3_10_data), float(b_8_3_11_data), float(b_8_3_12_data)]
    calculation_result = sum(list)
    result = str(calculation_result)
    b_8_firstdata.insert(0, result)

def b_8_2_logic(event):
    b_8_firstdata_data = b_8_firstdata.get()
    calculation_result = np.sqrt((4 * float(b_8_firstdata_data) / mt.pi))
    result = str(calculation_result)
    b_8_seconddata.insert(0, result)

def b_8_3_logic(event):
    b_8_firstdata_data = b_8_firstdata.get()
    calculation_result = np.sqrt(float(b_8_firstdata_data))
    result = str(calculation_result)
    b_8_thirddata.insert(0, result)

def b_9_clicked():
    b_9_1_text.place(x=0, y=41)

    b_9_2_text.place(x=94, y=41)

    b_9_3_text.place(x=201, y=41)

    b_9_4_text.place(x=312, y=41)

    b_9_5_text.place(x=417, y=41)

    b_9_text1.place(x=0, y=62)

    b_9_1_1.place(x=0, y=82)

    b_9_1_2.place(x=0, y=102)

    b_9_1_3.place(x=0, y=122)

    b_9_1_4.place(x=0, y=142)

    b_9_1_5.place(x=0, y=162)

    b_9_1_6.place(x=0, y=182)

    b_9_1_7.place(x=0, y=202)

    b_9_2_1.place(x=94, y=82)

    b_9_2_2.place(x=94, y=102)

    b_9_2_3.place(x=94, y=122)

    b_9_2_4.place(x=94, y=142)

    b_9_2_5.place(x=94, y=162)

    b_9_2_6.place(x=94, y=182)

    b_9_2_7.place(x=94, y=202)

    b_9_3_1.place(x=201, y=82)

    b_9_3_2.place(x=201, y=102)

    b_9_3_3.place(x=201, y=122)

    b_9_3_4.place(x=201, y=142)

    b_9_3_5.place(x=201, y=162)

    b_9_3_6.place(x=201, y=182)

    b_9_3_7.place(x=201, y=202)

    b_9_4_1.place(x=312, y=82)

    b_9_4_2.place(x=312, y=102)

    b_9_4_3.place(x=312, y=122)

    b_9_4_4.place(x=312, y=142)

    b_9_4_5.place(x=312, y=162)

    b_9_4_6.place(x=312, y=182)

    b_9_4_7.place(x=312, y=202)

    b_9_5_1.place(x=415, y=82)

    b_9_5_2.place(x=415, y=102)

    b_9_5_3.place(x=415, y=122)

    b_9_5_4.place(x=415, y=142)

    b_9_5_5.place(x=415, y=162)

    b_9_5_6.place(x=415, y=182)

    b_9_5_7.place(x=415, y=202)

    b_9_text2.place(x=0, y=222)

    b_9_1_8.place(x=0, y=242)

    b_9_1_9.place(x=0, y=262)

    b_9_1_10.place(x=0, y=282)

    b_9_1_11.place(x=0, y=302)

    b_9_1_12.place(x=0, y=322)

    b_9_1_13.place(x=0, y=342)

    b_9_1_14.place(x=0, y=362)

    b_9_1_15.place(x=0, y=382)

    b_9_1_16.place(x=0, y=402)

    b_9_1_17.place(x=0, y=422)

    b_9_1_18.place(x=0, y=442)

    b_9_1_19.place(x=0, y=462)

    b_9_1_20.place(x=0, y=482)

    b_9_1_21.place(x=0, y=502)

    b_9_2_8.place(x=94, y=242)

    b_9_2_9.place(x=94, y=262)

    b_9_2_10.place(x=94, y=282)

    b_9_2_11.place(x=94, y=302)

    b_9_2_12.place(x=94, y=322)

    b_9_2_13.place(x=94, y=342)

    b_9_2_14.place(x=94, y=362)

    b_9_2_15.place(x=94, y=382)

    b_9_2_16.place(x=94, y=402)

    b_9_2_17.place(x=94, y=422)

    b_9_2_18.place(x=94, y=442)

    b_9_2_19.place(x=94, y=462)

    b_9_2_20.place(x=94, y=482)

    b_9_2_21.place(x=94, y=502)

    b_9_3_8.place(x=201, y=242)

    b_9_3_9.place(x=201, y=262)

    b_9_3_10.place(x=201, y=282)

    b_9_3_11.place(x=201, y=302)

    b_9_3_12.place(x=201, y=322)

    b_9_3_13.place(x=201, y=342)

    b_9_3_14.place(x=201, y=362)

    b_9_3_15.place(x=201, y=382)

    b_9_3_16.place(x=201, y=402)

    b_9_3_17.place(x=201, y=422)

    b_9_3_18.place(x=201, y=442)

    b_9_3_19.place(x=201, y=462)

    b_9_3_20.place(x=201, y=482)

    b_9_3_21.place(x=201, y=502)

    b_9_4_8.place(x=312, y=242)

    b_9_4_9.place(x=312, y=262)

    b_9_4_10.place(x=312, y=282)

    b_9_4_11.place(x=312, y=302)

    b_9_4_12.place(x=312, y=322)

    b_9_4_13.place(x=312, y=342)

    b_9_4_14.place(x=312, y=362)

    b_9_4_15.place(x=312, y=382)

    b_9_4_16.place(x=312, y=402)

    b_9_4_17.place(x=312, y=422)

    b_9_4_18.place(x=312, y=442)

    b_9_4_19.place(x=312, y=462)

    b_9_4_20.place(x=312, y=482)

    b_9_4_21.place(x=312, y=502)

    b_9_5_8.place(x=415, y=242)

    b_9_5_9.place(x=415, y=262)

    b_9_5_10.place(x=415, y=282)

    b_9_5_11.place(x=415, y=302)

    b_9_5_12.place(x=415, y=322)

    b_9_5_13.place(x=415, y=342)

    b_9_5_14.place(x=415, y=362)

    b_9_5_15.place(x=415, y=382)

    b_9_5_16.place(x=415, y=402)

    b_9_5_17.place(x=415, y=422)

    b_9_5_18.place(x=415, y=442)

    b_9_5_19.place(x=415, y=462)

    b_9_5_20.place(x=415, y=482)

    b_9_5_21.place(x=415, y=502)

    b_9_text3.place(x=0, y=522)

    b_9_1_22.place(x=0, y=542)

    b_9_1_23.place(x=0, y=562)

    b_9_1_24.place(x=0, y=582)

    b_9_1_25.place(x=0, y=602)

    b_9_1_26.place(x=0, y=622)

    b_9_1_27.place(x=0, y=642)

    b_9_1_28.place(x=0, y=662)

    b_9_1_29.place(x=0, y=682)

    b_9_1_30.place(x=0, y=702)

    b_9_3_22.place(x=201, y=542)

    b_9_3_23.place(x=201, y=562)

    b_9_3_24.place(x=201, y=582)

    b_9_3_25.place(x=201, y=602)

    b_9_3_26.place(x=201, y=622)

    b_9_3_27.place(x=201, y=642)

    b_9_3_28.place(x=201, y=662)

    b_9_3_29.place(x=201, y=682)

    b_9_3_30.place(x=201, y=702)

    b_9_4_22.place(x=312, y=542)

    b_9_4_23.place(x=312, y=562)

    b_9_4_24.place(x=312, y=582)

    b_9_4_25.place(x=312, y=602)

    b_9_4_26.place(x=312, y=622)

    b_9_4_27.place(x=312, y=642)

    b_9_4_28.place(x=312, y=662)

    b_9_4_29.place(x=312, y=682)

    b_9_4_30.place(x=312, y=702)

    b_9_5_22.place(x=415, y=542)

    b_9_5_23.place(x=415, y=562)

    b_9_5_24.place(x=415, y=582)

    b_9_5_25.place(x=415, y=602)

    b_9_5_26.place(x=415, y=622)

    b_9_5_27.place(x=415, y=642)

    b_9_5_28.place(x=415, y=662)

    b_9_5_29.place(x=415, y=682)

    b_9_5_30.place(x=415, y=702)

    b_9_text4.place(x=0, y=722)

    b_9_1_31.place(x=0, y=742)

    b_9_1_32.place(x=0, y=762)

    b_9_1_33.place(x=0, y=782)

    b_9_1_34.place(x=0, y=802)

    b_9_1_35.place(x=0, y=822)

    b_9_1_36.place(x=0, y=842)

    b_9_1_37.place(x=520, y=82)

    b_9_2_31.place(x=94, y=742)

    b_9_2_32.place(x=94, y=762)

    b_9_2_33.place(x=94, y=782)

    b_9_2_34.place(x=94, y=802)

    b_9_2_35.place(x=94, y=822)

    b_9_2_36.place(x=94, y=842)

    b_9_2_37.place(x=614, y=82)

    b_9_3_31.place(x=201, y=742)

    b_9_3_32.place(x=201, y=762)

    b_9_3_33.place(x=201, y=782)

    b_9_3_34.place(x=201, y=802)

    b_9_3_35.place(x=201, y=822)

    b_9_3_36.place(x=201, y=842)

    b_9_3_37.place(x=721, y=82)

    b_9_4_31.place(x=312, y=742)

    b_9_4_32.place(x=312, y=762)

    b_9_4_33.place(x=312, y=782)

    b_9_4_34.place(x=312, y=802)

    b_9_4_35.place(x=312, y=822)

    b_9_4_36.place(x=312, y=842)

    b_9_4_37.place(x=832, y=82)

    b_9_5_31.place(x=415, y=742)

    b_9_5_32.place(x=415, y=762)

    b_9_5_33.place(x=415, y=782)

    b_9_5_34.place(x=415, y=802)

    b_9_5_35.place(x=415, y=822)

    b_9_5_36.place(x=415, y=842)

    b_9_5_37.place(x=935, y=82)

    b_9_text5.place(x=520, y=102)

    b_9_1_38.place(x=520, y=122)

    b_9_1_39.place(x=520, y=142)

    b_9_1_40.place(x=520, y=162)

    b_9_1_41.place(x=520, y=182)

    b_9_1_42.place(x=520, y=202)

    b_9_1_43.place(x=520, y=222)

    b_9_1_44.place(x=520, y=242)

    b_9_2_38.place(x=614, y=122)

    b_9_2_39.place(x=614, y=142)

    b_9_2_40.place(x=614, y=162)

    b_9_2_41.place(x=614, y=182)

    b_9_2_42.place(x=614, y=202)

    b_9_2_43.place(x=614, y=222)

    b_9_2_44.place(x=614, y=242)

    b_9_3_38.place(x=721, y=122)

    b_9_3_39.place(x=721, y=142)

    b_9_3_40.place(x=721, y=162)

    b_9_3_41.place(x=721, y=182)

    b_9_3_42.place(x=721, y=202)

    b_9_3_43.place(x=721, y=222)

    b_9_3_44.place(x=721, y=242)

    b_9_4_38.place(x=832, y=122)

    b_9_4_39.place(x=832, y=142)

    b_9_4_40.place(x=832, y=162)

    b_9_4_41.place(x=832, y=182)

    b_9_4_42.place(x=832, y=202)

    b_9_4_43.place(x=832, y=222)

    b_9_4_44.place(x=832, y=242)

    b_9_5_38.place(x=935, y=122)

    b_9_5_39.place(x=935, y=142)

    b_9_5_40.place(x=935, y=162)

    b_9_5_41.place(x=935, y=182)

    b_9_5_42.place(x=935, y=202)

    b_9_5_43.place(x=935, y=222)

    b_9_5_44.place(x=935, y=242)

    b_9_6.place(x=767, y=302)
    b_9_6_text1.place(x=703, y=281)
    b_9_6_text2.place(x=703, y=302)

    b_9_7_text1.place(x=1125, y=41)

    b_9_7_text2.place(x=1202, y=41)

    b_9_7_text3.place(x=1302, y=41)

    b_9_7_1_1.place(x=1100, y=62)

    b_9_7_1_2.place(x=1100, y=82)

    b_9_7_1_3.place(x=1100, y=102)

    b_9_7_1_4.place(x=1100, y=122)

    b_9_7_1_5.place(x=1100, y=142)

    b_9_7_1_6.place(x=1100, y=162)

    b_9_7_1_7.place(x=1100, y=182)

    b_9_7_1_8.place(x=1100, y=202)

    b_9_7_1_9.place(x=1100, y=222)

    b_9_7_1_10.place(x=1100, y=242)

    b_9_7_1_11.place(x=1100, y=262)

    b_9_7_1_12.place(x=1100, y=282)

    b_9_7_1_13.place(x=1100, y=302)

    b_9_7_1_14.place(x=1100, y=322)

    b_9_7_1_15.place(x=1100, y=342)

    b_9_7_1_16.place(x=1100, y=362)

    b_9_7_1_17.place(x=1100, y=382)

    b_9_7_1_18.place(x=1100, y=402)

    b_9_7_1_19.place(x=1100, y=422)

    b_9_7_1_20.place(x=1100, y=442)

    b_9_7_1_21.place(x=1100, y=462)

    b_9_7_2_1.place(x=1189, y=62)

    b_9_7_2_2.place(x=1189, y=82)

    b_9_7_2_3.place(x=1189, y=102)

    b_9_7_2_4.place(x=1189, y=122)

    b_9_7_2_5.place(x=1189, y=142)

    b_9_7_2_6.place(x=1189, y=162)

    b_9_7_2_7.place(x=1189, y=182)

    b_9_7_2_8.place(x=1189, y=202)

    b_9_7_2_9.place(x=1189, y=222)

    b_9_7_2_10.place(x=1189, y=242)

    b_9_7_2_11.place(x=1189, y=262)

    b_9_7_2_12.place(x=1189, y=282)

    b_9_7_2_13.place(x=1189, y=302)

    b_9_7_2_14.place(x=1189, y=322)

    b_9_7_2_15.place(x=1189, y=342)

    b_9_7_2_16.place(x=1189, y=362)

    b_9_7_2_17.place(x=1189, y=382)

    b_9_7_2_18.place(x=1189, y=402)

    b_9_7_2_19.place(x=1189, y=422)

    b_9_7_2_20.place(x=1189, y=442)

    b_9_7_2_21.place(x=1189, y=462)

    b_9_7_3_1.place(x=1278, y=62)

    b_9_7_3_2.place(x=1278, y=82)

    b_9_7_3_3.place(x=1278, y=102)

    b_9_7_3_4.place(x=1278, y=122)

    b_9_7_3_5.place(x=1278, y=142)

    b_9_7_3_6.place(x=1278, y=162)

    b_9_7_3_7.place(x=1278, y=182)

    b_9_7_3_8.place(x=1278, y=202)

    b_9_7_3_9.place(x=1278, y=222)

    b_9_7_3_10.place(x=1278, y=242)

    b_9_7_3_11.place(x=1278, y=262)

    b_9_7_3_12.place(x=1278, y=282)

    b_9_7_3_13.place(x=1278, y=302)

    b_9_7_3_14.place(x=1278, y=322)

    b_9_7_3_15.place(x=1278, y=342)

    b_9_7_3_16.place(x=1278, y=362)

    b_9_7_3_17.place(x=1278, y=382)

    b_9_7_3_18.place(x=1278, y=402)

    b_9_7_3_19.place(x=1278, y=422)

    b_9_7_3_20.place(x=1278, y=442)

    b_9_7_3_21.place(x=1278, y=462)

    b_9_8.place(x=1100, y=502)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()
    
    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_9_5_1_logic(event):
    b_9_4_1_data = b_9_4_1.get()
    calculation_result = float(b_9_4_1_data) * 0.123
    result = str(calculation_result)
    b_9_5_1.insert(0, result)

def b_9_5_2_logic(event):
    b_9_4_2_data = b_9_4_2.get()
    calculation_result = float(b_9_4_2_data) * 0.201
    result = str(calculation_result)
    b_9_5_2.insert(0, result)

def b_9_5_3_logic(event):
    b_9_4_3_data = b_9_4_3.get()
    calculation_result = float(b_9_4_3_data) * 0.366
    result = str(calculation_result)
    b_9_5_3.insert(0, result)

def b_9_5_4_logic(event):
    b_9_4_4_data = b_9_4_4.get()
    calculation_result = float(b_9_4_4_data) * 0.581
    result = str(calculation_result)
    b_9_5_4.insert(0, result)

def b_9_5_5_logic(event):
    b_9_4_5_data = b_9_4_5.get()
    calculation_result = float(b_9_4_5_data) * 1.01
    result = str(calculation_result)
    b_9_5_5.insert(0, result)

def b_9_5_6_logic(event):
    b_9_4_6_data = b_9_4_6.get()
    calculation_result = float(b_9_4_6_data) * 1.37
    result = str(calculation_result)
    b_9_5_6.insert(0, result)

def b_9_5_7_logic(event):
    b_9_4_7_data = b_9_4_7.get()
    calculation_result = float(b_9_4_7_data) * 2.16
    result = str(calculation_result)
    b_9_5_7.insert(0, result)

def b_9_5_8_logic(event):
    b_9_4_8_data = b_9_4_8.get()
    calculation_result = float(b_9_4_8_data) * 1.23
    result = str(calculation_result)
    b_9_5_8.insert(0, result)

def b_9_5_9_logic(event):
    b_9_4_9_data = b_9_4_9.get()
    calculation_result = float(b_9_4_9_data) * 2.08
    result = str(calculation_result)
    b_9_5_9.insert(0, result)

def b_9_5_10_logic(event):
    b_9_4_10_data = b_9_4_10.get()
    calculation_result = float(b_9_4_10_data) * 3.22
    result = str(calculation_result)
    b_9_5_10.insert(0, result)

def b_9_5_11_logic(event):
    b_9_4_11_data = b_9_4_11.get()
    calculation_result = float(b_9_4_11_data) * 3.85
    result = str(calculation_result)
    b_9_5_11.insert(0, result)

def b_9_5_12_logic(event):
    b_9_4_12_data = b_9_4_12.get()
    calculation_result = float(b_9_4_12_data) * 5.35
    result = str(calculation_result)
    b_9_5_12.insert(0, result)

def b_9_5_13_logic(event):
    b_9_4_13_data = b_9_4_13.get()
    calculation_result = float(b_9_4_13_data) * 7.09
    result = str(calculation_result)
    b_9_5_13.insert(0, result)

def b_9_5_14_logic(event):
    b_9_4_14_data = b_9_4_14.get()
    calculation_result = float(b_9_4_14_data) * 7.93
    result = str(calculation_result)
    b_9_5_14.insert(0, result)

def b_9_5_15_logic(event):
    b_9_4_15_data = b_9_4_15.get()
    calculation_result = float(b_9_4_15_data) * 10
    result = str(calculation_result)
    b_9_5_15.insert(0, result)

def b_9_5_16_logic(event):
    b_9_4_16_data = b_9_4_16.get()
    calculation_result = float(b_9_4_16_data) * 12.3
    result = str(calculation_result)
    b_9_5_16.insert(0, result)

def b_9_5_17_logic(event):
    b_9_4_17_data = b_9_4_17.get()
    calculation_result = float(b_9_4_17_data) * 17.7
    result = str(calculation_result)
    b_9_5_17.insert(0, result)

def b_9_5_18_logic(event):
    b_9_4_18_data = b_9_4_18.get()
    calculation_result = float(b_9_4_18_data) * 37.7
    result = str(calculation_result)
    b_9_5_18.insert(0, result)

def b_9_5_19_logic(event):
    b_9_4_19_data = b_9_4_19.get()
    calculation_result = float(b_9_4_19_data) * 53.2
    result = str(calculation_result)
    b_9_5_19.insert(0, result)

def b_9_5_20_logic(event):
    b_9_4_20_data = b_9_4_20.get()
    calculation_result = float(b_9_4_20_data) * 75.3
    result = str(calculation_result)
    b_9_5_20.insert(0, result)

def b_9_5_21_logic(event):
    b_9_4_21_data = b_9_4_21.get()
    calculation_result = float(b_9_4_21_data) * 90.5
    result = str(calculation_result)
    b_9_5_21.insert(0, result)

def b_9_5_22_logic(event):
    b_9_4_22_data = b_9_4_22.get()
    calculation_result = float(b_9_4_22_data) * 0.03
    result = str(calculation_result)
    b_9_5_22.insert(0, result)

def b_9_5_23_logic(event):
    b_9_4_23_data = b_9_4_23.get()
    calculation_result = float(b_9_4_23_data) * 0.06
    result = str(calculation_result)
    b_9_5_23.insert(0, result)

def b_9_5_24_logic(event):
    b_9_4_24_data = b_9_4_24.get()
    calculation_result = float(b_9_4_24_data) * 0.08
    result = str(calculation_result)
    b_9_5_24.insert(0, result)

def b_9_5_25_logic(event):
    b_9_4_25_data = b_9_4_25.get()
    calculation_result = float(b_9_4_25_data) * 0.13
    result = str(calculation_result)
    b_9_5_25.insert(0, result)

def b_9_5_26_logic(event):
    b_9_4_26_data = b_9_4_26.get()
    calculation_result = float(b_9_4_26_data) * 0.2
    result = str(calculation_result)
    b_9_5_26.insert(0, result)

def b_9_5_27_logic(event):
    b_9_4_27_data = b_9_4_27.get()
    calculation_result = float(b_9_4_27_data) * 0.3
    result = str(calculation_result)
    b_9_5_27.insert(0, result)

def b_9_5_28_logic(event):
    b_9_4_28_data = b_9_4_28.get()
    calculation_result = float(b_9_4_28_data) * 0.52
    result = str(calculation_result)
    b_9_5_28.insert(0, result)

def b_9_5_29_logic(event):
    b_9_4_29_data = b_9_4_29.get()
    calculation_result = float(b_9_4_29_data) * 0.8
    result = str(calculation_result)
    b_9_5_29.insert(0, result)

def b_9_5_30_logic(event):
    b_9_4_30_data = b_9_4_30.get()
    calculation_result = float(b_9_4_30_data) * 1.2
    result = str(calculation_result)
    b_9_5_30.insert(0, result)

def b_9_5_31_logic(event):
    b_9_4_31_data = b_9_4_31.get()
    calculation_result = float(b_9_4_31_data) * 0.106
    result = str(calculation_result)
    b_9_5_31.insert(0, result)

def b_9_5_32_logic(event):
    b_9_4_32_data = b_9_4_32.get()
    calculation_result = float(b_9_4_32_data) * 0.163
    result = str(calculation_result)
    b_9_5_32.insert(0, result)

def b_9_5_33_logic(event):
    b_9_4_33_data = b_9_4_33.get()
    calculation_result = float(b_9_4_33_data) * 0.254
    result = str(calculation_result)
    b_9_5_33.insert(0, result)

def b_9_5_34_logic(event):
    b_9_4_34_data = b_9_4_34.get()
    calculation_result = float(b_9_4_34_data) * 0.423
    result = str(calculation_result)
    b_9_5_34.insert(0, result)

def b_9_5_35_logic(event):
    b_9_4_35_data = b_9_4_35.get()
    calculation_result = float(b_9_4_35_data) * 0.661
    result = str(calculation_result)
    b_9_5_35.insert(0, result)

def b_9_5_36_logic(event):
    b_9_4_36_data = b_9_4_36.get()
    calculation_result = float(b_9_4_36_data) * 1.029
    result = str(calculation_result)
    b_9_5_36.insert(0, result)

def b_9_5_37_logic(event):
    b_9_4_37_data = b_9_4_37.get()
    calculation_result = float(b_9_4_37_data) * 1.633
    result = str(calculation_result)
    b_9_5_37.insert(0, result)

def b_9_5_38_logic(event):
    b_9_4_38_data = b_9_4_38.get()
    calculation_result = float(b_9_4_38_data) * 0.049
    result = str(calculation_result)
    b_9_5_38.insert(0, result)

def b_9_5_39_logic(event):
    b_9_4_39_data = b_9_4_39.get()
    calculation_result = float(b_9_4_39_data) * 0.095
    result = str(calculation_result)
    b_9_5_39.insert(0, result)

def b_9_5_40_logic(event):
    b_9_4_40_data = b_9_4_40.get()
    calculation_result = float(b_9_4_40_data) * 0.113
    result = str(calculation_result)
    b_9_5_40.insert(0, result)

def b_9_5_41_logic(event):
    b_9_4_41_data = b_9_4_41.get()
    calculation_result = float(b_9_4_41_data) * 0.113
    result = str(calculation_result)
    b_9_5_41.insert(0, result)

def b_9_5_42_logic(event):
    b_9_4_42_data = b_9_4_42.get()
    calculation_result = float(b_9_4_42_data) * 0.201
    result = str(calculation_result)
    b_9_5_42.insert(0, result)

def b_9_5_43_logic(event):
    b_9_4_43_data = b_9_4_43.get()
    calculation_result = float(b_9_4_43_data) * 0.327
    result = str(calculation_result)
    b_9_5_43.insert(0, result)

def b_9_5_44_logic(event):
    b_9_4_44_data = b_9_4_44.get()
    calculation_result = float(b_9_4_44_data) * 0.539
    result = str(calculation_result)
    b_9_5_44.insert(0, result)

def b_9_6_logic(event):
    b_9_5_1_data = b_9_5_1.get()
    b_9_5_2_data = b_9_5_2.get()
    b_9_5_3_data = b_9_5_3.get()
    b_9_5_4_data = b_9_5_4.get()
    b_9_5_5_data = b_9_5_5.get()
    b_9_5_6_data = b_9_5_6.get()
    b_9_5_7_data = b_9_5_7.get()
    b_9_5_8_data = b_9_5_8.get()
    b_9_5_9_data = b_9_5_9.get()
    b_9_5_10_data = b_9_5_10.get()
    b_9_5_11_data = b_9_5_11.get()
    b_9_5_12_data = b_9_5_12.get()
    b_9_5_13_data = b_9_5_13.get()
    b_9_5_14_data = b_9_5_14.get()
    b_9_5_15_data = b_9_5_15.get()
    b_9_5_16_data = b_9_5_16.get()
    b_9_5_17_data = b_9_5_17.get()
    b_9_5_18_data = b_9_5_18.get()
    b_9_5_19_data = b_9_5_19.get()
    b_9_5_20_data = b_9_5_20.get()
    b_9_5_21_data = b_9_5_21.get()
    b_9_5_22_data = b_9_5_22.get()
    b_9_5_23_data = b_9_5_23.get()
    b_9_5_24_data = b_9_5_24.get()
    b_9_5_25_data = b_9_5_25.get()
    b_9_5_26_data = b_9_5_26.get()
    b_9_5_27_data = b_9_5_27.get()
    b_9_5_28_data = b_9_5_28.get()
    b_9_5_29_data = b_9_5_29.get()
    b_9_5_30_data = b_9_5_30.get()
    b_9_5_31_data = b_9_5_31.get()
    b_9_5_32_data = b_9_5_32.get()
    b_9_5_33_data = b_9_5_33.get()
    b_9_5_34_data = b_9_5_34.get()
    b_9_5_35_data = b_9_5_35.get()
    b_9_5_36_data = b_9_5_36.get()
    b_9_5_37_data = b_9_5_37.get()
    b_9_5_38_data = b_9_5_38.get()
    b_9_5_39_data = b_9_5_39.get()
    b_9_5_40_data = b_9_5_40.get()
    b_9_5_41_data = b_9_5_41.get()
    b_9_5_42_data = b_9_5_42.get()
    b_9_5_43_data = b_9_5_43.get()
    b_9_5_44_data = b_9_5_44.get()
    list = [float(b_9_5_1_data), float(b_9_5_2_data), float(b_9_5_3_data), float(b_9_5_4_data), float(b_9_5_5_data), float(b_9_5_6_data), float(b_9_5_7_data), float(b_9_5_8_data), float(b_9_5_9_data), float(b_9_5_10_data), float(b_9_5_11_data), float(b_9_5_12_data), float(b_9_5_13_data), float(b_9_5_14_data), float(b_9_5_15_data), float(b_9_5_16_data), float(b_9_5_17_data), float(b_9_5_18_data), float(b_9_5_19_data), float(b_9_5_20_data), float(b_9_5_21_data), float(b_9_5_22_data), float(b_9_5_23_data), float(b_9_5_24_data), float(b_9_5_25_data), float(b_9_5_26_data), float(b_9_5_27_data), float(b_9_5_28_data), float(b_9_5_29_data), float(b_9_5_30_data), float(b_9_5_31_data), float(b_9_5_32_data), float(b_9_5_33_data), float(b_9_5_34_data), float(b_9_5_35_data), float(b_9_5_36_data), float(b_9_5_37_data), float(b_9_5_38_data), float(b_9_5_39_data), float(b_9_5_40_data), float(b_9_5_41_data), float(b_9_5_42_data), float(b_9_5_43_data), float(b_9_5_44_data)]
    calculation_result = sum(list)
    result = str(calculation_result)
    b_9_6.insert(0, result)

def b_9_7_1_1_logic(event):
    calculation_result = 17.2 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_1.insert(0, result)

def b_9_7_1_2_logic(event):
    calculation_result = 21.3 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_2.insert(0, result)

def b_9_7_1_3_logic(event):
    calculation_result = 26.9 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_3.insert(0, result)

def b_9_7_1_4_logic(event):
    calculation_result = 33.7 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_4.insert(0, result)

def b_9_7_1_5_logic(event):
    calculation_result = 42.4 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_5.insert(0, result)

def b_9_7_1_6_logic(event):
    calculation_result = 48.3 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_6.insert(0, result)

def b_9_7_1_7_logic(event):
    calculation_result = 60.3 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_7.insert(0, result)

def b_9_7_1_8_logic(event):
    calculation_result = 44.5 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_8.insert(0, result)

def b_9_7_1_9_logic(event):
    calculation_result = 57 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_9.insert(0, result)

def b_9_7_1_10_logic(event):
    calculation_result = 70 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_10.insert(0, result)

def b_9_7_1_11_logic(event):
    calculation_result = 76 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_11.insert(0, result)

def b_9_7_1_12_logic(event):
    calculation_result = 89 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_12.insert(0, result)

def b_9_7_1_13_logic(event):
    calculation_result = 102 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_13.insert(0, result)

def b_9_7_1_14_logic(event):
    calculation_result = 108 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_14.insert(0, result)

def b_9_7_1_15_logic(event):
    calculation_result = 121 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_15.insert(0, result)

def b_9_7_1_16_logic(event):
    calculation_result = 133 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_16.insert(0, result)

def b_9_7_1_17_logic(event):
    calculation_result = 159 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_17.insert(0, result)

def b_9_7_1_18_logic(event):
    calculation_result = 219 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_18.insert(0, result)

def b_9_7_1_19_logic(event):
    calculation_result = 273 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_19.insert(0, result)

def b_9_7_1_20_logic(event):
    calculation_result = 323 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_20.insert(0, result)

def b_9_7_1_21_logic(event):
    calculation_result = 355.6 * mt.pi * (0.1 ** 3)
    result = str(calculation_result)
    b_9_7_1_21.insert(0, result)

def b_9_7_2_1_logic(event):
    b_9_4_1_data = b_9_4_1.get()
    b_9_7_1_1_data = b_9_7_1_1.get()
    calculation_result = float(b_9_4_1_data) * float(b_9_7_1_1_data)
    result = str(calculation_result)
    b_9_7_2_1.insert(0, result)

def b_9_7_2_2_logic(event):
    b_9_4_2_data = b_9_4_2.get()
    b_9_7_1_2_data = b_9_7_1_2.get()
    calculation_result = float(b_9_4_2_data) * float(b_9_7_1_2_data)
    result = str(calculation_result)
    b_9_7_2_2.insert(0, result)

def b_9_7_2_3_logic(event):
    b_9_4_3_data = b_9_4_3.get()
    b_9_7_1_3_data = b_9_7_1_3.get()
    calculation_result = float(b_9_4_3_data) * float(b_9_7_1_3_data)
    result = str(calculation_result)
    b_9_7_2_3.insert(0, result)

def b_9_7_2_4_logic(event):
    b_9_4_4_data = b_9_4_4.get()
    b_9_7_1_4_data = b_9_7_1_4.get()
    calculation_result = float(b_9_4_4_data) * float(b_9_7_1_4_data)
    result = str(calculation_result)
    b_9_7_2_4.insert(0, result)

def b_9_7_2_5_logic(event):
    b_9_4_5_data = b_9_4_5.get()
    b_9_7_1_5_data = b_9_7_1_5.get()
    calculation_result = float(b_9_4_5_data) * float(b_9_7_1_5_data)
    result = str(calculation_result)
    b_9_7_2_5.insert(0, result)

def b_9_7_2_6_logic(event):
    b_9_4_6_data = b_9_4_6.get()
    b_9_7_1_6_data = b_9_7_1_6.get()
    calculation_result = float(b_9_4_6_data) * float(b_9_7_1_6_data)
    result = str(calculation_result)
    b_9_7_2_6.insert(0, result)

def b_9_7_2_7_logic(event):
    b_9_4_7_data = b_9_4_7.get()
    b_9_7_1_7_data = b_9_7_1_7.get()
    calculation_result = float(b_9_4_7_data) * float(b_9_7_1_7_data)
    result = str(calculation_result)
    b_9_7_2_7.insert(0, result)

def b_9_7_2_8_logic(event):
    b_9_4_8_data = b_9_4_8.get()
    b_9_7_1_8_data = b_9_7_1_8.get()
    calculation_result = float(b_9_4_8_data) * float(b_9_7_1_8_data)
    result = str(calculation_result)
    b_9_7_2_8.insert(0, result)

def b_9_7_2_9_logic(event):
    b_9_4_9_data = b_9_4_9.get()
    b_9_7_1_9_data = b_9_7_1_9.get()
    calculation_result = float(b_9_4_9_data) * float(b_9_7_1_9_data)
    result = str(calculation_result)
    b_9_7_2_9.insert(0, result)

def b_9_7_2_10_logic(event):
    b_9_4_10_data = b_9_4_10.get()
    b_9_7_1_10_data = b_9_7_1_10.get()
    calculation_result = float(b_9_4_10_data) * float(b_9_7_1_10_data)
    result = str(calculation_result)
    b_9_7_2_10.insert(0, result)

def b_9_7_2_11_logic(event):
    b_9_4_11_data = b_9_4_11.get()
    b_9_7_1_11_data = b_9_7_1_11.get()
    calculation_result = float(b_9_4_11_data) * float(b_9_7_1_11_data)
    result = str(calculation_result)
    b_9_7_2_11.insert(0, result)

def b_9_7_2_12_logic(event):
    b_9_4_12_data = b_9_4_12.get()
    b_9_7_1_12_data = b_9_7_1_12.get()
    calculation_result = float(b_9_4_12_data) * float(b_9_7_1_12_data)
    result = str(calculation_result)
    b_9_7_2_12.insert(0, result)

def b_9_7_2_13_logic(event):
    b_9_4_13_data = b_9_4_13.get()
    b_9_7_1_13_data = b_9_7_1_13.get()
    calculation_result = float(b_9_4_13_data) * float(b_9_7_1_13_data)
    result = str(calculation_result)
    b_9_7_2_13.insert(0, result)

def b_9_7_2_14_logic(event):
    b_9_4_14_data = b_9_4_14.get()
    b_9_7_1_14_data = b_9_7_1_14.get()
    calculation_result = float(b_9_4_14_data) * float(b_9_7_1_14_data)
    result = str(calculation_result)
    b_9_7_2_14.insert(0, result)

def b_9_7_2_15_logic(event):
    b_9_4_15_data = b_9_4_15.get()
    b_9_7_1_15_data = b_9_7_1_15.get()
    calculation_result = float(b_9_4_15_data) * float(b_9_7_1_15_data)
    result = str(calculation_result)
    b_9_7_2_15.insert(0, result)

def b_9_7_2_16_logic(event):
    b_9_4_16_data = b_9_4_16.get()
    b_9_7_1_16_data = b_9_7_1_16.get()
    calculation_result = float(b_9_4_16_data) * float(b_9_7_1_16_data)
    result = str(calculation_result)
    b_9_7_2_16.insert(0, result)

def b_9_7_2_17_logic(event):
    b_9_4_17_data = b_9_4_17.get()
    b_9_7_1_17_data = b_9_7_1_17.get()
    calculation_result = float(b_9_4_17_data) * float(b_9_7_1_17_data)
    result = str(calculation_result)
    b_9_7_2_17.insert(0, result)

def b_9_7_2_18_logic(event):
    b_9_4_18_data = b_9_4_18.get()
    b_9_7_1_18_data = b_9_7_1_18.get()
    calculation_result = float(b_9_4_18_data) * float(b_9_7_1_18_data)
    result = str(calculation_result)
    b_9_7_2_18.insert(0, result)

def b_9_7_2_19_logic(event):
    b_9_4_19_data = b_9_4_19.get()
    b_9_7_1_19_data = b_9_7_1_19.get()
    calculation_result = float(b_9_4_19_data) * float(b_9_7_1_19_data)
    result = str(calculation_result)
    b_9_7_2_19.insert(0, result)

def b_9_7_2_20_logic(event):
    b_9_4_20_data = b_9_4_20.get()
    b_9_7_1_20_data = b_9_7_1_20.get()
    calculation_result = float(b_9_4_20_data) * float(b_9_7_1_20_data)
    result = str(calculation_result)
    b_9_7_2_20.insert(0, result)

def b_9_7_2_21_logic(event):
    b_9_4_21_data = b_9_4_21.get()
    b_9_7_1_21_data = b_9_7_1_21.get()
    calculation_result = float(b_9_4_21_data) * float(b_9_7_1_21_data)
    result = str(calculation_result)
    b_9_7_2_21.insert(0, result)

def b_9_7_3_1_logic(event):
    b_9_7_2_1_data = b_9_7_2_1.get()
    calculation_result = 0.13 * float(b_9_7_2_1_data)
    result = str(calculation_result)
    b_9_7_3_1.insert(0, result)

def b_9_7_3_2_logic(event):
    b_9_7_2_2_data = b_9_7_2_2.get()
    calculation_result = 0.13 * float(b_9_7_2_2_data)
    result = str(calculation_result)
    b_9_7_3_2.insert(0, result)

def b_9_7_3_3_logic(event):
    b_9_7_2_3_data = b_9_7_2_3.get()
    calculation_result = 0.13 * float(b_9_7_2_3_data)
    result = str(calculation_result)
    b_9_7_3_3.insert(0, result)

def b_9_7_3_4_logic(event):
    b_9_7_2_4_data = b_9_7_2_4.get()
    calculation_result = 0.13 * float(b_9_7_2_4_data)
    result = str(calculation_result)
    b_9_7_3_4.insert(0, result)

def b_9_7_3_5_logic(event):
    b_9_7_2_5_data = b_9_7_2_5.get()
    calculation_result = 0.13 * float(b_9_7_2_5_data)
    result = str(calculation_result)
    b_9_7_3_5.insert(0, result)

def b_9_7_3_6_logic(event):
    b_9_7_2_6_data = b_9_7_2_6.get()
    calculation_result = 0.13 * float(b_9_7_2_6_data)
    result = str(calculation_result)
    b_9_7_3_6.insert(0, result)

def b_9_7_3_7_logic(event):
    b_9_7_2_7_data = b_9_7_2_7.get()
    calculation_result = 0.13 * float(b_9_7_2_7_data)
    result = str(calculation_result)
    b_9_7_3_7.insert(0, result)

def b_9_7_3_8_logic(event):
    b_9_7_2_8_data = b_9_7_2_8.get()
    calculation_result = 0.13 * float(b_9_7_2_8_data)
    result = str(calculation_result)
    b_9_7_3_8.insert(0, result)

def b_9_7_3_9_logic(event):
    b_9_7_2_9_data = b_9_7_2_9.get()
    calculation_result = 0.13 * float(b_9_7_2_9_data)
    result = str(calculation_result)
    b_9_7_3_9.insert(0, result)

def b_9_7_3_10_logic(event):
    b_9_7_2_10_data = b_9_7_2_10.get()
    calculation_result = 0.13 * float(b_9_7_2_10_data)
    result = str(calculation_result)
    b_9_7_3_10.insert(0, result)

def b_9_7_3_11_logic(event):
    b_9_7_2_11_data = b_9_7_2_11.get()
    calculation_result = 0.13 * float(b_9_7_2_11_data)
    result = str(calculation_result)
    b_9_7_3_11.insert(0, result)

def b_9_7_3_12_logic(event):
    b_9_7_2_12_data = b_9_7_2_12.get()
    calculation_result = 0.13 * float(b_9_7_2_12_data)
    result = str(calculation_result)
    b_9_7_3_12.insert(0, result)

def b_9_7_3_13_logic(event):
    b_9_7_2_13_data = b_9_7_2_13.get()
    calculation_result = 0.13 * float(b_9_7_2_13_data)
    result = str(calculation_result)
    b_9_7_3_13.insert(0, result)

def b_9_7_3_14_logic(event):
    b_9_7_2_14_data = b_9_7_2_14.get()
    calculation_result = 0.13 * float(b_9_7_2_14_data)
    result = str(calculation_result)
    b_9_7_3_14.insert(0, result)  

def b_9_7_3_15_logic(event):
    b_9_7_2_15_data = b_9_7_2_15.get()
    calculation_result = 0.13 * float(b_9_7_2_15_data)
    result = str(calculation_result)
    b_9_7_3_15.insert(0, result)

def b_9_7_3_16_logic(event):
    b_9_7_2_16_data = b_9_7_2_16.get()
    calculation_result = 0.13 * float(b_9_7_2_16_data)
    result = str(calculation_result)
    b_9_7_3_16.insert(0, result)

def b_9_7_3_17_logic(event):
    b_9_7_2_17_data = b_9_7_2_17.get()
    calculation_result = 0.13 * float(b_9_7_2_17_data)
    result = str(calculation_result)
    b_9_7_3_17.insert(0, result)

def b_9_7_3_18_logic(event):
    b_9_7_2_18_data = b_9_7_2_18.get()
    calculation_result = 0.13 * float(b_9_7_2_18_data)
    result = str(calculation_result)
    b_9_7_3_18.insert(0, result)

def b_9_7_3_19_logic(event):
    b_9_7_2_19_data = b_9_7_2_19.get()
    calculation_result = 0.13 * float(b_9_7_2_19_data)
    result = str(calculation_result)
    b_9_7_3_19.insert(0, result)

def b_9_7_3_20_logic(event):
    b_9_7_2_20_data = b_9_7_2_20.get()
    calculation_result = 0.13 * float(b_9_7_2_20_data)
    result = str(calculation_result)
    b_9_7_3_20.insert(0, result)

def b_9_7_3_21_logic(event):
    b_9_7_2_21_data = b_9_7_2_21.get()
    calculation_result = 0.13 * float(b_9_7_2_21_data)
    result = str(calculation_result)
    b_9_7_3_21.insert(0, result)

def b_9_8_logic(event):
    b_9_7_3_1_data = b_9_7_3_1.get()
    b_9_7_3_2_data = b_9_7_3_2.get()
    b_9_7_3_3_data = b_9_7_3_3.get()
    b_9_7_3_4_data = b_9_7_3_4.get()
    b_9_7_3_5_data = b_9_7_3_5.get()
    b_9_7_3_6_data = b_9_7_3_6.get()
    b_9_7_3_7_data = b_9_7_3_7.get()
    b_9_7_3_8_data = b_9_7_3_8.get()
    b_9_7_3_9_data = b_9_7_3_9.get()
    b_9_7_3_10_data = b_9_7_3_10.get()
    b_9_7_3_11_data = b_9_7_3_11.get()
    b_9_7_3_12_data = b_9_7_3_12.get()
    b_9_7_3_13_data = b_9_7_3_13.get()
    b_9_7_3_14_data = b_9_7_3_14.get()
    b_9_7_3_15_data = b_9_7_3_15.get()
    b_9_7_3_16_data = b_9_7_3_16.get()
    b_9_7_3_17_data = b_9_7_3_17.get()
    b_9_7_3_18_data = b_9_7_3_18.get()
    b_9_7_3_19_data = b_9_7_3_19.get()
    b_9_7_3_20_data = b_9_7_3_20.get()
    b_9_7_3_21_data = b_9_7_3_21.get()
    list = [float(b_9_7_3_1_data), float(b_9_7_3_2_data), float(b_9_7_3_3_data), float(b_9_7_3_4_data), float(b_9_7_3_5_data), float(b_9_7_3_6_data), float(b_9_7_3_7_data), float(b_9_7_3_8_data), float(b_9_7_3_9_data), float(b_9_7_3_10_data), float(b_9_7_3_11_data), float(b_9_7_3_12_data), float(b_9_7_3_13_data), float(b_9_7_3_14_data), float(b_9_7_3_15_data), float(b_9_7_3_16_data), float(b_9_7_3_17_data), float(b_9_7_3_18_data), float(b_9_7_3_19_data), float(b_9_7_3_20_data), float(b_9_7_3_21_data)]
    calculation_result = sum(list)
    result = str(calculation_result)
    b_9_8.insert(0, result)

def b_10_clicked():
    b_10_1_text.place(x=0, y=41)

    b_10_2_text.place(x=95, y=41)

    b_10_3_text.place(x=149, y=41)

    b_10_4_text.place(x=291, y=41)

    b_10_5_text.place(x=386, y=41)

    b_10_1_1.place(x=0, y=62)

    b_10_1_2.place(x=0, y=162)

    b_10_1_3.place(x=0, y=262)

    b_10_1_4.place(x=0, y=322)

    b_10_1_5.place(x=0, y=422)

    b_10_1_6.place(x=0, y=522)

    b_10_2_1.place(x=95, y=62)

    b_10_2_2.place(x=95, y=82)

    b_10_2_3.place(x=95, y=102)

    b_10_2_4.place(x=95, y=122)

    b_10_2_5.place(x=95, y=142)

    b_10_2_6.place(x=95, y=162)

    b_10_2_7.place(x=95, y=182)

    b_10_2_8.place(x=95, y=202)

    b_10_2_9.place(x=95, y=222)

    b_10_2_10.place(x=95, y=242)

    b_10_2_11.place(x=95, y=262)

    b_10_2_12.place(x=95, y=282)

    b_10_2_13.place(x=95, y=302)

    b_10_2_14.place(x=95, y=322)

    b_10_2_15.place(x=95, y=342)

    b_10_2_16.place(x=95, y=362)

    b_10_2_17.place(x=95, y=382)

    b_10_2_18.place(x=95, y=402)

    b_10_2_19.place(x=95, y=422)

    b_10_2_20.place(x=95, y=442)

    b_10_2_21.place(x=95, y=462)

    b_10_2_22.place(x=95, y=482)

    b_10_2_23.place(x=95, y=502)

    b_10_2_24.place(x=95, y=522)

    b_10_2_25.place(x=95, y=542)

    b_10_2_26.place(x=95, y=562)

    b_10_2_27.place(x=95, y=582)

    b_10_2_28.place(x=95, y=602)

    b_10_3_1.place(x=149, y=62)

    b_10_3_2.place(x=149, y=82)

    b_10_3_3.place(x=149, y=102)

    b_10_3_4.place(x=149, y=122)

    b_10_3_5.place(x=149, y=142)

    b_10_3_6.place(x=149, y=162)

    b_10_3_7.place(x=149, y=182)

    b_10_3_8.place(x=149, y=202)

    b_10_3_9.place(x=149, y=222)

    b_10_3_10.place(x=149, y=242)

    b_10_3_11.place(x=149, y=262)

    b_10_3_12.place(x=149, y=282)

    b_10_3_13.place(x=149, y=302)

    b_10_3_14.place(x=149, y=322)

    b_10_3_15.place(x=149, y=342)

    b_10_3_16.place(x=149, y=362)

    b_10_3_17.place(x=149, y=382)

    b_10_3_18.place(x=149, y=402)

    b_10_3_19.place(x=149, y=422)

    b_10_3_20.place(x=149, y=442)

    b_10_3_21.place(x=149, y=462)

    b_10_3_22.place(x=149, y=482)

    b_10_3_23.place(x=149, y=502)

    b_10_3_24.place(x=149, y=522)

    b_10_3_25.place(x=149, y=542)

    b_10_3_26.place(x=149, y=562)

    b_10_3_27.place(x=149, y=582)

    b_10_3_28.place(x=149, y=602)

    b_10_4_1.place(x=291, y=62)

    b_10_4_2.place(x=291, y=82)

    b_10_4_3.place(x=291, y=102)

    b_10_4_4.place(x=291, y=122)

    b_10_4_5.place(x=291, y=142)

    b_10_4_6.place(x=291, y=162)

    b_10_4_7.place(x=291, y=182)

    b_10_4_8.place(x=291, y=202)

    b_10_4_9.place(x=291, y=222)

    b_10_4_10.place(x=291, y=242)

    b_10_4_11.place(x=291, y=262)

    b_10_4_12.place(x=291, y=282)

    b_10_4_13.place(x=291, y=302)

    b_10_4_14.place(x=291, y=322)

    b_10_4_15.place(x=291, y=342)

    b_10_4_16.place(x=291, y=362)

    b_10_4_17.place(x=291, y=382)

    b_10_4_18.place(x=291, y=402)

    b_10_4_19.place(x=291, y=422)

    b_10_4_20.place(x=291, y=442)

    b_10_4_21.place(x=291, y=462)

    b_10_4_22.place(x=291, y=482)

    b_10_4_23.place(x=291, y=502)

    b_10_4_24.place(x=291, y=522)

    b_10_4_25.place(x=291, y=542)

    b_10_4_26.place(x=291, y=562)

    b_10_4_27.place(x=291, y=582)

    b_10_4_28.place(x=291, y=602)

    b_10_5_1.place(x=384, y=62)

    b_10_5_2.place(x=384, y=82)

    b_10_5_3.place(x=384, y=102)

    b_10_5_4.place(x=384, y=122)

    b_10_5_5.place(x=384, y=142)

    b_10_5_6.place(x=384, y=162)

    b_10_5_7.place(x=384, y=182)

    b_10_5_8.place(x=384, y=202)

    b_10_5_9.place(x=384, y=222)

    b_10_5_10.place(x=384, y=242)

    b_10_5_11.place(x=384, y=262)

    b_10_5_12.place(x=384, y=282)

    b_10_5_13.place(x=384, y=302)

    b_10_5_14.place(x=384, y=322)

    b_10_5_15.place(x=384, y=342)

    b_10_5_16.place(x=384, y=362)

    b_10_5_17.place(x=384, y=382)

    b_10_5_18.place(x=384, y=402)

    b_10_5_19.place(x=384, y=422)

    b_10_5_20.place(x=384, y=442)

    b_10_5_21.place(x=384, y=462)

    b_10_5_22.place(x=384, y=482)

    b_10_5_23.place(x=384, y=502)

    b_10_5_24.place(x=384, y=522)

    b_10_5_25.place(x=384, y=542)

    b_10_5_26.place(x=384, y=562)

    b_10_5_27.place(x=384, y=582)

    b_10_5_28.place(x=384, y=602)

    b_10_6.place(x=312, y=642)
    b_10_6_text.place(x=266, y=642)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()
    
    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()
    
    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_10_5_1_logic(event):
    b_10_4_1_data = b_10_4_1.get()
    calculation_result = 1.9 * float(b_10_4_1_data)
    result = str(calculation_result)
    b_10_5_1.insert(0, result)

def b_10_5_2_logic(event):
    b_10_4_2_data = b_10_4_2.get()
    calculation_result = 2.3 * float(b_10_4_2_data)
    result = str(calculation_result)
    b_10_5_2.insert(0, result)

def b_10_5_3_logic(event):
    b_10_4_3_data = b_10_4_3.get()
    calculation_result = 2.7 * float(b_10_4_3_data)
    result = str(calculation_result)
    b_10_5_3.insert(0, result)

def b_10_5_4_logic(event):
    b_10_4_4_data = b_10_4_4.get()
    calculation_result = 3.1 * float(b_10_4_4_data)
    result = str(calculation_result)
    b_10_5_4.insert(0, result)

def b_10_5_5_logic(event):
    b_10_4_5_data = b_10_4_5.get()
    calculation_result = 4.3 * float(b_10_4_5_data)
    result = str(calculation_result)
    b_10_5_5.insert(0, result)

def b_10_5_6_logic(event):
    b_10_4_6_data = b_10_4_6.get()
    calculation_result = 1.9 * float(b_10_4_6_data)
    result = str(calculation_result)
    b_10_5_6.insert(0, result)

def b_10_5_7_logic(event):
    b_10_4_7_data = b_10_4_7.get()
    calculation_result = 2.3 * float(b_10_4_7_data)
    result = str(calculation_result)
    b_10_5_7.insert(0, result)

def b_10_5_8_logic(event):
    b_10_4_8_data = b_10_4_8.get()
    calculation_result = 2.7 * float(b_10_4_8_data)
    result = str(calculation_result)
    b_10_5_8.insert(0, result)

def b_10_5_9_logic(event):
    b_10_4_9_data = b_10_4_9.get()
    calculation_result = 3.1 * float(b_10_4_9_data)
    result = str(calculation_result)
    b_10_5_9.insert(0, result)

def b_10_5_10_logic(event):
    b_10_4_10_data = b_10_4_10.get()
    calculation_result = 4.3 * float(b_10_4_10_data)
    result = str(calculation_result)
    b_10_5_10.insert(0, result)

def b_10_5_11_logic(event):
    b_10_4_11_data = b_10_4_11.get()
    calculation_result = 5.1 * float(b_10_4_11_data)
    result = str(calculation_result)
    b_10_5_11.insert(0, result)

def b_10_5_12_logic(event):
    b_10_4_12_data = b_10_4_12.get()
    calculation_result = 5.8 * float(b_10_4_12_data)
    result = str(calculation_result)
    b_10_5_12.insert(0, result)

def b_10_5_13_logic(event):
    b_10_4_13_data = b_10_4_13.get()
    calculation_result = 8.3 * float(b_10_4_13_data)
    result = str(calculation_result)
    b_10_5_13.insert(0, result)

def b_10_5_14_logic(event):
    b_10_4_14_data = b_10_4_14.get()
    calculation_result = 3.7 * float(b_10_4_14_data)
    result = str(calculation_result)
    b_10_5_14.insert(0, result)

def b_10_5_15_logic(event):
    b_10_4_15_data = b_10_4_15.get()
    calculation_result = 4.4 * float(b_10_4_15_data)
    result = str(calculation_result)
    b_10_5_15.insert(0, result)

def b_10_5_16_logic(event):
    b_10_4_16_data = b_10_4_16.get()
    calculation_result = 5.1 * float(b_10_4_16_data)
    result = str(calculation_result)
    b_10_5_16.insert(0, result)

def b_10_5_17_logic(event):
    b_10_4_17_data = b_10_4_17.get()
    calculation_result = 5.8 * float(b_10_4_17_data)
    result = str(calculation_result)
    b_10_5_17.insert(0, result)

def b_10_5_18_logic(event):
    b_10_4_18_data = b_10_4_18.get()
    calculation_result = 8.3 * float(b_10_4_18_data)
    result = str(calculation_result)
    b_10_5_18.insert(0, result)

def b_10_5_19_logic(event):
    b_10_4_19_data = b_10_4_19.get()
    calculation_result = 3.7 * float(b_10_4_19_data)
    result = str(calculation_result)
    b_10_5_19.insert(0, result)

def b_10_5_20_logic(event):
    b_10_4_20_data = b_10_4_21.get()
    calculation_result = 4.4 * float(b_10_4_20_data)
    result = str(calculation_result)
    b_10_5_20.insert(0, result)

def b_10_5_21_logic(event):
    b_10_4_21_data = b_10_4_21.get()
    calculation_result = 5.1 * float(b_10_4_21_data)
    result = str(calculation_result)
    b_10_5_21.insert(0, result)

def b_10_5_22_logic(event):
    b_10_4_22_data = b_10_4_22.get()
    calculation_result = 5.8 * float(b_10_4_22_data)
    result = str(calculation_result)
    b_10_5_22.insert(0, result)

def b_10_5_23_logic(event):
    b_10_4_23_data = b_10_4_23.get()
    calculation_result = 8.3 * float(b_10_4_23_data)
    result = str(calculation_result)
    b_10_5_23.insert(0, result)

def b_10_5_24_logic(event):
    b_10_4_24_data = b_10_4_24.get()
    calculation_result = 5.3 * float(b_10_4_24_data)
    result = str(calculation_result)
    b_10_5_24.insert(0, result)

def b_10_5_25_logic(event):
    b_10_4_25_data = b_10_4_25.get()
    calculation_result = 6.4 * float(b_10_4_25_data)
    result = str(calculation_result)
    b_10_5_25.insert(0, result)

def b_10_5_26_logic(event):
    b_10_4_26_data = b_10_4_16.get()
    calculation_result = 7.6 * float(b_10_4_26_data)
    result = str(calculation_result)
    b_10_5_26.insert(0, result)

def b_10_5_27_logic(event):
    b_10_4_27_data = b_10_4_17.get()
    calculation_result = 8.7 * float(b_10_4_27_data)
    result = str(calculation_result)
    b_10_5_27.insert(0, result)

def b_10_5_28_logic(event):
    b_10_4_28_data = b_10_4_18.get()
    calculation_result = 12.6 * float(b_10_4_28_data)
    result = str(calculation_result)
    b_10_5_28.insert(0, result)

def b_10_6_logic(event):
    b_10_5_1_data = b_10_5_1.get()
    b_10_5_2_data = b_10_5_2.get()
    b_10_5_3_data = b_10_5_3.get()
    b_10_5_4_data = b_10_5_4.get()
    b_10_5_5_data = b_10_5_5.get()
    b_10_5_6_data = b_10_5_6.get()
    b_10_5_7_data = b_10_5_7.get()
    b_10_5_8_data = b_10_5_8.get()
    b_10_5_9_data = b_10_5_9.get()
    b_10_5_10_data = b_10_5_10.get()
    b_10_5_11_data = b_10_5_11.get()
    b_10_5_12_data = b_10_5_12.get()
    b_10_5_13_data = b_10_5_13.get()
    b_10_5_14_data = b_10_5_14.get()
    b_10_5_15_data = b_10_5_15.get()
    b_10_5_16_data = b_10_5_16.get()
    b_10_5_17_data = b_10_5_17.get()
    b_10_5_18_data = b_10_5_18.get()
    b_10_5_19_data = b_10_5_19.get()
    b_10_5_20_data = b_10_5_20.get()
    b_10_5_21_data = b_10_5_21.get()
    b_10_5_22_data = b_10_5_22.get()
    b_10_5_23_data = b_10_5_23.get()
    b_10_5_24_data = b_10_5_24.get()
    b_10_5_25_data = b_10_5_25.get()
    b_10_5_26_data = b_10_5_26.get()
    b_10_5_27_data = b_10_5_27.get()
    b_10_5_28_data = b_10_5_28.get()
    list = [float(b_10_5_1_data), float(b_10_5_1_data), float(b_10_5_2_data), float(b_10_5_3_data), float(b_10_5_4_data), float(b_10_5_5_data), float(b_10_5_6_data), float(b_10_5_7_data), float(b_10_5_8_data), float(b_10_5_9_data), float(b_10_5_10_data), float(b_10_5_11_data), float(b_10_5_12_data), float(b_10_5_13_data), float(b_10_5_14_data), float(b_10_5_15_data), float(b_10_5_16_data), float(b_10_5_17_data), float(b_10_5_18_data), float(b_10_5_19_data), float(b_10_5_20_data), float(b_10_5_21_data), float(b_10_5_22_data), float(b_10_5_23_data), float(b_10_5_24_data), float(b_10_5_25_data), float(b_10_5_26_data), float(b_10_5_27_data), float(b_10_5_28_data)]
    calculation_result = sum(list)
    result = str(calculation_result)
    b_10_6.insert(0, result)

def b_11_clicked():
    b_11_1_text.place(x=0, y=41)

    b_11_1_1_text.place(x=18, y=62)

    b_11_1_2_text.place(x=115, y=62)

    b_11_1_3_text.place(x=200, y=62)

    b_11_1_1_1.place(x=0, y=82)

    b_11_1_1_2.place(x=0, y=102)

    b_11_1_1_3.place(x=0, y=122)

    b_11_1_1_4.place(x=0, y=142)

    b_11_1_1_5.place(x=0, y=162)

    b_11_1_1_6.place(x=0, y=182)

    b_11_1_1_7.place(x=0, y=202)

    b_11_1_1_8.place(x=0, y=222)

    b_11_1_1_9.place(x=0, y=242)

    b_11_1_1_10.place(x=0, y=262)

    b_11_1_2_1.place(x=93, y=82)

    b_11_1_2_2.place(x=93, y=102)

    b_11_1_2_3.place(x=93, y=122)

    b_11_1_2_4.place(x=93, y=142)

    b_11_1_2_5.place(x=93, y=162)

    b_11_1_2_6.place(x=93, y=182)

    b_11_1_2_7.place(x=93, y=202)

    b_11_1_2_8.place(x=93, y=222)

    b_11_1_2_9.place(x=93, y=242)

    b_11_1_2_10.place(x=93, y=262)

    b_11_1_3_1.place(x=186, y=82)

    b_11_1_3_2.place(x=186, y=102)

    b_11_1_3_3.place(x=186, y=122)

    b_11_1_3_4.place(x=186, y=142)

    b_11_1_3_5.place(x=186, y=162)

    b_11_1_3_6.place(x=186, y=182)

    b_11_1_3_7.place(x=186, y=202)

    b_11_1_3_8.place(x=186, y=222)

    b_11_1_3_9.place(x=186, y=242)

    b_11_1_3_10.place(x=186, y=262)

    b_11_1_4.place(x=35, y=292)
    b_11_1_4_text.place(x=0, y=292)

    b_11_2_text.place(x=300, y=41)

    b_11_2_1_text.place(x=338, y=62)

    b_11_2_2_text.place(x=425, y=62)

    b_11_2_3_text.place(x=510, y=62)

    b_11_2_4_text.place(x=585, y=62)

    b_11_2_5_text.place(x=680, y=62)

    b_11_2_6_text.place(x=785, y=62)

    b_11_2_1_1.place(x=305, y=82)

    b_11_2_1_2.place(x=305, y=102)

    b_11_2_1_3.place(x=305, y=122)

    b_11_2_1_4.place(x=305, y=142)

    b_11_2_1_5.place(x=305, y=162)

    b_11_2_1_6.place(x=305, y=182)

    b_11_2_1_7.place(x=305, y=202)

    b_11_2_1_8.place(x=305, y=222)

    b_11_2_1_9.place(x=305, y=242)

    b_11_2_1_10.place(x=305, y=262)

    b_11_2_1_11.place(x=305, y=282)

    b_11_2_1_12.place(x=305, y=302)

    b_11_2_1_13.place(x=305, y=322)

    b_11_2_1_14.place(x=305, y=342)

    b_11_2_1_15.place(x=305, y=362)

    b_11_2_1_16.place(x=305, y=382)

    b_11_2_1_17.place(x=305, y=402)

    b_11_2_1_18.place(x=305, y=422)

    b_11_2_1_19.place(x=305, y=442)

    b_11_2_1_20.place(x=305, y=462)

    b_11_2_1_21.place(x=305, y=482)

    b_11_2_1_22.place(x=305, y=502)

    b_11_2_1_23.place(x=305, y=522)

    b_11_2_2_1.place(x=398, y=82)

    b_11_2_2_2.place(x=398, y=102)

    b_11_2_2_3.place(x=398, y=122)

    b_11_2_2_4.place(x=398, y=142)

    b_11_2_2_5.place(x=398, y=162)

    b_11_2_2_6.place(x=398, y=182)

    b_11_2_2_7.place(x=398, y=202)

    b_11_2_2_8.place(x=398, y=222)

    b_11_2_2_9.place(x=398, y=242)

    b_11_2_2_10.place(x=398, y=262)

    b_11_2_2_11.place(x=398, y=282)

    b_11_2_2_12.place(x=398, y=302)

    b_11_2_2_13.place(x=398, y=322)

    b_11_2_2_14.place(x=398, y=342)

    b_11_2_2_15.place(x=398, y=362)

    b_11_2_2_16.place(x=398, y=382)

    b_11_2_2_17.place(x=398, y=402)

    b_11_2_2_18.place(x=398, y=422)

    b_11_2_2_19.place(x=398, y=442)

    b_11_2_2_20.place(x=398, y=462)

    b_11_2_2_21.place(x=398, y=482)

    b_11_2_2_22.place(x=398, y=502)

    b_11_2_2_23.place(x=398, y=522)

    b_11_2_3_1.place(x=491, y=82)

    b_11_2_3_2.place(x=491, y=102)

    b_11_2_3_3.place(x=491, y=122)

    b_11_2_3_4.place(x=491, y=142)

    b_11_2_3_5.place(x=491, y=162)

    b_11_2_3_6.place(x=491, y=182)

    b_11_2_3_7.place(x=491, y=202)

    b_11_2_3_8.place(x=491, y=222)

    b_11_2_3_9.place(x=491, y=242)

    b_11_2_3_10.place(x=491, y=262)

    b_11_2_3_11.place(x=491, y=282)

    b_11_2_3_12.place(x=491, y=302)

    b_11_2_3_13.place(x=491, y=322)

    b_11_2_3_14.place(x=491, y=342)

    b_11_2_3_15.place(x=491, y=362)

    b_11_2_3_16.place(x=491, y=382)

    b_11_2_3_17.place(x=491, y=402)

    b_11_2_3_18.place(x=491, y=422)

    b_11_2_3_19.place(x=491, y=442)

    b_11_2_3_20.place(x=491, y=462)

    b_11_2_3_21.place(x=491, y=482)

    b_11_2_3_22.place(x=491, y=502)

    b_11_2_3_23.place(x=491, y=522)

    b_11_2_4_1.place(x=584, y=82)

    b_11_2_4_2.place(x=584, y=102)

    b_11_2_4_3.place(x=584, y=122)

    b_11_2_4_4.place(x=584, y=142)

    b_11_2_4_5.place(x=584, y=162)

    b_11_2_4_6.place(x=584, y=182)

    b_11_2_4_7.place(x=584, y=202)

    b_11_2_4_8.place(x=584, y=222)

    b_11_2_4_9.place(x=584, y=242)

    b_11_2_4_10.place(x=584, y=262)

    b_11_2_4_11.place(x=584, y=282)

    b_11_2_4_12.place(x=584, y=302)

    b_11_2_4_13.place(x=584, y=322)

    b_11_2_4_14.place(x=584, y=342)

    b_11_2_4_15.place(x=584, y=362)

    b_11_2_4_16.place(x=584, y=382)

    b_11_2_4_17.place(x=584, y=402)

    b_11_2_4_18.place(x=584, y=422)

    b_11_2_4_19.place(x=584, y=442)

    b_11_2_4_20.place(x=584, y=462)

    b_11_2_4_21.place(x=584, y=482)

    b_11_2_4_22.place(x=584, y=502)

    b_11_2_4_23.place(x=584, y=522)

    b_11_2_5_1.place(x=677, y=82)

    b_11_2_5_2.place(x=677, y=102)

    b_11_2_5_3.place(x=677, y=122)

    b_11_2_5_4.place(x=677, y=142)

    b_11_2_5_5.place(x=677, y=162)

    b_11_2_5_6.place(x=677, y=182)

    b_11_2_5_7.place(x=677, y=202)

    b_11_2_5_8.place(x=677, y=222)

    b_11_2_5_9.place(x=677, y=242)

    b_11_2_5_10.place(x=677, y=262)

    b_11_2_5_11.place(x=677, y=282)

    b_11_2_5_12.place(x=677, y=302)

    b_11_2_5_13.place(x=677, y=322)

    b_11_2_5_14.place(x=677, y=342)

    b_11_2_5_15.place(x=677, y=362)

    b_11_2_5_16.place(x=677, y=382)

    b_11_2_5_17.place(x=677, y=402)

    b_11_2_5_18.place(x=677, y=422)

    b_11_2_5_19.place(x=677, y=442)

    b_11_2_5_20.place(x=677, y=462)

    b_11_2_5_21.place(x=677, y=482)

    b_11_2_5_22.place(x=677, y=502)

    b_11_2_5_23.place(x=677, y=522)

    b_11_2_6_1.place(x=770, y=82)

    b_11_2_6_2.place(x=770, y=102)

    b_11_2_6_3.place(x=770, y=122)

    b_11_2_6_4.place(x=770, y=142)

    b_11_2_6_5.place(x=770, y=162)

    b_11_2_6_6.place(x=770, y=182)

    b_11_2_6_7.place(x=770, y=202)

    b_11_2_6_8.place(x=770, y=222)

    b_11_2_6_9.place(x=770, y=242)

    b_11_2_6_10.place(x=770, y=262)

    b_11_2_6_11.place(x=770, y=282)

    b_11_2_6_12.place(x=770, y=302)

    b_11_2_6_13.place(x=770, y=322)

    b_11_2_6_14.place(x=770, y=342)

    b_11_2_6_15.place(x=770, y=362)

    b_11_2_6_16.place(x=770, y=382)

    b_11_2_6_17.place(x=770, y=402)

    b_11_2_6_18.place(x=770, y=422)

    b_11_2_6_19.place(x=770, y=442)

    b_11_2_6_20.place(x=770, y=462)

    b_11_2_6_21.place(x=770, y=482)

    b_11_2_6_22.place(x=770, y=502)

    b_11_2_6_23.place(x=770, y=522)

    b_11_2_7.place(x=712, y=562)
    b_11_2_7_text1.place(x=676, y=562)
    b_11_2_7_text2.place(x=909, y=562)

    b_11_2_8.place(x=712, y=592)
    b_11_2_8_text.place(x=909, y=592)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  

    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_11_1_3_1_logic(event):
    b_11_1_1_1_data = b_11_1_1_1.get()
    b_11_1_2_1_data = b_11_1_2_1.get()
    calculation_result = (float(b_11_1_1_1_data) / 1000) * mt.pi * float(b_11_1_2_1_data)
    result = str(calculation_result)
    b_11_1_3_1.insert(0, result)

def b_11_1_3_2_logic(event):
    b_11_1_1_2_data = b_11_1_1_2.get()
    b_11_1_2_2_data = b_11_1_2_2.get()
    calculation_result = (float(b_11_1_1_2_data) / 1000) * mt.pi * float(b_11_1_2_2_data)
    result = str(calculation_result)
    b_11_1_3_2.insert(0, result)

def b_11_1_3_3_logic(event):
    b_11_1_1_3_data = b_11_1_1_3.get()
    b_11_1_2_3_data = b_11_1_2_3.get()
    calculation_result = (float(b_11_1_1_3_data) / 1000) * mt.pi * float(b_11_1_2_3_data)
    result = str(calculation_result)
    b_11_1_3_3.insert(0, result)

def b_11_1_3_4_logic(event):
    b_11_1_1_4_data = b_11_1_1_4.get()
    b_11_1_2_4_data = b_11_1_2_4.get()
    calculation_result = (float(b_11_1_1_4_data) / 1000) * mt.pi * float(b_11_1_2_4_data)
    result = str(calculation_result)
    b_11_1_3_4.insert(0, result)

def b_11_1_3_5_logic(event):
    b_11_1_1_5_data = b_11_1_1_5.get()
    b_11_1_2_5_data = b_11_1_2_5.get()
    calculation_result = (float(b_11_1_1_5_data) / 1000) * mt.pi * float(b_11_1_2_5_data)
    result = str(calculation_result)
    b_11_1_3_5.insert(0, result)

def b_11_1_3_6_logic(event):
    b_11_1_1_6_data = b_11_1_1_6.get()
    b_11_1_2_6_data = b_11_1_2_6.get()
    calculation_result = (float(b_11_1_1_6_data) / 1000) * mt.pi * float(b_11_1_2_6_data)
    result = str(calculation_result)
    b_11_1_3_6.insert(0, result)

def b_11_1_3_7_logic(event):
    b_11_1_1_7_data = b_11_1_1_7.get()
    b_11_1_2_7_data = b_11_1_2_7.get()
    calculation_result = (float(b_11_1_1_7_data) / 1000) * mt.pi * float(b_11_1_2_7_data)
    result = str(calculation_result)
    b_11_1_3_7.insert(0, result)

def b_11_1_3_8_logic(event):
    b_11_1_1_8_data = b_11_1_1_8.get()
    b_11_1_2_8_data = b_11_1_2_8.get()
    calculation_result = (float(b_11_1_1_8_data) / 1000) * mt.pi * float(b_11_1_2_8_data)
    result = str(calculation_result)
    b_11_1_3_8.insert(0, result)

def b_11_1_3_9_logic(event):
    b_11_1_1_9_data = b_11_1_1_9.get()
    b_11_1_2_9_data = b_11_1_2_9.get()
    calculation_result = (float(b_11_1_1_9_data) / 1000) * mt.pi * float(b_11_1_2_9_data)
    result = str(calculation_result)
    b_11_1_3_9.insert(0, result)

def b_11_1_3_10_logic(event):
    b_11_1_1_10_data = b_11_1_1_10.get()
    b_11_1_2_10_data = b_11_1_2_10.get()
    calculation_result = (float(b_11_1_1_10_data) / 1000) * mt.pi * float(b_11_1_2_10_data)
    result = str(calculation_result)
    b_11_1_3_10.insert(0, result)

def b_11_1_4_logic(event):
    b_11_1_3_1_data = b_11_1_3_1.get()
    b_11_1_3_2_data = b_11_1_3_2.get()
    b_11_1_3_3_data = b_11_1_3_3.get()
    b_11_1_3_4_data = b_11_1_3_4.get()
    b_11_1_3_5_data = b_11_1_3_5.get()
    b_11_1_3_6_data = b_11_1_3_6.get()
    b_11_1_3_7_data = b_11_1_3_7.get()
    b_11_1_3_8_data = b_11_1_3_8.get()
    b_11_1_3_9_data = b_11_1_3_9.get()
    b_11_1_3_10_data = b_11_1_3_10.get()
    list = [float(b_11_1_3_1_data), float(b_11_1_3_2_data), float(b_11_1_3_3_data), float(b_11_1_3_4_data), float(b_11_1_3_5_data), float(b_11_1_3_6_data), float(b_11_1_3_7_data), float(b_11_1_3_8_data), float(b_11_1_3_9_data), float(b_11_1_3_10_data)]
    calculation_result = sum(list)
    result = str(calculation_result)
    b_11_1_4.insert(0, result)

def b_11_2_4_1_logic(event):
    b_11_2_1_1_data = b_11_2_1_1.get()
    b_11_2_2_1_data = b_11_2_2_1.get()
    b_11_2_3_1_data = b_11_2_3_1.get()
    calculation_result = 2 * ((float(b_11_2_1_1_data) + float(b_11_2_2_1_data)) / 1000) * float(b_11_2_3_1_data)
    result = str(calculation_result)
    b_11_2_4_1.insert(0, result)

def b_11_2_4_2_logic(event):
    b_11_2_1_2_data = b_11_2_1_2.get()
    b_11_2_2_2_data = b_11_2_2_2.get()
    b_11_2_3_2_data = b_11_2_3_2.get()
    calculation_result = 2 * ((float(b_11_2_1_2_data) + float(b_11_2_2_2_data)) / 1000) * float(b_11_2_3_2_data)
    result = str(calculation_result)
    b_11_2_4_2.insert(0, result) 

def b_11_2_4_3_logic(event):
    b_11_2_1_3_data = b_11_2_1_3.get()
    b_11_2_2_3_data = b_11_2_2_3.get()
    b_11_2_3_3_data = b_11_2_3_3.get()
    calculation_result = 2 * ((float(b_11_2_1_3_data) + float(b_11_2_2_3_data)) / 1000) * float(b_11_2_3_3_data)
    result = str(calculation_result)
    b_11_2_4_3.insert(0, result)

def b_11_2_4_4_logic(event):
    b_11_2_1_4_data = b_11_2_1_4.get()
    b_11_2_2_4_data = b_11_2_2_4.get()
    b_11_2_3_4_data = b_11_2_3_4.get()
    calculation_result = 2 * ((float(b_11_2_1_4_data) + float(b_11_2_2_4_data)) / 1000) * float(b_11_2_3_4_data)
    result = str(calculation_result)
    b_11_2_4_4.insert(0, result)

def b_11_2_4_5_logic(event):
    b_11_2_1_5_data = b_11_2_1_5.get()
    b_11_2_2_5_data = b_11_2_2_5.get()
    b_11_2_3_5_data = b_11_2_3_5.get()
    calculation_result = 2 * ((float(b_11_2_1_5_data) + float(b_11_2_2_5_data)) / 1000) * float(b_11_2_3_5_data)
    result = str(calculation_result)
    b_11_2_4_5.insert(0, result)

def b_11_2_4_6_logic(event):
    b_11_2_1_6_data = b_11_2_1_6.get()
    b_11_2_2_6_data = b_11_2_2_6.get()
    b_11_2_3_6_data = b_11_2_3_6.get()
    calculation_result = 2 * ((float(b_11_2_1_6_data) + float(b_11_2_2_6_data)) / 1000) * float(b_11_2_3_6_data)
    result = str(calculation_result)
    b_11_2_4_6.insert(0, result)

def b_11_2_4_7_logic(event):
    b_11_2_1_7_data = b_11_2_1_7.get()
    b_11_2_2_7_data = b_11_2_2_7.get()
    b_11_2_3_7_data = b_11_2_3_7.get()
    calculation_result = 2 * ((float(b_11_2_1_7_data) + float(b_11_2_2_7_data)) / 1000) * float(b_11_2_3_7_data)
    result = str(calculation_result)
    b_11_2_4_7.insert(0, result)

def b_11_2_4_8_logic(event):
    b_11_2_1_8_data = b_11_2_1_8.get()
    b_11_2_2_8_data = b_11_2_2_8.get()
    b_11_2_3_8_data = b_11_2_3_8.get()
    calculation_result = 2 * ((float(b_11_2_1_8_data) + float(b_11_2_2_8_data)) / 1000) * float(b_11_2_3_8_data)
    result = str(calculation_result)
    b_11_2_4_8.insert(0, result)

def b_11_2_4_9_logic(event):
    b_11_2_1_9_data = b_11_2_1_9.get()
    b_11_2_2_9_data = b_11_2_2_9.get()
    b_11_2_3_9_data = b_11_2_3_9.get()
    calculation_result = 2 * ((float(b_11_2_1_9_data) + float(b_11_2_2_9_data)) / 1000) * float(b_11_2_3_9_data)
    result = str(calculation_result)
    b_11_2_4_9.insert(0, result)

def b_11_2_4_10_logic(event):
    b_11_2_1_10_data = b_11_2_1_10.get()
    b_11_2_2_10_data = b_11_2_2_10.get()
    b_11_2_3_10_data = b_11_2_3_10.get()
    calculation_result = 2 * ((float(b_11_2_1_10_data) + float(b_11_2_2_10_data)) / 1000) * float(b_11_2_3_10_data)
    result = str(calculation_result)
    b_11_2_4_10.insert(0, result)

def b_11_2_4_11_logic(event):
    b_11_2_1_11_data = b_11_2_1_11.get()
    b_11_2_2_11_data = b_11_2_2_11.get()
    b_11_2_3_11_data = b_11_2_3_11.get()
    calculation_result = 2 * ((float(b_11_2_1_11_data) + float(b_11_2_2_11_data)) / 1000) * float(b_11_2_3_11_data)
    result = str(calculation_result)
    b_11_2_4_11.insert(0, result)

def b_11_2_4_12_logic(event):
    b_11_2_1_12_data = b_11_2_1_12.get()
    b_11_2_2_12_data = b_11_2_2_12.get()
    b_11_2_3_12_data = b_11_2_3_12.get()
    calculation_result = 2 * ((float(b_11_2_1_12_data) + float(b_11_2_2_12_data)) / 1000) * float(b_11_2_3_12_data)
    result = str(calculation_result)
    b_11_2_4_12.insert(0, result)

def b_11_2_4_13_logic(event):
    b_11_2_1_13_data = b_11_2_1_13.get()
    b_11_2_2_13_data = b_11_2_2_13.get()
    b_11_2_3_13_data = b_11_2_3_13.get()
    calculation_result = 2 * ((float(b_11_2_1_13_data) + float(b_11_2_2_13_data)) / 1000) * float(b_11_2_3_13_data)
    result = str(calculation_result)
    b_11_2_4_13.insert(0, result)

def b_11_2_4_14_logic(event):
    b_11_2_1_14_data = b_11_2_1_14.get()
    b_11_2_2_14_data = b_11_2_2_14.get()
    b_11_2_3_14_data = b_11_2_3_14.get()
    calculation_result = 2 * ((float(b_11_2_1_14_data) + float(b_11_2_2_14_data)) / 1000) * float(b_11_2_3_14_data)
    result = str(calculation_result)
    b_11_2_4_14.insert(0, result)

def b_11_2_4_15_logic(event):
    b_11_2_1_15_data = b_11_2_1_15.get()
    b_11_2_2_15_data = b_11_2_2_15.get()
    b_11_2_3_15_data = b_11_2_3_15.get()
    calculation_result = 2 * ((float(b_11_2_1_15_data) + float(b_11_2_2_15_data)) / 1000) * float(b_11_2_3_15_data)
    result = str(calculation_result)
    b_11_2_4_15.insert(0, result)

def b_11_2_4_16_logic(event):
    b_11_2_1_16_data = b_11_2_1_16.get()
    b_11_2_2_16_data = b_11_2_2_16.get()
    b_11_2_3_16_data = b_11_2_3_16.get()
    calculation_result = 2 * ((float(b_11_2_1_16_data) + float(b_11_2_2_16_data)) / 1000) * float(b_11_2_3_16_data)
    result = str(calculation_result)
    b_11_2_4_16.insert(0, result)

def b_11_2_4_17_logic(event):
    b_11_2_1_17_data = b_11_2_1_17.get()
    b_11_2_2_17_data = b_11_2_2_17.get()
    b_11_2_3_17_data = b_11_2_3_17.get()
    calculation_result = 2 * ((float(b_11_2_1_17_data) + float(b_11_2_2_17_data)) / 1000) * float(b_11_2_3_17_data)
    result = str(calculation_result)
    b_11_2_4_17.insert(0, result)

def b_11_2_4_18_logic(event):
    b_11_2_1_18_data = b_11_2_1_18.get()
    b_11_2_2_18_data = b_11_2_2_18.get()
    b_11_2_3_18_data = b_11_2_3_18.get()
    calculation_result = 2 * ((float(b_11_2_1_18_data) + float(b_11_2_2_18_data)) / 1000) * float(b_11_2_3_18_data)
    result = str(calculation_result)
    b_11_2_4_18.insert(0, result)

def b_11_2_4_19_logic(event):
    b_11_2_1_19_data = b_11_2_1_19.get()
    b_11_2_2_19_data = b_11_2_2_19.get()
    b_11_2_3_19_data = b_11_2_3_19.get()
    calculation_result = 2 * ((float(b_11_2_1_19_data) + float(b_11_2_2_19_data)) / 1000) * float(b_11_2_3_19_data)
    result = str(calculation_result)
    b_11_2_4_19.insert(0, result)

def b_11_2_4_20_logic(event):
    b_11_2_1_20_data = b_11_2_1_20.get()
    b_11_2_2_20_data = b_11_2_2_20.get()
    b_11_2_3_20_data = b_11_2_3_20.get()
    calculation_result = 2 * ((float(b_11_2_1_20_data) + float(b_11_2_2_20_data)) / 1000) * float(b_11_2_3_20_data)
    result = str(calculation_result)
    b_11_2_4_20.insert(0, result)

def b_11_2_4_21_logic(event):
    b_11_2_1_21_data = b_11_2_1_21.get()
    b_11_2_2_21_data = b_11_2_2_21.get()
    b_11_2_3_21_data = b_11_2_3_21.get()
    calculation_result = 2 * ((float(b_11_2_1_21_data) + float(b_11_2_2_21_data)) / 1000) * float(b_11_2_3_21_data)
    result = str(calculation_result)
    b_11_2_4_21.insert(0, result)

def b_11_2_4_22_logic(event):
    b_11_2_1_22_data = b_11_2_1_22.get()
    b_11_2_2_22_data = b_11_2_2_22.get()
    b_11_2_3_22_data = b_11_2_3_22.get()
    calculation_result = 2 * ((float(b_11_2_1_22_data) + float(b_11_2_2_22_data)) / 1000) * float(b_11_2_3_22_data)
    result = str(calculation_result)
    b_11_2_4_22.insert(0, result)

def b_11_2_4_23_logic(event):
    b_11_2_1_23_data = b_11_2_1_23.get()
    b_11_2_2_23_data = b_11_2_2_23.get()
    b_11_2_3_23_data = b_11_2_3_23.get()
    calculation_result = 2 * ((float(b_11_2_1_23_data) + float(b_11_2_2_23_data)) / 1000) * float(b_11_2_3_23_data)
    result = str(calculation_result)
    b_11_2_4_23.insert(0, result)

def b_11_2_7_logic(event):
    b_11_2_4_1_data = b_11_2_4_1.get()
    b_11_2_4_2_data = b_11_2_4_2.get()
    b_11_2_4_3_data = b_11_2_4_3.get()
    b_11_2_4_4_data = b_11_2_4_4.get()
    b_11_2_4_5_data = b_11_2_4_5.get()
    b_11_2_4_6_data = b_11_2_4_6.get()
    b_11_2_4_7_data = b_11_2_4_7.get()
    b_11_2_4_8_data = b_11_2_4_8.get()
    b_11_2_4_9_data = b_11_2_4_9.get()
    b_11_2_4_10_data = b_11_2_4_10.get()
    b_11_2_4_11_data = b_11_2_4_11.get()
    b_11_2_4_12_data = b_11_2_4_12.get()
    b_11_2_4_13_data = b_11_2_4_13.get()
    b_11_2_4_14_data = b_11_2_4_14.get()
    b_11_2_4_15_data = b_11_2_4_15.get()
    b_11_2_4_16_data = b_11_2_4_16.get()
    b_11_2_4_17_data = b_11_2_4_17.get()
    b_11_2_4_18_data = b_11_2_4_18.get()
    b_11_2_4_19_data = b_11_2_4_19.get()
    b_11_2_4_20_data = b_11_2_4_20.get()
    b_11_2_4_21_data = b_11_2_4_21.get()
    b_11_2_4_22_data = b_11_2_4_22.get()
    b_11_2_4_23_data = b_11_2_4_23.get()
    list = [float(b_11_2_4_1_data), float(b_11_2_4_2_data), float(b_11_2_4_3_data), float(b_11_2_4_4_data), float(b_11_2_4_5_data), float(b_11_2_4_6_data), float(b_11_2_4_7_data), float(b_11_2_4_8_data), float(b_11_2_4_9_data), float(b_11_2_4_10_data), float(b_11_2_4_11_data), float(b_11_2_4_12_data), float(b_11_2_4_13_data), float(b_11_2_4_14_data), float(b_11_2_4_15_data), float(b_11_2_4_16_data), float(b_11_2_4_17_data), float(b_11_2_4_18_data), float(b_11_2_4_19_data), float(b_11_2_4_20_data), float(b_11_2_4_21_data), float(b_11_2_4_22_data), float(b_11_2_4_23_data)]
    calculation_result = sum(list)
    result = str(calculation_result)
    b_11_2_7.insert(0, result)

def b_11_2_6_1_logic(event):
    b_11_2_4_1_data = b_11_2_4_1.get()
    b_11_2_5_1_data = b_11_2_5_1.get()
    calculation_result = float(b_11_2_4_1_data) * float(b_11_2_5_1_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_1.insert(0, result)

def b_11_2_6_2_logic(event):
    b_11_2_4_2_data = b_11_2_4_2.get()
    b_11_2_5_2_data = b_11_2_5_2.get()
    calculation_result = float(b_11_2_4_2_data) * float(b_11_2_5_2_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_2.insert(0, result)

def b_11_2_6_3_logic(event):
    b_11_2_4_3_data = b_11_2_4_3.get()
    b_11_2_5_3_data = b_11_2_5_3.get()
    calculation_result = float(b_11_2_4_3_data) * float(b_11_2_5_3_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_3.insert(0, result)

def b_11_2_6_4_logic(event):
    b_11_2_4_4_data = b_11_2_4_4.get()
    b_11_2_5_4_data = b_11_2_5_4.get()
    calculation_result = float(b_11_2_4_4_data) * float(b_11_2_5_4_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_4.insert(0, result)

def b_11_2_6_5_logic(event):
    b_11_2_4_5_data = b_11_2_4_5.get()
    b_11_2_5_5_data = b_11_2_5_5.get()
    calculation_result = float(b_11_2_4_5_data) * float(b_11_2_5_5_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_5.insert(0, result)

def b_11_2_6_6_logic(event):
    b_11_2_4_6_data = b_11_2_4_6.get()
    b_11_2_5_6_data = b_11_2_5_6.get()
    calculation_result = float(b_11_2_4_6_data) * float(b_11_2_5_6_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_6.insert(0, result)

def b_11_2_6_7_logic(event):
    b_11_2_4_7_data = b_11_2_4_7.get()
    b_11_2_5_7_data = b_11_2_5_7.get()
    calculation_result = float(b_11_2_4_7_data) * float(b_11_2_5_7_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_7.insert(0, result)

def b_11_2_6_8_logic(event):
    b_11_2_4_8_data = b_11_2_4_8.get()
    b_11_2_5_8_data = b_11_2_5_8.get()
    calculation_result = float(b_11_2_4_8_data) * float(b_11_2_5_8_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_8.insert(0, result)

def b_11_2_6_9_logic(event):
    b_11_2_4_9_data = b_11_2_4_9.get()
    b_11_2_5_9_data = b_11_2_5_9.get()
    calculation_result = float(b_11_2_4_9_data) * float(b_11_2_5_9_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_9.insert(0, result)

def b_11_2_6_10_logic(event):
    b_11_2_4_10_data = b_11_2_4_10.get()
    b_11_2_5_10_data = b_11_2_5_10.get()
    calculation_result = float(b_11_2_4_10_data) * float(b_11_2_5_10_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_10.insert(0, result)

def b_11_2_6_11_logic(event):
    b_11_2_4_11_data = b_11_2_4_11.get()
    b_11_2_5_11_data = b_11_2_5_11.get()
    calculation_result = float(b_11_2_4_11_data) * float(b_11_2_5_11_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_11.insert(0, result)

def b_11_2_6_12_logic(event):
    b_11_2_4_12_data = b_11_2_4_12.get()
    b_11_2_5_12_data = b_11_2_5_12.get()
    calculation_result = float(b_11_2_4_12_data) * float(b_11_2_5_12_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_12.insert(0, result)

def b_11_2_6_13_logic(event):
    b_11_2_4_13_data = b_11_2_4_13.get()
    b_11_2_5_13_data = b_11_2_5_13.get()
    calculation_result = float(b_11_2_4_13_data) * float(b_11_2_5_13_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_13.insert(0, result)

def b_11_2_6_14_logic(event):
    b_11_2_4_14_data = b_11_2_4_14.get()
    b_11_2_5_14_data = b_11_2_5_14.get()
    calculation_result = float(b_11_2_4_14_data) * float(b_11_2_5_14_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_14.insert(0, result)

def b_11_2_6_15_logic(event):
    b_11_2_4_15_data = b_11_2_4_15.get()
    b_11_2_5_15_data = b_11_2_5_15.get()
    calculation_result = float(b_11_2_4_15_data) * float(b_11_2_5_15_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_15.insert(0, result)

def b_11_2_6_16_logic(event):
    b_11_2_4_16_data = b_11_2_4_16.get()
    b_11_2_5_16_data = b_11_2_5_16.get()
    calculation_result = float(b_11_2_4_16_data) * float(b_11_2_5_16_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_16.insert(0, result)

def b_11_2_6_17_logic(event):
    b_11_2_4_17_data = b_11_2_4_17.get()
    b_11_2_5_17_data = b_11_2_5_17.get()
    calculation_result = float(b_11_2_4_17_data) * float(b_11_2_5_17_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_17.insert(0, result)

def b_11_2_6_18_logic(event):
    b_11_2_4_18_data = b_11_2_4_18.get()
    b_11_2_5_18_data = b_11_2_5_18.get()
    calculation_result = float(b_11_2_4_18_data) * float(b_11_2_5_18_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_18.insert(0, result)

def b_11_2_6_19_logic(event):
    b_11_2_4_19_data = b_11_2_4_19.get()
    b_11_2_5_19_data = b_11_2_5_19.get()
    calculation_result = float(b_11_2_4_19_data) * float(b_11_2_5_19_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_19.insert(0, result)

def b_11_2_6_20_logic(event):
    b_11_2_4_20_data = b_11_2_4_20.get()
    b_11_2_5_20_data = b_11_2_5_20.get()
    calculation_result = float(b_11_2_4_20_data) * float(b_11_2_5_20_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_20.insert(0, result)

def b_11_2_6_21_logic(event):
    b_11_2_4_21_data = b_11_2_4_21.get()
    b_11_2_5_21_data = b_11_2_5_21.get()
    calculation_result = float(b_11_2_4_21_data) * float(b_11_2_5_21_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_21.insert(0, result)

def b_11_2_6_22_logic(event):
    b_11_2_4_22_data = b_11_2_4_22.get()
    b_11_2_5_22_data = b_11_2_5_22.get()
    calculation_result = float(b_11_2_4_22_data) * float(b_11_2_5_22_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_22.insert(0, result)

def b_11_2_6_23_logic(event):
    b_11_2_4_23_data = b_11_2_4_23.get()
    b_11_2_5_23_data = b_11_2_5_23.get()
    calculation_result = float(b_11_2_4_23_data) * float(b_11_2_5_23_data) * 7.9
    result = str(calculation_result)
    b_11_2_6_23.insert(0, result)

def b_11_2_8_logic(event):
    b_11_2_6_1_data = b_11_2_6_1.get()
    b_11_2_6_2_data = b_11_2_6_2.get()
    b_11_2_6_3_data = b_11_2_6_3.get()
    b_11_2_6_4_data = b_11_2_6_4.get()
    b_11_2_6_5_data = b_11_2_6_5.get()
    b_11_2_6_6_data = b_11_2_6_6.get()
    b_11_2_6_7_data = b_11_2_6_7.get()
    b_11_2_6_8_data = b_11_2_6_8.get()
    b_11_2_6_9_data = b_11_2_6_9.get()
    b_11_2_6_10_data = b_11_2_6_10.get()
    b_11_2_6_11_data = b_11_2_6_11.get()
    b_11_2_6_12_data = b_11_2_6_12.get()
    b_11_2_6_13_data = b_11_2_6_13.get()
    b_11_2_6_14_data = b_11_2_6_14.get()
    b_11_2_6_15_data = b_11_2_6_15.get()
    b_11_2_6_16_data = b_11_2_6_16.get()
    b_11_2_6_17_data = b_11_2_6_17.get()
    b_11_2_6_18_data = b_11_2_6_18.get()
    b_11_2_6_19_data = b_11_2_6_19.get()
    b_11_2_6_20_data = b_11_2_6_20.get()
    b_11_2_6_21_data = b_11_2_6_21.get()
    b_11_2_6_22_data = b_11_2_6_22.get()
    b_11_2_6_23_data = b_11_2_6_23.get()
    list = [float(b_11_2_6_1_data), float(b_11_2_6_2_data), float(b_11_2_6_3_data), float(b_11_2_6_4_data), float(b_11_2_6_5_data), float(b_11_2_6_6_data), float(b_11_2_6_7_data), float(b_11_2_6_8_data), float(b_11_2_6_9_data), float(b_11_2_6_10_data), float(b_11_2_6_11_data), float(b_11_2_6_12_data), float(b_11_2_6_13_data), float(b_11_2_6_14_data), float(b_11_2_6_15_data), float(b_11_2_6_16_data), float(b_11_2_6_17_data), float(b_11_2_6_18_data), float(b_11_2_6_19_data), float(b_11_2_6_20_data), float(b_11_2_6_21_data), float(b_11_2_6_22_data), float(b_11_2_6_23_data)]
    calculation_result = sum(list)
    result = str(calculation_result)
    b_11_2_8.insert(0, result)

def b_12_clicked():
    b_12_1_firstdata.place(x=312, y=52)
    b_12_1_firstdata_text1.place(x=197, y=52)
    b_12_1_firstdata_text2.place(x=515, y=52)

    b_12_1_seconddata.place(x=312, y=92)
    b_12_1_seconddata_text1.place(x=195, y=92)
    b_12_1_seconddata_text2.place(x=515, y=92)

    b_12_1_thirddata.place(x=312, y=126)
    b_12_1_thirddata_text.place(x=181, y=126)

    b_12_2_firstdata.place(x=312, y=166)
    b_12_2_firstdata_text1.place(x=179, y=166)
    b_12_2_firstdata_text2.place(x=515, y=166)

    b_12_2_seconddata.place(x=312, y=206)
    b_12_2_seconddata_text1.place(x=195, y=206)
    b_12_2_seconddata_text2.place(x=515, y=206)

    b_12_3_firstdata.place(x=312, y=246)
    b_12_3_firstdata_text1.place(x=197, y=246)
    b_12_3_firstdata_text2.place(x=515, y=246)

    b_12_3_seconddata.place(x=312, y=286)
    b_12_3_seconddata_text1.place(x=246, y=286)
    b_12_3_seconddata_text2.place(x=515, y=286)

    b_12_3_thirddata.place(x=312, y=326)
    b_12_3_thirddata_text1.place(x=246, y=326)
    b_12_3_thirddata_text2.place(x=515, y=326)

    b_12_3_fourthdata.place(x=312, y=366)
    b_12_3_fourthdata_text1.place(x=140, y=366)
    b_12_3_fourthdata_text2.place(x=515, y=366)

    b_12_4_1_text1.place(x=802, y=52)

    b_12_4_1_text2.place(x=872, y=52)
    
    b_12_4_1_text3.place(x=955, y=52)

    b_12_4_2_text1.place(x=650, y=72)

    b_12_4_2_text2.place(x=650, y=93)

    b_12_4_2_text3.place(x=650, y=114)
    
    b_12_4_1.place(x=770, y=72)

    b_12_4_2.place(x=845, y=72)

    b_12_4_3.place(x=919, y=72)

    b_12_4_4.place(x=919, y=94)

    b_12_4_5.place(x=919, y=116)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  
    
    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()
    
    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()

    b_11_1_1_10.place_forget()

    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()
    
    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_13_1_text.place_forget()
    
    b_13_1_1.place_forget()
    
    b_13_1_2.place_forget()
    
    b_13_1_3.place_forget()
    
    b_13_1_4.place_forget()
    
    b_13_2_1.place_forget()
    
    b_13_2_2.place_forget()
    
    b_13_2_3.place_forget()
    
    b_13_2_4.place_forget()
    
    b_13_3.place_forget()
    b_13_3_text1.place_forget()
    b_13_3_text2.place_forget()
    
    b_13_4_text.place_forget()
    
    b_13_4_1.place_forget()
    b_13_4_1_text.place_forget()
    
    b_13_4_2.place_forget()
    b_13_4_2_text.place_forget()
    
    b_13_4_3.place_forget()
    b_13_4_3_text.place_forget()
    
    b_13_4_4.place_forget()
    b_13_4_4_text.place_forget()
    
    b_13_4_5.place_forget()
    b_13_4_5_text.place_forget()
    
    b_13_4_6.place_forget()
    b_13_4_6_text.place_forget()
    
    b_13_4_7.place_forget()
    b_13_4_7_text.place_forget()
    
    b_13_4_8.place_forget()
    b_13_4_8_text.place_forget()
    
    b_13_5_1.place_forget()
    
    b_13_5_2.place_forget()
    
    b_13_5_3.place_forget()
    
    b_13_5_4.place_forget()
    
    b_13_5_5.place_forget()
    
    b_13_5_6.place_forget()
    
    b_13_5_7.place_forget()
    
    b_13_5_8.place_forget()
    
    b_13_5_9.place_forget()
    
    b_13_5_10.place_forget()
    
    b_13_5_11.place_forget()
    
    b_13_5_12.place_forget()
    
    b_13_5_13.place_forget()
    
    b_13_5_14.place_forget()
    
    b_13_5_15.place_forget()
    
    b_13_5_16.place_forget()

    b_13_6_1.place_forget()

    b_13_6_2.place_forget()
    
    b_13_6_3.place_forget()
    
    b_13_6_4.place_forget()

def b_12_2_1_logic(event):
    b_12_1_firstdata_data = b_12_1_firstdata.get()
    b_12_1_seconddata_data = b_12_1_seconddata.get()
    b_12_1_thirddata_data = b_12_1_thirddata.get()
    calculation_result = float(b_12_1_firstdata_data) / (3600 * float(b_12_1_seconddata_data) * float(b_12_1_thirddata_data))
    result = str(calculation_result)
    b_12_2_firstdata.insert(0, result)

def b_12_3_1_logic(event):
    b_12_2_firstdata_data = b_12_2_firstdata.get()
    b_12_2_seconddata_data = b_12_2_seconddata.get()
    calculation_result = 1000 * 1000 * float(b_12_2_firstdata_data) / float(b_12_2_seconddata_data)
    result = str(calculation_result)
    b_12_3_firstdata.insert(0, result)

def b_12_3_4_logic(event):
    b_12_1_firstdata_data = b_12_1_firstdata.get()
    b_12_1_thirddata_data = b_12_1_thirddata.get()
    b_12_3_seconddata_data = b_12_3_seconddata.get()
    b_12_3_thirddata_data = b_12_3_thirddata.get()
    calculation_result = float(b_12_1_firstdata_data) / (3600 * float(b_12_1_thirddata_data) * (float(b_12_3_seconddata_data) / 1000) * (float(b_12_3_thirddata_data) / 1000))
    result = str(calculation_result)
    b_12_3_fourthdata.insert(0, result)

def b_12_4_3_logic(event):
    b_12_4_1_data = b_12_4_1.get()
    b_12_4_2_data = b_12_4_2.get()
    calculation_result = (float(b_12_4_1_data) * float(b_12_4_2_data)) / (10 ** 6)
    result = str(calculation_result)
    b_12_4_3.insert(0, result)

def b_12_4_5_logic(event):
    b_12_4_3_data = b_12_4_3.get()
    b_12_4_4_data = b_12_4_4.get()
    calculation_result = float(b_12_4_4_data) / float(b_12_4_3_data)
    result = str(calculation_result)
    b_12_4_5.insert(0, result)

def b_13_clicked():
    b_13_1_text.place(x=380, y=52)

    b_13_1_1.place(x=300, y=72)

    b_13_1_2.place(x=300, y=92)

    b_13_1_3.place(x=300, y=112)

    b_13_1_4.place(x=300, y=132)

    b_13_2_1.place(x=300, y=152)

    b_13_2_2.place(x=300, y=172)

    b_13_2_3.place(x=300, y=192)

    b_13_2_4.place(x=300, y=212)

    b_13_3.place(x=300, y=232)
    b_13_3_text1.place(x=255, y=232)
    b_13_3_text2.place(x=497, y=232)

    b_13_4_text.place(x=648, y=52)

    b_13_4_1.place(x=600, y=72)
    b_13_4_1_text.place(x=798, y=71)

    b_13_4_2.place(x=600, y=92)
    b_13_4_2_text.place(x=798, y=91)

    b_13_4_3.place(x=600, y=112)
    b_13_4_3_text.place(x=798, y=112)

    b_13_4_4.place(x=600, y=132)
    b_13_4_4_text.place(x=798, y=132)

    b_13_4_5.place(x=600, y=152)
    b_13_4_5_text.place(x=798, y=152)

    b_13_4_6.place(x=600, y=172)
    b_13_4_6_text.place(x=798, y=172)

    b_13_4_7.place(x=600, y=192)
    b_13_4_7_text.place(x=798, y=192)

    b_13_4_8.place(x=600, y=212)
    b_13_4_8_text.place(x=798, y=212)

    b_13_5_1.place(x=900, y=52)

    b_13_5_2.place(x=900, y=72)

    b_13_5_3.place(x=900, y=92)

    b_13_5_4.place(x=900, y=112)

    b_13_5_5.place(x=900, y=132)
    
    b_13_5_6.place(x=900, y=152)
    
    b_13_5_7.place(x=900, y=172)
    
    b_13_5_8.place(x=900, y=192)
    
    b_13_5_9.place(x=900, y=212)
    
    b_13_5_10.place(x=900, y=232)
    
    b_13_5_11.place(x=900, y=252)
    
    b_13_5_12.place(x=900, y=272)
    
    b_13_5_13.place(x=900, y=292)
    
    b_13_5_14.place(x=900, y=312)
    
    b_13_5_15.place(x=900, y=332)
    
    b_13_5_16.place(x=900, y=352)

    b_13_6_1.place(x=600, y=232)

    b_13_6_2.place(x=600, y=252)
    
    b_13_6_3.place(x=600, y=272)
    
    b_13_6_4.place(x=600, y=292)

    b_2_1_firstdata.place_forget()
    b_2_1_firstdata_text1.place_forget()
    b_2_1_firstdata_text2.place_forget()

    b_2_1_seconddata.place_forget()
    b_2_1_seconddata_text1.place_forget()
    b_2_1_seconddata_text2.place_forget()

    b_2_1_thirddata.place_forget()
    b_2_1_thirddata_text1.place_forget()
    b_2_1_thirddata_text2.place_forget()

    b_2_1_fourthdata.place_forget()
    b_2_1_fourthdata_text1.place_forget()
    b_2_1_fourthdata_text2.place_forget()

    b_2_1_fifthdata.place_forget()
    b_2_1_fifthdata_text1.place_forget()
    b_2_1_fifthdata_text2.place_forget()

    b_2_2_text1.place_forget()

    b_2_2_text2.place_forget()   

    b_2_2_firstdata.place_forget()
    b_2_2_firstdata_text1.place_forget()
    b_2_2_firstdata_text2.place_forget()

    b_2_2_seconddata.place_forget()
    b_2_2_seconddata_text1.place_forget()
    b_2_2_seconddata_text2.place_forget()

    b_2_3_text.place_forget()

    b_2_3_firstdata.place_forget()
    b_2_3_firstdata_text1.place_forget()
    b_2_3_firstdata_text2.place_forget()

    b_2_3_seconddata.place_forget()
    b_2_3_seconddata_text1.place_forget()
    b_2_3_seconddata_text2.place_forget()

    b_2_4_text.place_forget()

    b_2_4_firstdata.place_forget()
    b_2_4_firstdata_text1.place_forget()
    b_2_4_firstdata_text2.place_forget()

    b_2_4_seconddata.place_forget()
    b_2_4_seconddata_text1.place_forget()
    b_2_4_seconddata_text2.place_forget()      

    b_2_4_thirddata.place_forget() 
    b_2_4_thirddata_text1.place_forget()
    b_2_4_thirddata_text2.place_forget()

    b_2_5_text.place_forget()

    b_2_5_firstdata.place_forget()
    b_2_5_firstdata_text1.place_forget()
    b_2_5_firstdata_text2.place_forget()

    b_2_5_seconddata.place_forget()
    b_2_5_seconddata_text1.place_forget()
    b_2_5_seconddata_text2.place_forget()  
    
    b_3_firstdata.place_forget()
    b_3_firstdata_text1.place_forget()
    b_3_firstdata_text2.place_forget()

    b_3_seconddata.place_forget()
    b_3_seconddata_text1.place_forget()
    b_3_seconddata_text2.place_forget()

    b_3_thirddata.place_forget()
    b_3_thirddata_text1.place_forget()
    b_3_thirddata_text2.place_forget() 

    b_4_firstdata.place_forget()
    b_4_firstdata_text1.place_forget()
    b_4_firstdata_text2.place_forget()

    b_4_seconddata.place_forget()
    b_4_seconddata_text1.place_forget()
    b_4_seconddata_text2.place_forget()

    b_4_thirddata.place_forget()
    b_4_thirddata_text1.place_forget()
    b_4_thirddata_text2.place_forget()

    b_4_fourthdata.place_forget()
    b_4_fourthdata_text1.place_forget()
    b_4_fourthdata_text2.place_forget()

    b_4_fifthdata.place_forget()
    b_4_fifthdata_text1.place_forget()
    b_4_fifthdata_text2.place_forget()

    b_4_data_table_text.place_forget()

    b_4_data_table.place_forget()

    b_5_1_firstdata.place_forget()
    b_5_1_firstdata_text1.place_forget()
    b_5_1_firstdata_text2.place_forget()

    b_5_1_seconddata.place_forget()
    b_5_1_seconddata_text1.place_forget()
    b_5_1_seconddata_text2.place_forget()

    b_5_1_thirddata.place_forget()
    b_5_1_thirddata_text1.place_forget()
    b_5_1_thirddata_text2.place_forget()

    b_5_2_firstdata.place_forget()
    b_5_2_firstdata_text1.place_forget()
    b_5_2_firstdata_text2.place_forget()

    b_5_2_seconddata.place_forget()
    b_5_2_seconddata_text1.place_forget()
    b_5_2_seconddata_text2.place_forget()

    b_5_2_thirddata.place_forget()
    b_5_2_thirddata_text1.place_forget()
    b_5_2_thirddata_text2.place_forget()

    b_5_2_fourthdata.place_forget()
    b_5_2_fourthdata_text1.place_forget()
    b_5_2_fourthdata_text2.place_forget()

    b_5_3_firstdata.place_forget()
    b_5_3_firstdata_text1.place_forget()
    b_5_3_firstdata_text2.place_forget()

    b_5_3_seconddata.place_forget()
    b_5_3_seconddata_text1.place_forget()
    b_5_3_seconddata_text2.place_forget()

    b_5_3_thirddata.place_forget()
    b_5_3_thirddata_text1.place_forget()
    b_5_3_thirddata_text2.place_forget()

    b_6_1_firstdata.place_forget()    
    b_6_1_firstdata_text1.place_forget()
    b_6_1_firstdata_text2.place_forget()

    b_6_1_seconddata.place_forget()
    b_6_1_seconddata_text1.place_forget()
    b_6_1_seconddata_text2.place_forget()

    b_6_1_thirddata.place_forget()
    b_6_1_thirddata_text1.place_forget()
    b_6_1_thirddata_text2.place_forget()

    b_6_2_firstdata.place_forget()
    b_6_2_firstdata_text1.place_forget()
    b_6_2_firstdata_text2.place_forget()

    b_6_2_seconddata.place_forget()
    b_6_2_seconddata_text1.place_forget()
    b_6_2_seconddata_text2.place_forget()

    b_6_2_thirddata.place_forget()
    b_6_2_thirddata_text1.place_forget()
    b_6_2_thirddata_text2.place_forget()

    b_6_3_firstdata.place_forget()
    b_6_3_firstdata_text1.place_forget()
    b_6_3_firstdata_text2.place_forget()

    b_6_3_seconddata.place_forget()
    b_6_3_seconddata_text1.place_forget()
    b_6_3_seconddata_text2.place_forget()

    b_6_3_thirddata.place_forget()
    b_6_3_thirddata_text1.place_forget()
    b_6_3_thirddata_text2.place_forget()

    b_7_1_text.place_forget()

    b_7_1_1_1_text.place_forget()
    
    b_7_1_2_1_text.place_forget()

    b_7_1_3_1_text.place_forget()

    b_7_1_4_1_text.place_forget()

    b_7_1_5_1_text.place_forget()

    b_7_1_1_2_text.place_forget()

    b_7_1_2_2_text.place_forget()

    b_7_1_3_2_text.place_forget()

    b_7_1_1.place_forget()

    b_7_1_2.place_forget()

    b_7_1_3.place_forget()

    b_7_1_4.place_forget()

    b_7_1_5.place_forget()

    b_7_1_6.place_forget()

    b_7_1_7.place_forget()

    b_7_1_8.place_forget()

    b_7_1_9.place_forget()

    b_7_1_10.place_forget()

    b_7_1_11.place_forget()

    b_7_1_12.place_forget()

    b_7_1_13.place_forget()

    b_7_1_14.place_forget()

    b_7_1_15.place_forget()

    b_7_2_text.place_forget()

    b_7_2_1_1_text.place_forget()
    
    b_7_2_2_1_text.place_forget()

    b_7_2_3_1_text.place_forget()

    b_7_2_4_1_text.place_forget()

    b_7_2_5_1_text.place_forget()

    b_7_2_1_2_text.place_forget()

    b_7_2_2_2_text.place_forget()

    b_7_2_3_2_text.place_forget()

    b_7_2_1.place_forget()

    b_7_2_2.place_forget()

    b_7_2_3.place_forget()

    b_7_2_4.place_forget()

    b_7_2_5.place_forget()

    b_7_2_6.place_forget()

    b_7_2_7.place_forget()

    b_7_2_8.place_forget()

    b_7_2_9.place_forget()

    b_7_2_10.place_forget()

    b_7_2_11.place_forget()

    b_7_2_12.place_forget()

    b_7_2_13.place_forget()

    b_7_2_14.place_forget()

    b_7_2_15.place_forget()

    b_7_3_text.place_forget()

    b_7_3_1_1_text.place_forget()
    
    b_7_3_2_1_text.place_forget()

    b_7_3_3_1_text.place_forget()

    b_7_3_4_1_text.place_forget()

    b_7_3_5_1_text.place_forget()

    b_7_3_1_2_text.place_forget()

    b_7_3_2_2_text.place_forget()

    b_7_3_3_2_text.place_forget()

    b_7_3_1.place_forget()

    b_7_3_2.place_forget()

    b_7_3_3.place_forget()

    b_7_3_4.place_forget()

    b_7_3_5.place_forget()

    b_7_3_6.place_forget()

    b_7_3_7.place_forget()

    b_7_3_8.place_forget()

    b_7_3_9.place_forget()

    b_7_3_10.place_forget()

    b_7_3_11.place_forget()

    b_7_3_12.place_forget()

    b_7_3_13.place_forget()

    b_7_3_14.place_forget()

    b_7_3_15.place_forget()

    b_7_4_text.place_forget()

    b_7_4_1_1_text.place_forget()
    
    b_7_4_2_1_text.place_forget()

    b_7_4_3_1_text.place_forget()

    b_7_4_4_1_text.place_forget()

    b_7_4_5_1_text.place_forget()

    b_7_4_6_1_text.place_forget()

    b_7_4_7_1_text.place_forget()

    b_7_4_1_2_text.place_forget()

    b_7_4_2_2_text.place_forget()

    b_7_4_3_2_text.place_forget()

    b_7_4_1.place_forget()

    b_7_4_2.place_forget()

    b_7_4_3.place_forget()

    b_7_4_4.place_forget()

    b_7_4_5.place_forget()

    b_7_4_6.place_forget()

    b_7_4_7.place_forget()

    b_7_4_8.place_forget()

    b_7_4_9.place_forget()

    b_7_4_10.place_forget()

    b_7_4_11.place_forget()

    b_7_4_12.place_forget()

    b_7_4_13.place_forget()

    b_7_4_14.place_forget()

    b_7_4_15.place_forget()

    b_7_4_16.place_forget()

    b_7_4_17.place_forget()

    b_7_4_18.place_forget()

    b_7_4_19.place_forget()

    b_7_4_20.place_forget()

    b_7_4_21.place_forget()

    b_7_5_text.place_forget()

    b_7_5_1_1_text.place_forget()
    
    b_7_5_2_1_text.place_forget()

    b_7_5_3_1_text.place_forget()

    b_7_5_4_1_text.place_forget()

    b_7_5_5_1_text.place_forget()

    b_7_5_6_1_text.place_forget()

    b_7_5_7_1_text.place_forget()

    b_7_5_1_2_text.place_forget()

    b_7_5_2_2_text.place_forget()

    b_7_5_3_2_text.place_forget()

    b_7_5_1.place_forget()

    b_7_5_2.place_forget()

    b_7_5_3.place_forget()

    b_7_5_4.place_forget()

    b_7_5_5.place_forget()

    b_7_5_6.place_forget()

    b_7_5_7.place_forget()

    b_7_5_8.place_forget()

    b_7_5_9.place_forget()

    b_7_5_10.place_forget()

    b_7_5_11.place_forget()

    b_7_5_12.place_forget()

    b_7_5_13.place_forget()

    b_7_5_14.place_forget()

    b_7_5_15.place_forget()

    b_7_5_16.place_forget()

    b_7_5_17.place_forget()

    b_7_5_18.place_forget()

    b_7_5_19.place_forget()

    b_7_5_20.place_forget()

    b_7_5_21.place_forget()
    
    b_7_6_text.place_forget()

    b_7_6_1_1_text.place_forget()
    
    b_7_6_2_1_text.place_forget()

    b_7_6_3_1_text.place_forget()

    b_7_6_4_1_text.place_forget()

    b_7_6_5_1_text.place_forget()

    b_7_6_6_1_text.place_forget()

    b_7_6_7_1_text.place_forget()

    b_7_6_1_2_text.place_forget()

    b_7_6_2_2_text.place_forget()

    b_7_6_3_2_text.place_forget()

    b_7_6_1.place_forget()

    b_7_6_2.place_forget()

    b_7_6_3.place_forget()

    b_7_6_4.place_forget()

    b_7_6_5.place_forget()

    b_7_6_6.place_forget()

    b_7_6_7.place_forget()

    b_7_6_8.place_forget()

    b_7_6_9.place_forget()

    b_7_6_10.place_forget()

    b_7_6_11.place_forget()

    b_7_6_12.place_forget()

    b_7_6_13.place_forget()

    b_7_6_14.place_forget()

    b_7_6_15.place_forget()

    b_7_6_16.place_forget()

    b_7_6_17.place_forget()

    b_7_6_18.place_forget()

    b_7_6_19.place_forget()

    b_7_6_20.place_forget()

    b_7_6_21.place_forget()

    b_8_text1.place_forget()
    
    b_8_text2.place_forget()
    
    b_8_text3.place_forget()
    
    b_8_1_1.place_forget()
    
    b_8_1_2.place_forget()
    
    b_8_1_3.place_forget()
    
    b_8_1_4.place_forget()
    
    b_8_1_5.place_forget()
    
    b_8_1_6.place_forget()
    
    b_8_1_7.place_forget()
    
    b_8_1_8.place_forget()
    
    b_8_1_9.place_forget()
    
    b_8_1_10.place_forget()
    
    b_8_1_11.place_forget()
    
    b_8_1_12.place_forget()
    
    b_8_2_1.place_forget()
    
    b_8_2_2.place_forget()
    
    b_8_2_3.place_forget()
    
    b_8_2_4.place_forget()
    
    b_8_2_5.place_forget()
    
    b_8_2_6.place_forget()
    
    b_8_2_7.place_forget()
    
    b_8_2_8.place_forget()
    
    b_8_2_9.place_forget()
    
    b_8_2_10.place_forget()
    
    b_8_2_11.place_forget()
    
    b_8_2_12.place_forget()
    
    b_8_3_1.place_forget()
    
    b_8_3_2.place_forget()
    
    b_8_3_3.place_forget()
    
    b_8_3_4.place_forget()
    
    b_8_3_5.place_forget()
    
    b_8_3_6.place_forget()
    
    b_8_3_7.place_forget()
    
    b_8_3_8.place_forget()
    
    b_8_3_9.place_forget()
    
    b_8_3_10.place_forget()
    
    b_8_3_11.place_forget()
    
    b_8_3_12.place_forget()

    b_8_firstdata.place_forget()
    b_8_firstdata_text1.place_forget()
    b_8_firstdata_text2.place_forget()

    b_8_seconddata.place_forget()
    b_8_seconddata_text1.place_forget()
    b_8_seconddata_text2.place_forget()

    b_8_thirddata.place_forget()
    b_8_thirddata_text1.place_forget()
    
    b_8_thirddata_text2.place_forget()

    b_9_1_text.place_forget()
    
    b_9_2_text.place_forget()

    b_9_3_text.place_forget()
    
    b_9_4_text.place_forget()
    
    b_9_5_text.place_forget()
    
    b_9_text1.place_forget()
    
    b_9_1_1.place_forget()
    
    b_9_1_2.place_forget()
    
    b_9_1_3.place_forget()
    
    b_9_1_4.place_forget()
    
    b_9_1_5.place_forget()
    
    b_9_1_6.place_forget()
    
    b_9_1_7.place_forget()
    
    b_9_2_1.place_forget()
    
    b_9_2_2.place_forget()
    
    b_9_2_3.place_forget()
    
    b_9_2_4.place_forget()
    
    b_9_2_5.place_forget()
    
    b_9_2_6.place_forget()
    
    b_9_2_7.place_forget()
    
    b_9_3_1.place_forget()
    
    b_9_3_2.place_forget()
    
    b_9_3_3.place_forget()
    
    b_9_3_4.place_forget()
    
    b_9_3_5.place_forget()
    
    b_9_3_6.place_forget()

    b_9_3_7.place_forget()
    
    b_9_4_1.place_forget()
    
    b_9_4_2.place_forget()
    
    b_9_4_3.place_forget()
    
    b_9_4_4.place_forget()
    
    b_9_4_5.place_forget()
    
    b_9_4_6.place_forget()
    
    b_9_4_7.place_forget()
    
    b_9_5_1.place_forget()
    
    b_9_5_2.place_forget()
    
    b_9_5_3.place_forget()
    
    b_9_5_4.place_forget()
    
    b_9_5_5.place_forget()
    
    b_9_5_6.place_forget()
    
    b_9_5_7.place_forget()
    
    b_9_text2.place_forget()

    b_9_1_8.place_forget()
    
    b_9_1_9.place_forget()
    
    b_9_1_10.place_forget()
    
    b_9_1_11.place_forget()
    
    b_9_1_12.place_forget()
    
    b_9_1_13.place_forget()
    
    b_9_1_14.place_forget()
    
    b_9_1_15.place_forget()
    
    b_9_1_16.place_forget()
    
    b_9_1_17.place_forget()
    
    b_9_1_18.place_forget()
    
    b_9_1_19.place_forget()
    
    b_9_1_20.place_forget()
    
    b_9_1_21.place_forget()
    
    b_9_2_8.place_forget()
    
    b_9_2_9.place_forget()
    
    b_9_2_10.place_forget()
    
    b_9_2_11.place_forget()
    
    b_9_2_12.place_forget()
    
    b_9_2_13.place_forget()
    
    b_9_2_14.place_forget()
    
    b_9_2_15.place_forget()
    
    b_9_2_16.place_forget()
    
    b_9_2_17.place_forget()
    
    b_9_2_18.place_forget()
    
    b_9_2_19.place_forget()
    
    b_9_2_20.place_forget()
    
    b_9_2_21.place_forget()
    
    b_9_3_8.place_forget()
    
    b_9_3_9.place_forget()
    
    b_9_3_10.place_forget()
    
    b_9_3_11.place_forget()
    
    b_9_3_12.place_forget()
    
    b_9_3_13.place_forget()
    
    b_9_3_14.place_forget()
    
    b_9_3_15.place_forget()
    
    b_9_3_16.place_forget()
    
    b_9_3_17.place_forget()
    
    b_9_3_18.place_forget()
    
    b_9_3_19.place_forget()
    
    b_9_3_20.place_forget()
    
    b_9_3_21.place_forget()
    
    b_9_4_8.place_forget()
    
    b_9_4_9.place_forget()

    b_9_4_10.place_forget()
    
    b_9_4_11.place_forget()
    
    b_9_4_12.place_forget()
    
    b_9_4_13.place_forget()
    
    b_9_4_14.place_forget()
    
    b_9_4_15.place_forget()
    
    b_9_4_16.place_forget()
    
    b_9_4_17.place_forget()
    
    b_9_4_18.place_forget()
    
    b_9_4_19.place_forget()
    
    b_9_4_20.place_forget()
    
    b_9_4_21.place_forget()

    b_9_5_8.place_forget()
    
    b_9_5_9.place_forget()
    
    b_9_5_10.place_forget()

    b_9_5_11.place_forget()
    
    b_9_5_12.place_forget()
    
    b_9_5_13.place_forget()
    
    b_9_5_14.place_forget()
    
    b_9_5_15.place_forget()
    
    b_9_5_16.place_forget()
    
    b_9_5_17.place_forget()
    
    b_9_5_18.place_forget()
    
    b_9_5_19.place_forget()
    
    b_9_5_20.place_forget()
    
    b_9_5_21.place_forget()
    
    b_9_text3.place_forget()

    b_9_1_22.place_forget()
    
    b_9_1_23.place_forget()
    
    b_9_1_24.place_forget()
    
    b_9_1_25.place_forget()
    
    b_9_1_26.place_forget()
    
    b_9_1_27.place_forget()
    
    b_9_1_28.place_forget()
    
    b_9_1_29.place_forget()
    
    b_9_1_30.place_forget()
    
    b_9_3_22.place_forget()
    
    b_9_3_23.place_forget()

    b_9_3_24.place_forget()
    
    b_9_3_25.place_forget()
    
    b_9_3_26.place_forget()
    
    b_9_3_27.place_forget()
    
    b_9_3_28.place_forget()
    
    b_9_3_29.place_forget()
    
    b_9_3_30.place_forget()
    
    b_9_4_22.place_forget()
    
    b_9_4_23.place_forget()
    
    b_9_4_24.place_forget()
    
    b_9_4_25.place_forget()
    
    b_9_4_26.place_forget()
    
    b_9_4_27.place_forget()
    
    b_9_4_28.place_forget()
    
    b_9_4_29.place_forget()
    
    b_9_4_30.place_forget()
    
    b_9_5_22.place_forget()
    
    b_9_5_23.place_forget()
    
    b_9_5_24.place_forget()
    
    b_9_5_25.place_forget()
    
    b_9_5_26.place_forget()
    
    b_9_5_27.place_forget()
    
    b_9_5_28.place_forget()
    
    b_9_5_29.place_forget()
    
    b_9_5_30.place_forget()
    
    b_9_text4.place_forget()

    b_9_1_31.place_forget()
    
    b_9_1_32.place_forget()
    
    b_9_1_33.place_forget()
    
    b_9_1_34.place_forget()
    
    b_9_1_35.place_forget()
    
    b_9_1_36.place_forget()
    
    b_9_1_37.place_forget()
    
    b_9_2_31.place_forget()
    
    b_9_2_32.place_forget()
    
    b_9_2_33.place_forget()
    
    b_9_2_34.place_forget()
    
    b_9_2_35.place_forget()
    
    b_9_2_36.place_forget()
    
    b_9_2_37.place_forget()
    
    b_9_3_31.place_forget()
    
    b_9_3_32.place_forget()
    
    b_9_3_33.place_forget()
    
    b_9_3_34.place_forget()
    
    b_9_3_35.place_forget()
    
    b_9_3_36.place_forget()
    
    b_9_3_37.place_forget()
    
    b_9_4_31.place_forget()
    
    b_9_4_32.place_forget()
    
    b_9_4_33.place_forget()
    
    b_9_4_34.place_forget()
    
    b_9_4_35.place_forget()
    
    b_9_4_36.place_forget()
    
    b_9_4_37.place_forget()
    
    b_9_5_31.place_forget()
    
    b_9_5_32.place_forget()
    
    b_9_5_33.place_forget()
    
    b_9_5_34.place_forget()
    
    b_9_5_35.place_forget()
    
    b_9_5_36.place_forget()
    
    b_9_5_37.place_forget()
    
    b_9_text5.place_forget()

    b_9_1_38.place_forget()
    
    b_9_1_39.place_forget()

    b_9_1_40.place_forget()
    
    b_9_1_41.place_forget()
    
    b_9_1_42.place_forget()
    
    b_9_1_43.place_forget()
    
    b_9_1_44.place_forget()
    
    b_9_2_38.place_forget()
    
    b_9_2_39.place_forget()
    
    b_9_2_40.place_forget()
    
    b_9_2_41.place_forget()
    
    b_9_2_42.place_forget()
    
    b_9_2_43.place_forget()
    
    b_9_2_44.place_forget()
    
    b_9_3_38.place_forget()
    
    b_9_3_39.place_forget()
    
    b_9_3_40.place_forget()
    
    b_9_3_41.place_forget()
    
    b_9_3_42.place_forget()
    
    b_9_3_43.place_forget()
    
    b_9_3_44.place_forget()
    
    b_9_4_38.place_forget()
    
    b_9_4_39.place_forget()
    
    b_9_4_40.place_forget()
    
    b_9_4_41.place_forget()
    
    b_9_4_42.place_forget()
    
    b_9_4_43.place_forget()
    
    b_9_4_44.place_forget()
    
    b_9_5_38.place_forget()
    
    b_9_5_39.place_forget()
    
    b_9_5_40.place_forget()
    
    b_9_5_41.place_forget()
    
    b_9_5_42.place_forget()
    
    b_9_5_43.place_forget()
    
    b_9_5_44.place_forget()
    
    b_9_6.place_forget()

    b_9_6_text1.place_forget()
    
    b_9_6_text2.place_forget()
    
    b_9_7_text1.place_forget()
    
    b_9_7_text2.place_forget()
    
    b_9_7_text3.place_forget()
    
    b_9_7_1_1.place_forget()
    
    b_9_7_1_2.place_forget()
    
    b_9_7_1_3.place_forget()
    
    b_9_7_1_4.place_forget()
    
    b_9_7_1_5.place_forget()
    
    b_9_7_1_6.place_forget()
    
    b_9_7_1_7.place_forget()
    
    b_9_7_1_8.place_forget()
    
    b_9_7_1_9.place_forget()
    
    b_9_7_1_10.place_forget()
    
    b_9_7_1_11.place_forget()
    
    b_9_7_1_12.place_forget()
    
    b_9_7_1_13.place_forget()
    
    b_9_7_1_14.place_forget()
    
    b_9_7_1_15.place_forget()
    
    b_9_7_1_16.place_forget()
    
    b_9_7_1_17.place_forget()
    
    b_9_7_1_18.place_forget()
    
    b_9_7_1_19.place_forget()
    
    b_9_7_1_20.place_forget()
    
    b_9_7_1_21.place_forget()
    
    b_9_7_2_1.place_forget()
    
    b_9_7_2_2.place_forget()
    
    b_9_7_2_3.place_forget()
    
    b_9_7_2_4.place_forget()
    
    b_9_7_2_5.place_forget()
    
    b_9_7_2_6.place_forget()
    
    b_9_7_2_7.place_forget()
    
    b_9_7_2_8.place_forget()
    
    b_9_7_2_9.place_forget()
    
    b_9_7_2_10.place_forget()
    
    b_9_7_2_11.place_forget()
    
    b_9_7_2_12.place_forget()
    
    b_9_7_2_13.place_forget()
    
    b_9_7_2_14.place_forget()
    
    b_9_7_2_15.place_forget()
    
    b_9_7_2_16.place_forget()
    
    b_9_7_2_17.place_forget()
    
    b_9_7_2_18.place_forget()
    
    b_9_7_2_19.place_forget()
    
    b_9_7_2_20.place_forget()
    
    b_9_7_2_21.place_forget()
    
    b_9_7_3_1.place_forget()
    
    b_9_7_3_2.place_forget()
    
    b_9_7_3_3.place_forget()
    
    b_9_7_3_4.place_forget()
    
    b_9_7_3_5.place_forget()
    
    b_9_7_3_6.place_forget()
    
    b_9_7_3_7.place_forget()
    
    b_9_7_3_8.place_forget()
    
    b_9_7_3_9.place_forget()
    
    b_9_7_3_10.place_forget()
    
    b_9_7_3_11.place_forget()
    
    b_9_7_3_12.place_forget()
    
    b_9_7_3_13.place_forget()
    
    b_9_7_3_14.place_forget()
    
    b_9_7_3_15.place_forget()
    
    b_9_7_3_16.place_forget()
    
    b_9_7_3_17.place_forget()
    
    b_9_7_3_18.place_forget()
    
    b_9_7_3_19.place_forget()
    
    b_9_7_3_20.place_forget()
    
    b_9_7_3_21.place_forget()

    b_9_8.place_forget()

    b_10_1_text.place_forget()

    b_10_2_text.place_forget()
    
    b_10_3_text.place_forget()
    
    b_10_4_text.place_forget()
    
    b_10_5_text.place_forget()
    
    b_10_1_1.place_forget()
    
    b_10_1_2.place_forget()
    
    b_10_1_3.place_forget()
    
    b_10_1_4.place_forget()
    
    b_10_1_5.place_forget()
    
    b_10_1_6.place_forget()
    
    b_10_2_1.place_forget()
    
    b_10_2_2.place_forget()
    
    b_10_2_3.place_forget()
    
    b_10_2_4.place_forget()
    
    b_10_2_5.place_forget()
    
    b_10_2_6.place_forget()
    
    b_10_2_7.place_forget()
    
    b_10_2_8.place_forget()
    
    b_10_2_9.place_forget()
    
    b_10_2_10.place_forget()
    
    b_10_2_11.place_forget()
    
    b_10_2_12.place_forget()
    
    b_10_2_13.place_forget()
    
    b_10_2_14.place_forget()
    
    b_10_2_15.place_forget()
    
    b_10_2_16.place_forget()
    
    b_10_2_17.place_forget()
    
    b_10_2_18.place_forget()
    
    b_10_2_19.place_forget()
    
    b_10_2_20.place_forget()
    
    b_10_2_21.place_forget()
    
    b_10_2_22.place_forget()
    
    b_10_2_23.place_forget()
    
    b_10_2_24.place_forget()
    
    b_10_2_25.place_forget()
    
    b_10_2_26.place_forget()
    
    b_10_2_27.place_forget()
    
    b_10_2_28.place_forget()
    
    b_10_3_1.place_forget()

    b_10_3_2.place_forget()
    
    b_10_3_3.place_forget()
    
    b_10_3_4.place_forget()
    
    b_10_3_5.place_forget()
    
    b_10_3_6.place_forget()
    
    b_10_3_7.place_forget()
    
    b_10_3_8.place_forget()
    
    b_10_3_9.place_forget()
    
    b_10_3_10.place_forget()
    
    b_10_3_11.place_forget()

    b_10_3_12.place_forget()
    
    b_10_3_13.place_forget()
    
    b_10_3_14.place_forget()
    
    b_10_3_15.place_forget()
    
    b_10_3_16.place_forget()
    
    b_10_3_17.place_forget()
    
    b_10_3_18.place_forget()
    
    b_10_3_19.place_forget()
    
    b_10_3_20.place_forget()
    
    b_10_3_21.place_forget()
    
    b_10_3_22.place_forget()
    
    b_10_3_23.place_forget()
    
    b_10_3_24.place_forget()
    
    b_10_3_25.place_forget()
    
    b_10_3_26.place_forget()
    
    b_10_3_27.place_forget()
    
    b_10_3_28.place_forget()
    
    b_10_4_1.place_forget()

    b_10_4_2.place_forget()
    
    b_10_4_3.place_forget()
    
    b_10_4_4.place_forget()
    
    b_10_4_5.place_forget()
    
    b_10_4_6.place_forget()
    
    b_10_4_7.place_forget()
    
    b_10_4_8.place_forget()
    
    b_10_4_9.place_forget()
    
    b_10_4_10.place_forget()

    b_10_4_11.place_forget()

    b_10_4_12.place_forget()

    b_10_4_13.place_forget()

    b_10_4_14.place_forget()

    b_10_4_15.place_forget()

    b_10_4_16.place_forget()

    b_10_4_17.place_forget()
    
    b_10_4_18.place_forget()
    
    b_10_4_19.place_forget()
    
    b_10_4_20.place_forget()
    
    b_10_4_21.place_forget()
    
    b_10_4_22.place_forget()
    
    b_10_4_23.place_forget()
    
    b_10_4_24.place_forget()
    
    b_10_4_25.place_forget()
    
    b_10_4_26.place_forget()
    
    b_10_4_27.place_forget()
    
    b_10_4_28.place_forget()
    
    b_10_5_1.place_forget()
    
    b_10_5_2.place_forget()
    
    b_10_5_3.place_forget()
    
    b_10_5_4.place_forget()
    
    b_10_5_5.place_forget()
    
    b_10_5_6.place_forget()
    
    b_10_5_7.place_forget()
    
    b_10_5_8.place_forget()
    
    b_10_5_9.place_forget()
    
    b_10_5_10.place_forget()
    
    b_10_5_11.place_forget()
    
    b_10_5_12.place_forget()
    
    b_10_5_13.place_forget()
    
    b_10_5_14.place_forget()
    
    b_10_5_15.place_forget()
    
    b_10_5_16.place_forget()
    
    b_10_5_17.place_forget()
    
    b_10_5_18.place_forget()
    
    b_10_5_19.place_forget()
    
    b_10_5_20.place_forget()
    
    b_10_5_21.place_forget()
    
    b_10_5_22.place_forget()
    
    b_10_5_23.place_forget()
    
    b_10_5_24.place_forget()
    
    b_10_5_25.place_forget()
    
    b_10_5_26.place_forget()
    
    b_10_5_27.place_forget()
    
    b_10_5_28.place_forget()
    
    b_10_6.place_forget()
    b_10_6_text.place_forget()

    b_11_1_text.place_forget()

    b_11_1_1_text.place_forget()
    
    b_11_1_2_text.place_forget()
    
    b_11_1_3_text.place_forget()
    
    b_11_1_1_1.place_forget()
    
    b_11_1_1_2.place_forget()
    
    b_11_1_1_3.place_forget()
    
    b_11_1_1_4.place_forget()
    
    b_11_1_1_5.place_forget()
    
    b_11_1_1_6.place_forget()
    
    b_11_1_1_7.place_forget()

    b_11_1_1_8.place_forget()

    b_11_1_1_9.place_forget()
    
    b_11_1_1_10.place_forget()

    b_11_1_2_1.place_forget()
    
    b_11_1_2_2.place_forget()
    
    b_11_1_2_3.place_forget()
    
    b_11_1_2_4.place_forget()
    
    b_11_1_2_5.place_forget()
    
    b_11_1_2_6.place_forget()
    
    b_11_1_2_7.place_forget()

    b_11_1_2_8.place_forget()

    b_11_1_2_9.place_forget()

    b_11_1_2_10.place_forget()

    b_11_1_3_1.place_forget()
    
    b_11_1_3_2.place_forget()
    
    b_11_1_3_3.place_forget()
    
    b_11_1_3_4.place_forget()
    
    b_11_1_3_5.place_forget()
    
    b_11_1_3_6.place_forget()
    
    b_11_1_3_7.place_forget()
    
    b_11_1_3_8.place_forget()

    b_11_1_3_9.place_forget()

    b_11_1_3_10.place_forget()

    b_11_1_4.place_forget()

    b_11_1_4_text.place_forget()
    
    b_11_2_text.place_forget()

    b_11_2_1_text.place_forget()

    b_11_2_2_text.place_forget()

    b_11_2_3_text.place_forget()

    b_11_2_4_text.place_forget()

    b_11_2_5_text.place_forget()

    b_11_2_6_text.place_forget()

    b_11_2_1_1.place_forget()

    b_11_2_1_2.place_forget()
    
    b_11_2_1_3.place_forget()
    
    b_11_2_1_4.place_forget()
    
    b_11_2_1_5.place_forget()
    
    b_11_2_1_6.place_forget()
    
    b_11_2_1_7.place_forget()
    
    b_11_2_1_8.place_forget()
    
    b_11_2_1_9.place_forget()
    
    b_11_2_1_10.place_forget()

    b_11_2_1_11.place_forget()
    
    b_11_2_1_12.place_forget()
    
    b_11_2_1_13.place_forget()
    
    b_11_2_1_14.place_forget()
    
    b_11_2_1_15.place_forget()
    
    b_11_2_1_16.place_forget()
    
    b_11_2_1_17.place_forget()
    
    b_11_2_1_18.place_forget()
    
    b_11_2_1_19.place_forget()
    
    b_11_2_1_20.place_forget()
    
    b_11_2_1_21.place_forget()
    
    b_11_2_1_22.place_forget()
    
    b_11_2_1_23.place_forget()
    
    b_11_2_2_1.place_forget()

    b_11_2_2_2.place_forget()
    
    b_11_2_2_3.place_forget()
    
    b_11_2_2_4.place_forget()
    
    b_11_2_2_5.place_forget()
    
    b_11_2_2_6.place_forget()
    
    b_11_2_2_7.place_forget()
    
    b_11_2_2_8.place_forget()
    
    b_11_2_2_9.place_forget()
    
    b_11_2_2_10.place_forget()
    
    b_11_2_2_11.place_forget()

    b_11_2_2_12.place_forget()
    
    b_11_2_2_13.place_forget()
    
    b_11_2_2_14.place_forget()
    
    b_11_2_2_15.place_forget()
    
    b_11_2_2_16.place_forget()
    
    b_11_2_2_17.place_forget()
    
    b_11_2_2_18.place_forget()
    
    b_11_2_2_19.place_forget()
    
    b_11_2_2_20.place_forget()
    
    b_11_2_2_21.place_forget()
    
    b_11_2_2_22.place_forget()
    
    b_11_2_2_23.place_forget()
    
    b_11_2_3_1.place_forget()
    
    b_11_2_3_2.place_forget()
    
    b_11_2_3_3.place_forget()
    
    b_11_2_3_4.place_forget()
    
    b_11_2_3_5.place_forget()
    
    b_11_2_3_6.place_forget()
    
    b_11_2_3_7.place_forget()
    
    b_11_2_3_8.place_forget()
    
    b_11_2_3_9.place_forget()
    
    b_11_2_3_10.place_forget()
    
    b_11_2_3_11.place_forget()
    
    b_11_2_3_12.place_forget()
    
    b_11_2_3_13.place_forget()
    
    b_11_2_3_14.place_forget()
    
    b_11_2_3_15.place_forget()
    
    b_11_2_3_16.place_forget()
    
    b_11_2_3_17.place_forget()
    
    b_11_2_3_18.place_forget()
    
    b_11_2_3_19.place_forget()
    
    b_11_2_3_20.place_forget()
    
    b_11_2_3_21.place_forget()
    
    b_11_2_3_22.place_forget()
    
    b_11_2_3_23.place_forget()
    
    b_11_2_4_1.place_forget()
    
    b_11_2_4_2.place_forget()
    
    b_11_2_4_3.place_forget()
    
    b_11_2_4_4.place_forget()
    
    b_11_2_4_5.place_forget()
    
    b_11_2_4_6.place_forget()
    
    b_11_2_4_7.place_forget()
    
    b_11_2_4_8.place_forget()
    
    b_11_2_4_9.place_forget()
    
    b_11_2_4_10.place_forget()
    
    b_11_2_4_11.place_forget()
    
    b_11_2_4_12.place_forget()
    
    b_11_2_4_13.place_forget()
    
    b_11_2_4_14.place_forget()
    
    b_11_2_4_15.place_forget()
    
    b_11_2_4_16.place_forget()
    
    b_11_2_4_17.place_forget()
    
    b_11_2_4_18.place_forget()
    
    b_11_2_4_19.place_forget()
    
    b_11_2_4_20.place_forget()
    
    b_11_2_4_21.place_forget()
    
    b_11_2_4_22.place_forget()
    
    b_11_2_4_23.place_forget()
    
    b_11_2_5_1.place_forget()
    
    b_11_2_5_2.place_forget()
    
    b_11_2_5_3.place_forget()
    
    b_11_2_5_4.place_forget()
    
    b_11_2_5_5.place_forget()
    
    b_11_2_5_6.place_forget()
    
    b_11_2_5_7.place_forget()
    
    b_11_2_5_8.place_forget()
    
    b_11_2_5_9.place_forget()
    
    b_11_2_5_10.place_forget()
    
    b_11_2_5_11.place_forget()
    
    b_11_2_5_12.place_forget()
    
    b_11_2_5_13.place_forget()
    
    b_11_2_5_14.place_forget()
    
    b_11_2_5_15.place_forget()
    
    b_11_2_5_16.place_forget()
    
    b_11_2_5_17.place_forget()
    
    b_11_2_5_18.place_forget()
    
    b_11_2_5_19.place_forget()
    
    b_11_2_5_20.place_forget()
    
    b_11_2_5_21.place_forget()
    
    b_11_2_5_22.place_forget()
    
    b_11_2_5_23.place_forget()
    
    b_11_2_6_1.place_forget()
    
    b_11_2_6_2.place_forget()
    
    b_11_2_6_3.place_forget()
    
    b_11_2_6_4.place_forget()
    
    b_11_2_6_5.place_forget()
    
    b_11_2_6_6.place_forget()
    
    b_11_2_6_7.place_forget()
    
    b_11_2_6_8.place_forget()
    
    b_11_2_6_9.place_forget()
    
    b_11_2_6_10.place_forget()
    
    b_11_2_6_11.place_forget()
    
    b_11_2_6_12.place_forget()
    
    b_11_2_6_13.place_forget()
    
    b_11_2_6_14.place_forget()
    
    b_11_2_6_15.place_forget()
    
    b_11_2_6_16.place_forget()
    
    b_11_2_6_17.place_forget()
    
    b_11_2_6_18.place_forget()
    
    b_11_2_6_19.place_forget()
    
    b_11_2_6_20.place_forget()
    
    b_11_2_6_21.place_forget()
    
    b_11_2_6_22.place_forget()
    
    b_11_2_6_23.place_forget()

    b_11_2_7.place_forget()
    b_11_2_7_text1.place_forget()
    b_11_2_7_text2.place_forget()

    b_11_2_8.place_forget()
    b_11_2_8_text.place_forget()

    b_12_1_firstdata.place_forget()
    b_12_1_firstdata_text1.place_forget()
    b_12_1_firstdata_text2.place_forget()

    b_12_1_seconddata.place_forget()
    b_12_1_seconddata_text1.place_forget()
    b_12_1_seconddata_text2.place_forget()

    b_12_1_thirddata.place_forget()
    b_12_1_thirddata_text.place_forget()

    b_12_2_firstdata.place_forget()
    b_12_2_firstdata_text1.place_forget()
    b_12_2_firstdata_text2.place_forget()

    b_12_2_seconddata.place_forget()
    b_12_2_seconddata_text1.place_forget()
    b_12_2_seconddata_text2.place_forget()

    b_12_3_firstdata.place_forget()
    b_12_3_firstdata_text1.place_forget()
    b_12_3_firstdata_text2.place_forget()

    b_12_3_seconddata.place_forget()
    b_12_3_seconddata_text1.place_forget()
    b_12_3_seconddata_text2.place_forget()

    b_12_3_thirddata.place_forget()
    b_12_3_thirddata_text1.place_forget()
    b_12_3_thirddata_text2.place_forget()

    b_12_3_fourthdata.place_forget()
    b_12_3_fourthdata_text1.place_forget()
    b_12_3_fourthdata_text2.place_forget()

    b_12_4_1_text1.place_forget()
    
    b_12_4_1_text2.place_forget()
    
    b_12_4_1_text3.place_forget()
    
    b_12_4_2_text1.place_forget()
    
    b_12_4_2_text2.place_forget()
    
    b_12_4_2_text3.place_forget()
    
    b_12_4_1.place_forget()
    
    b_12_4_2.place_forget()
    
    b_12_4_3.place_forget()
    
    b_12_4_4.place_forget()
    
    b_12_4_5.place_forget()

def b_13_5_1_logic(event):
    b_13_4_1_data = b_13_4_1.get()
    calculation_result = (621 + 165) * 0.31 * float(b_13_4_1_data)
    result = str(calculation_result)
    b_13_5_1.insert(0, result)

def b_13_5_2_logic(event):
    b_13_4_2_data = b_13_4_2.get()
    calculation_result = (621 + 165) * 0.31 * float(b_13_4_2_data)
    result = str(calculation_result)
    b_13_5_2.insert(0, result)

def b_13_5_3_logic(event):
    b_13_4_3_data = b_13_4_3.get()
    calculation_result = (159 + 71) * 0.31 * float(b_13_4_3_data)
    result = str(calculation_result)
    b_13_5_3.insert(0, result)

def b_13_5_4_logic(event):
    b_13_4_4_data = b_13_4_4.get()
    calculation_result = (479 + 124) * 0.31 * float(b_13_4_4_data)
    result = str(calculation_result)
    b_13_5_4.insert(0, result)

def b_13_5_5_logic(event):
    b_13_4_1_data = b_13_4_1.get()
    calculation_result = 2.4 * 5.5 * float(b_13_4_1_data)
    result = str(calculation_result)
    b_13_5_5.insert(0, result)

def b_13_5_6_logic(event):
    b_13_4_2_data = b_13_4_2.get()
    calculation_result = 2.4 * 5.5 * float(b_13_4_2_data)
    result = str(calculation_result)
    b_13_5_6.insert(0, result)

def b_13_5_7_logic(event):
    b_13_4_3_data = b_13_4_3.get()
    calculation_result = 2.4 * 5.5 * float(b_13_4_3_data)
    result = str(calculation_result)
    b_13_5_7.insert(0, result)

def b_13_5_8_logic(event):
    b_13_4_4_data = b_13_4_4.get()
    calculation_result = 2.4 * 5.5 * float(b_13_4_4_data)
    result = str(calculation_result)
    b_13_5_8.insert(0, result)

def b_13_5_9_logic(event):
    b_13_4_5_data = b_13_4_5.get()
    b_13_6_1_data = b_13_6_1.get()
    calculation_result = ((621 + 165) * 0.31 * float(b_13_6_1_data)) + ((551 + 145) * 0.31 * float(b_13_4_5_data))
    result = str(calculation_result)
    b_13_5_9.insert(0, result)

def b_13_5_10_logic(event):
    b_13_4_6_data = b_13_4_6.get()
    b_13_6_2_data = b_13_6_2.get()
    calculation_result = ((621 + 165) * 0.31 * float(b_13_6_2_data)) + ((551 + 145) * 0.31 * float(b_13_4_6_data))
    result = str(calculation_result)
    b_13_5_10.insert(0, result)

def b_13_5_11_logic(event):
    b_13_4_7_data = b_13_4_7.get()
    b_13_6_3_data = b_13_6_3.get()
    calculation_result = ((159 + 71) * 0.31 * float(b_13_6_3_data)) + ((460 + 125) * 0.31 * float(b_13_4_7_data))
    result = str(calculation_result)
    b_13_5_11.insert(0, result)

def b_13_5_12_logic(event):
    b_13_4_8_data = b_13_4_8.get()
    b_13_6_4_data = b_13_6_4.get()
    calculation_result = ((621 + 165) * 0.31 * float(b_13_6_4_data)) + ((551 + 145) * 0.31 * float(b_13_4_8_data))
    result = str(calculation_result)
    b_13_5_12.insert(0, result)

def b_13_5_13_logic(event):
    b_13_4_5_data = b_13_4_5.get()
    b_13_6_1_data = b_13_6_1.get()
    calculation_result = 2.4 * 5.5 * (float(b_13_4_5_data) + float(b_13_6_1_data))
    result = str(calculation_result)
    b_13_5_13.insert(0, result)

def b_13_5_14_logic(event):
    b_13_4_6_data = b_13_4_6.get()
    b_13_6_2_data = b_13_6_2.get()
    calculation_result = 2.4 * 5.5 * (float(b_13_4_6_data) + float(b_13_6_2_data))
    result = str(calculation_result)
    b_13_5_14.insert(0, result)

def b_13_5_15_logic(event):
    b_13_4_7_data = b_13_4_7.get()
    b_13_6_3_data = b_13_6_3.get()
    calculation_result = 2.4 * 5.5 * (float(b_13_4_7_data) + float(b_13_6_3_data))
    result = str(calculation_result)
    b_13_5_15.insert(0, result)

def b_13_5_16_logic(event):
    b_13_4_8_data = b_13_4_8.get()
    b_13_6_4_data = b_13_6_4.get()
    calculation_result = 2.4 * 5.5 * (float(b_13_4_8_data) + float(b_13_6_4_data))
    result = str(calculation_result)
    b_13_5_16.insert(0, result)

def b_13_1_1_logic(event):
    b_13_5_1_data = b_13_5_1.get()
    b_13_5_5_data = b_13_5_5.get()
    calculation_result = float(b_13_5_1_data) + float(b_13_5_5_data)
    result = str(calculation_result)
    b_13_1_1.insert(0, result)

def b_13_1_2_logic(event):
    b_13_5_2_data = b_13_5_2.get()
    b_13_5_6_data = b_13_5_6.get()
    calculation_result = float(b_13_5_2_data) + float(b_13_5_6_data)
    result = str(calculation_result)
    b_13_1_2.insert(0, result)

def b_13_1_3_logic(event):
    b_13_5_3_data = b_13_5_1.get()
    b_13_5_7_data = b_13_5_5.get()
    calculation_result = float(b_13_5_3_data) + float(b_13_5_7_data)
    result = str(calculation_result)
    b_13_1_3.insert(0, result)

def b_13_1_4_logic(event):
    b_13_5_4_data = b_13_5_4.get()
    b_13_5_8_data = b_13_5_8.get()
    calculation_result = float(b_13_5_4_data) + float(b_13_5_8_data)
    result = str(calculation_result)
    b_13_1_4.insert(0, result)

def b_13_2_1_logic(event):
    b_13_5_9_data = b_13_5_9.get()
    b_13_5_13_data = b_13_5_13.get()
    calculation_result = float(b_13_5_9_data) + float(b_13_5_13_data)
    result = str(calculation_result)
    b_13_2_1.insert(0, result)

def b_13_2_2_logic(event):
    b_13_5_10_data = b_13_5_10.get()
    b_13_5_14_data = b_13_5_14.get()
    calculation_result = float(b_13_5_10_data) + float(b_13_5_14_data)
    result = str(calculation_result)
    b_13_2_2.insert(0, result)

def b_13_2_3_logic(event):
    b_13_5_11_data = b_13_5_11.get()
    b_13_5_15_data = b_13_5_15.get()
    calculation_result = float(b_13_5_11_data) + float(b_13_5_15_data)
    result = str(calculation_result)
    b_13_2_3.insert(0, result)

def b_13_2_4_logic(event):
    b_13_5_12_data = b_13_5_12.get()
    b_13_5_16_data = b_13_5_16.get()
    calculation_result = float(b_13_5_12_data) + float(b_13_5_16_data)
    result = str(calculation_result)
    b_13_2_4.insert(0, result)

def b_13_3_logic(event):
    b_13_1_1_data = b_13_1_1.get()
    b_13_1_2_data = b_13_1_2.get()
    b_13_1_3_data = b_13_1_3.get()
    b_13_1_4_data = b_13_1_4.get()
    b_13_2_1_data = b_13_2_1.get()
    b_13_2_2_data = b_13_2_2.get()
    b_13_2_3_data = b_13_2_3.get()
    b_13_2_4_data = b_13_2_4.get()
    list = [float(b_13_1_1_data), float(b_13_1_2_data), float(b_13_1_3_data), float(b_13_1_4_data), float(b_13_2_1_data), float(b_13_2_2_data), float(b_13_2_3_data), float(b_13_2_4_data)] 
    calculation_result = sum(list)
    result = str(calculation_result)
    b_13_3.insert(0, result)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

sc = CTk()
sc.title("Mechanical Engineer Calculator")
sc.geometry("1920x1080")

b_1 = CTkButton(master=sc, text="?", width=3, height=25, corner_radius=0, command=b_1_clicked)
b_1.grid(row=0, column=0)

b_2 = CTkButton(master=sc, text="грејач и хладњак", width=12, height=25, corner_radius=0, command=b_2_clicked)
b_2.grid(row=0, column=1)

b_2_1_firstdata = CTkEntry(master=sc, height=1, width=195)
b_2_1_firstdata_text1 = CTkLabel(master=sc, text="количина ваздуха")
b_2_1_firstdata_text2 = CTkLabel(master=sc, text="м3/ч")

b_2_1_seconddata = CTkEntry(master=sc, height=1, width=195)
b_2_1_seconddata_text1 = CTkLabel(master=sc, text="излазна температура ваздуха из коморе - зима")
b_2_1_seconddata_text2 = CTkLabel(master=sc, text="*c")

b_2_1_thirddata = CTkEntry(master=sc, height=1, width=195)
b_2_1_thirddata_text1 = CTkLabel(master=sc, text="излазна температура ваздуха из коморе - лето")
b_2_1_thirddata_text2 = CTkLabel(master=sc, text="*c")

b_2_1_fourthdata = CTkEntry(master=sc, height=1, width=195)
b_2_1_fourthdata_text1 = CTkLabel(master=sc, text="разлика t подаћа/обратка - топла вода")
b_2_1_fourthdata_text2 = CTkLabel(master=sc, text="*c")

b_2_1_fifthdata = CTkEntry(master=sc, height=1, width=195)
b_2_1_fifthdata_text1 = CTkLabel(master=sc, text="разлика t подаћа/обратка - хладна вода")
b_2_1_fifthdata_text2 = CTkLabel(master=sc, text="*c")

b_2_2_text1 = CTkLabel(master=sc, text="Град")

b_2_2_text2 = CTkLabel(master=sc, text="Москва") 
    
b_2_2_firstdata = CTkEntry(master=sc, height=1, width=195)
b_2_2_firstdata_text1 = CTkLabel(master=sc, text="спољња пројектна температура - зима")
b_2_2_firstdata_text2 = CTkLabel(master=sc, text="*c")    

b_2_2_seconddata = CTkEntry(master=sc, height=1, width=195)
b_2_2_seconddata_text1 = CTkLabel(master=sc, text="спољња пројектна температура - лето")
b_2_2_seconddata_text2 = CTkLabel(master=sc, text="*c")

b_2_3_text = CTkLabel(master=sc, text="Грејач")
        
b_2_3_firstdata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_2_3_firstdata_text1 = CTkLabel(master=sc, text="капацитет грејаћа")
b_2_3_firstdata_text2 = CTkLabel(master=sc, text="вт(W)")

b_2_3_firstdata.bind('<Return>', b_2_3_1_logic)
        
b_2_3_seconddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_2_3_seconddata_text1 = CTkLabel(master=sc, text="проток воде")
b_2_3_seconddata_text2 = CTkLabel(master=sc, text="л/ч")

b_2_3_seconddata.bind('<Return>', b_2_3_2_logic)

b_2_4_text = CTkLabel(master=sc, text="Хладњак")
        
b_2_4_firstdata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_2_4_firstdata_text1 = CTkLabel(master=sc, text="капацитет хладњака")
b_2_4_firstdata_text2 = CTkLabel(master=sc, text="вт(W)")

b_2_4_firstdata.bind('<Return>', b_2_4_1_logic)

b_2_4_seconddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_2_4_seconddata_text1 = CTkLabel(master=sc, text="проток воде")
b_2_4_seconddata_text2 = CTkLabel(master=sc, text="л/ч")

b_2_4_seconddata.bind('<Return>', b_2_4_2_logic)

b_2_4_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_2_4_thirddata_text1 = CTkLabel(master=sc, text="проток воде-гликол 30%")
b_2_4_thirddata_text2 = CTkLabel(master=sc, text="л/ч")

b_2_4_thirddata.bind('<Return>', b_2_4_3_logic)

b_2_5_text = CTkLabel(master=sc, text="Унеси")

b_2_5_firstdata = CTkEntry(master=sc, width=195, height=1)
b_2_5_firstdata_text1 = CTkLabel(master=sc, text="капацитет хладњака")
b_2_5_firstdata_text2 = CTkLabel(master=sc, text="Вт(W)")

b_2_5_seconddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_2_5_seconddata_text1 = CTkLabel(master=sc, text="проток воде")
b_2_5_seconddata_text2 = CTkLabel(master=sc, text="л/ч")

b_2_5_seconddata.bind('<Return>', b_2_5_2_logic)

b_3 = CTkButton(master=sc, text="вентилација", width=8, height=25, corner_radius=0,  command=b_3_clicked)
b_3.grid(row=0, column=2)

b_3_firstdata = CTkEntry(master=sc, width=195, height=1)
b_3_firstdata_text1 = CTkLabel(master=sc, text="cтрана А")
b_3_firstdata_text2 = CTkLabel(master=sc, text="мм")

b_3_seconddata = CTkEntry(master=sc, width=195, height=1)
b_3_seconddata_text1 = CTkLabel(master=sc, text="страна Б")
b_3_seconddata_text2 = CTkLabel(master=sc, text="мм")

b_3_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_3_thirddata_text1 = CTkLabel(master=sc, text="еквивалентни дијаметар")
b_3_thirddata_text2 = CTkLabel(master=sc, text="мм")

b_3_thirddata.bind('<Return>', b_3_logic)

b_4 = CTkButton(master=sc, text="ваздушно грејање", width=12, height=25, corner_radius=0, command=b_4_clicked)
b_4.grid(row=0, column=3)

b_4_firstdata = CTkEntry(sc, width=195, height=1)
b_4_firstdata_text1 = CTkLabel(sc, text="количина топлоте")
b_4_firstdata_text2 = CTkLabel(sc, text="Вт(W)")

b_4_seconddata = CTkEntry(sc, width=195, height=1)
b_4_seconddata_text1 = CTkLabel(sc, text="температура собе")
b_4_seconddata_text2 = CTkLabel(sc, text="*c")

b_4_thirddata = CTkEntry(sc, width=195, height=1)
b_4_thirddata_text1 = CTkLabel(sc, text="температура притока")
b_4_thirddata_text2 = CTkLabel(sc, text="*c")

b_4_fourthdata = CTkEntry(sc, width=195, height=1)
b_4_fourthdata_text1 = CTkLabel(sc, text="густина ваздуха")
b_4_fourthdata_text2 = CTkLabel(sc, text="кг/м3")

b_4_fifthdata = CTkEntry(sc, width=195, height=1, placeholder_text="резултат")
b_4_fifthdata_text1 = CTkLabel(sc, text="количина ваздуха")
b_4_fifthdata_text2 = CTkLabel(sc, text="м3/ч")

b_4_fifthdata.bind('<Return>', b_4_logic)

b_4_data_table_text = CTkLabel(master=sc, text="густина ваздуха у Москви p = 990 кг/м3")

b_4_data_table = CTkTabview(master=sc)

b_4_data_table.add("температура")
b_4_data_table.add("густина")

b_4_data_table.set("температура")

b_4_data_1_1 = CTkLabel(master=b_4_data_table.tab("температура"), text="0")
b_4_data_1_1.grid(row=0, column=0)

b_4_data_1_2 = CTkLabel(master=b_4_data_table.tab("температура"), text="2")
b_4_data_1_2.grid(row=1, column=0)

b_4_data_1_3 = CTkLabel(master=b_4_data_table.tab("температура"), text="4")
b_4_data_1_3.grid(row=2, column=0)

b_4_data_1_4 = CTkLabel(master=b_4_data_table.tab("температура"), text="6")
b_4_data_1_4.grid(row=3, column=0)

b_4_data_1_5 = CTkLabel(master=b_4_data_table.tab("температура"), text="8")
b_4_data_1_5.grid(row=4, column=0)

b_4_data_1_6 = CTkLabel(master=b_4_data_table.tab("температура"), text="10")
b_4_data_1_6.grid(row=5, column=0)

b_4_data_1_7 = CTkLabel(master=b_4_data_table.tab("температура"), text="12")
b_4_data_1_7.grid(row=6, column=0)

b_4_data_1_8 = CTkLabel(master=b_4_data_table.tab("температура"), text="14")
b_4_data_1_8.grid(row=7, column=0)

b_4_data_1_9 = CTkLabel(master=b_4_data_table.tab("температура"), text="16")
b_4_data_1_9.grid(row=8, column=0)

b_4_data_1_10 = CTkLabel(master=b_4_data_table.tab("температура"), text="18")
b_4_data_1_10.grid(row=9, column=0)

b_4_data_1_11 = CTkLabel(master=b_4_data_table.tab("температура"), text="20")
b_4_data_1_11.grid(row=10, column=0)

b_4_data_1_12 = CTkLabel(master=b_4_data_table.tab("температура"), text="22")
b_4_data_1_12.grid(row=11, column=0)

b_4_data_1_13 = CTkLabel(master=b_4_data_table.tab("температура"), text="24")
b_4_data_1_13.grid(row=12, column=0)

b_4_data_1_14 = CTkLabel(master=b_4_data_table.tab("температура"), text="26")
b_4_data_1_14.grid(row=13, column=0)

b_4_data_1_15 = CTkLabel(master=b_4_data_table.tab("температура"), text="28")
b_4_data_1_15.grid(row=14, column=0)

b_4_data_1_16 = CTkLabel(master=b_4_data_table.tab("температура"), text="30")
b_4_data_1_16.grid(row=15, column=0)

b_4_data_1_17 = CTkLabel(master=b_4_data_table.tab("температура"), text="32")
b_4_data_1_17.grid(row=16, column=0)

b_4_data_2_1 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.263")
b_4_data_2_1.grid(row=0, column=0)

b_4_data_2_2 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.253")
b_4_data_2_2.grid(row=1, column=0)

b_4_data_2_3 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.244")
b_4_data_2_3.grid(row=2, column=0)

b_4_data_2_4 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.236")
b_4_data_2_4.grid(row=3, column=0)

b_4_data_2_5 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.227")
b_4_data_2_5.grid(row=4, column=0)

b_4_data_2_6 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.218")
b_4_data_2_6.grid(row=5, column=0)

b_4_data_2_7 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.21")
b_4_data_2_7.grid(row=6, column=0)

b_4_data_2_8 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.201")
b_4_data_2_8.grid(row=7, column=0)

b_4_data_2_9 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.193")
b_4_data_2_9.grid(row=8, column=0)

b_4_data_2_10 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.185")
b_4_data_2_10.grid(row=9, column=0)

b_4_data_2_11 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.177")
b_4_data_2_11.grid(row=10, column=0)

b_4_data_2_12 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.169")
b_4_data_2_12.grid(row=11, column=0)

b_4_data_2_13 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.161")
b_4_data_2_13.grid(row=12, column=0)

b_4_data_2_14 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.153")
b_4_data_2_14.grid(row=13, column=0)

b_4_data_2_15 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.145")
b_4_data_2_15.grid(row=14, column=0)

b_4_data_2_16 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.138")
b_4_data_2_16.grid(row=15, column=0)

b_4_data_2_17 = CTkLabel(master=b_4_data_table.tab("густина"), text="1.13")
b_4_data_2_17.grid(row=16, column=0)

b_5 = CTkButton(master=sc, text="грејање проток", width=10, height=25, corner_radius=0, command=b_5_clicked)
b_5.grid(row=0, column=4)

b_5_1_firstdata = CTkEntry(master=sc, width=195, height=1)
b_5_1_firstdata_text1 = CTkLabel(master=sc, text="количина топлоте")
b_5_1_firstdata_text2 = CTkLabel(master=sc, text="Вт(W)")

b_5_1_seconddata = CTkEntry(sc, width=195, height=1)
b_5_1_seconddata_text1 = CTkLabel(master=sc, text="разлика t подача/обратка - топла вода")
b_5_1_seconddata_text2 = CTkLabel(master=sc, text="*c")

b_5_1_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_5_1_thirddata_text1 = CTkLabel(master=sc, text="проток воде")
b_5_1_thirddata_text2 = CTkLabel(master=sc, text="л/ч")

b_5_1_thirddata.bind('<Return>', b_5_1_3_logic)

b_5_2_firstdata = CTkEntry(master=sc, width=195, height=1)
b_5_2_firstdata_text1 = CTkLabel(master=sc, text="разлика t подача/обратка - хладна вода")
b_5_2_firstdata_text2 = CTkLabel(master=sc, text="*c")

b_5_2_seconddata = CTkEntry(master=sc, width=195, height=1)
b_5_2_seconddata_text1 = CTkLabel(master=sc, text="количина расхладне топлоте")
b_5_2_seconddata_text2 = CTkLabel(master=sc, text="Вт(W)")

b_5_2_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_5_2_thirddata_text1 = CTkLabel(master=sc, text="проток воде")
b_5_2_thirddata_text2 = CTkLabel(master=sc, text="л/ч")

b_5_2_thirddata.bind('<Return>', b_5_2_3_logic)

b_5_2_fourthdata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_5_2_fourthdata_text1 = CTkLabel(master=sc, text="проток воде - гликол 30%")
b_5_2_fourthdata_text2 = CTkLabel(master=sc, text="л/ч")

b_5_2_fourthdata.bind('<Return>', b_5_2_4_logic)

b_5_3_firstdata = CTkEntry(master=sc, width=195, height=1)
b_5_3_firstdata_text1 = CTkLabel(master=sc, text="проток воде")
b_5_3_firstdata_text2 = CTkLabel(master=sc, text="л/ч")

b_5_3_seconddata = CTkEntry(master=sc, width=195, height=1)
b_5_3_seconddata_text1 = CTkLabel(master=sc, text="разлика t")
b_5_3_seconddata_text2 = CTkLabel(sc, text="*c")

b_5_3_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_5_3_thirddata_text1 = CTkLabel(master=sc, text="количина топлоте")
b_5_3_thirddata_text2 = CTkLabel(master=sc, text="Вт(W)")

b_5_3_thirddata.bind('<Return>', b_5_3_3_logic)

b_6 = CTkButton(master=sc, text="брзина у цевима", width=10, height=25, corner_radius=0, command=b_6_clicked)
b_6.grid(row=0, column=5)

b_6_1_firstdata = CTkEntry(master=sc, width=195, height=1)
b_6_1_firstdata_text1 = CTkLabel(master=sc, text="унутрашњи пречник")
b_6_1_firstdata_text2 = CTkLabel(master=sc, text="мм")

b_6_1_seconddata = CTkEntry(master=sc, width=195, height=1)
b_6_1_seconddata_text1 = CTkLabel(master=sc, text="проток")
b_6_1_seconddata_text2 = CTkLabel(master=sc, text="м3/ч")

b_6_1_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_6_1_thirddata_text1 = CTkLabel(master=sc, text="брзина")
b_6_1_thirddata_text2 = CTkLabel(master=sc, text="м/с")

b_6_1_thirddata.bind('<Return>', b_6_1_3_logic)

b_6_2_firstdata = CTkEntry(master=sc, width=195, height=1)
b_6_2_firstdata_text1 = CTkLabel(master=sc, text="брзина")
b_6_2_firstdata_text2 = CTkLabel(master=sc, text="м/с")

b_6_2_seconddata = CTkEntry(master=sc, width=195, height=1)
b_6_2_seconddata_text1 = CTkLabel(master=sc, text="проток")
b_6_2_seconddata_text2 = CTkLabel(master=sc, text="м3/ч")

b_6_2_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_6_2_thirddata_text1 = CTkLabel(master=sc, text="пречник")
b_6_2_thirddata_text2 = CTkLabel(master=sc, text="мм")

b_6_2_thirddata.bind('<Return>', b_6_2_3_logic)

b_6_3_firstdata = CTkEntry(master=sc, width=195, height=1)
b_6_3_firstdata_text1 = CTkLabel(master=sc, text="брзина")
b_6_3_firstdata_text2 = CTkLabel(master=sc, text="м/с")

b_6_3_seconddata = CTkEntry(master=sc, width=195, height=1)
b_6_3_seconddata_text1 = CTkLabel(master=sc, text="пречник")
b_6_3_seconddata_text2 = CTkLabel(master=sc, text="мм")

b_6_3_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_6_3_thirddata_text1 = CTkLabel(master=sc, text="проток")
b_6_3_thirddata_text2 = CTkLabel(master=sc, text="м3/ч")

b_6_3_thirddata.bind('<Return>', b_6_3_3_logic)

b_7 = CTkButton(master=sc, text="раутитан таблица", width=12, height=25, corner_radius=0,  command=b_7_clicked)
b_7.grid(row=0, column=6)

b_7_1_text = CTkLabel(master=sc, height=1, text="раутитан стабил(кг/ч)")

b_7_1_1_1_text = CTkLabel(master=sc, height=1, text="16.2 * 2.6")

b_7_1_2_1_text = CTkLabel(master=sc, height=1, text="20 * 2.9")

b_7_1_3_1_text = CTkLabel(master=sc, height=1, text="25 * 3.7")

b_7_1_4_1_text = CTkLabel(master=sc, height=1, text="32 * 4.7")

b_7_1_5_1_text = CTkLabel(master=sc, height=1, text="40 * 6")

b_7_1_1_2_text = CTkLabel(master=sc, height=1, text="R=100Па/м")

b_7_1_2_2_text = CTkLabel(master=sc, height=1, text="R=150Па/м")

b_7_1_3_2_text = CTkLabel(master=sc, height=1, text="R=200Па/м")

b_7_1_1 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_2 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_3 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_4 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_5 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_6 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_7 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_8 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_9 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_10 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_11 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_12 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_13 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_14 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_1_15 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_2_text = CTkLabel(master=sc, height=1, text="раутитан стабил(Bт - dT = 10c*)")

b_7_2_1_1_text = CTkLabel(master=sc, height=1, text="16.2 * 2.6")

b_7_2_2_1_text = CTkLabel(master=sc, height=1, text="20 * 2.9")

b_7_2_3_1_text = CTkLabel(master=sc, height=1, text="25 * 3.7")

b_7_2_4_1_text = CTkLabel(master=sc, height=1, text="32 * 4.7")

b_7_2_5_1_text = CTkLabel(master=sc, height=1, text="40 * 6")

b_7_2_1_2_text = CTkLabel(master=sc, height=1, text="R=100Па/м")

b_7_2_2_2_text = CTkLabel(master=sc, height=1, text="R=150Па/м")

b_7_2_3_2_text = CTkLabel(master=sc, height=1, text="R=200Па/м")

b_7_2_1 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_1.bind('<Return>', b_7_2_1_logic)

b_7_2_2 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_2.bind('<Return>', b_7_2_2_logic)

b_7_2_3 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_3.bind('<Return>', b_7_2_3_logic)

b_7_2_4 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_4.bind('<Return>', b_7_2_4_logic)

b_7_2_5 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_5.bind('<Return>', b_7_2_5_logic)

b_7_2_6 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_6.bind('<Return>', b_7_2_6_logic)

b_7_2_7 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_7.bind('<Return>', b_7_2_7_logic)

b_7_2_8 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_8.bind('<Return>', b_7_2_8_logic)

b_7_2_9 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_9.bind('<Return>', b_7_2_9_logic)

b_7_2_10 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_10.bind('<Return>', b_7_2_10_logic)

b_7_2_11 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_11.bind('<Return>', b_7_2_11_logic)

b_7_2_12 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_12.bind('<Return>', b_7_2_12_logic)

b_7_2_13 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_13.bind('<Return>', b_7_2_13_logic)

b_7_2_14 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_14.bind('<Return>', b_7_2_14_logic)

b_7_2_15 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_2_15.bind('<Return>', b_7_2_15_logic)

b_7_3_text = CTkLabel(master=sc, height=1, text="раутитан стабил(Bт - dT = 20c*)")

b_7_3_1_1_text = CTkLabel(master=sc, height=1, text="16.2 * 2.6")

b_7_3_2_1_text = CTkLabel(master=sc, height=1, text="20 * 2.9")

b_7_3_3_1_text = CTkLabel(master=sc, height=1, text="25 * 3.7")

b_7_3_4_1_text = CTkLabel(master=sc, height=1, text="32 * 4.7")

b_7_3_5_1_text = CTkLabel(master=sc, height=1, text="40 * 6")

b_7_3_1_2_text = CTkLabel(master=sc, height=1, text="R=100Па/м")

b_7_3_2_2_text = CTkLabel(master=sc, height=1, text="R=150Па/м")

b_7_3_3_2_text = CTkLabel(master=sc, height=1, text="R=200Па/м")

b_7_3_1 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_1.bind('<Return>', b_7_3_1_logic)

b_7_3_2 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_2.bind('<Return>', b_7_3_2_logic)

b_7_3_3 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_3.bind('<Return>', b_7_3_3_logic)

b_7_3_4 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_4.bind('<Return>', b_7_3_4_logic)

b_7_3_5 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_5.bind('<Return>', b_7_3_5_logic)

b_7_3_6 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_6.bind('<Return>', b_7_3_6_logic)

b_7_3_7 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_7.bind('<Return>', b_7_3_7_logic)

b_7_3_8 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_8.bind('<Return>', b_7_3_8_logic)

b_7_3_9 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_9.bind('<Return>', b_7_3_9_logic)

b_7_3_10 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_10.bind('<Return>', b_7_3_10_logic)

b_7_3_11 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_11.bind('<Return>', b_7_3_11_logic)

b_7_3_12 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_12.bind('<Return>', b_7_3_12_logic)

b_7_3_13 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_13.bind('<Return>', b_7_3_13_logic)

b_7_3_14 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_14.bind('<Return>', b_7_3_14_logic)

b_7_3_15 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_3_15.bind('<Return>', b_7_3_15_logic)

b_7_4_text = CTkLabel(master=sc, height=1, text="раутитан flex/pink (кг/ч)")

b_7_4_1_1_text = CTkLabel(master=sc, height=1, text="16.2 * 2.6")

b_7_4_2_1_text = CTkLabel(master=sc, height=1, text="20 * 2.9")

b_7_4_3_1_text = CTkLabel(master=sc, height=1, text="25 * 3.7")

b_7_4_4_1_text = CTkLabel(master=sc, height=1, text="32 * 4.7")

b_7_4_5_1_text = CTkLabel(master=sc, height=1, text="40 * 5.5")

b_7_4_6_1_text = CTkLabel(master=sc, height=1, text="50 * 6.9")

b_7_4_7_1_text = CTkLabel(master=sc, height=1, text="63 * 8.6")

b_7_4_1_2_text = CTkLabel(master=sc, height=1, text="R=100Па/м")

b_7_4_2_2_text = CTkLabel(master=sc, height=1, text="R=150Па/м")

b_7_4_3_2_text = CTkLabel(master=sc, height=1, text="R=200Па/м")

b_7_4_1 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_2 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_3 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_4 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_5 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_6 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_7 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_8 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_9 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_10 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_11 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_12 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_13 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_14 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_15 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_16 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_17 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_18 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_19 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_20 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_4_21 = CTkEntry(master=sc, width=64, height=1, corner_radius=0)

b_7_5_text = CTkLabel(master=sc, height=1, text="раутитан flex/pink (Вт - dT = 10c*)")

b_7_5_1_1_text = CTkLabel(master=sc, height=1, text="16.2 * 2.6")

b_7_5_2_1_text = CTkLabel(master=sc, height=1, text="20 * 2.9")

b_7_5_3_1_text = CTkLabel(master=sc, height=1, text="25 * 3.7")

b_7_5_4_1_text = CTkLabel(master=sc, height=1, text="32 * 4.7")

b_7_5_5_1_text = CTkLabel(master=sc, height=1, text="40 * 5.5")

b_7_5_6_1_text = CTkLabel(master=sc, height=1, text="50 * 6.9")

b_7_5_7_1_text = CTkLabel(master=sc, height=1, text="63 * 8.6")

b_7_5_1_2_text = CTkLabel(master=sc, height=1, text="R=100Па/м")

b_7_5_2_2_text = CTkLabel(master=sc, height=1, text="R=150Па/м")

b_7_5_3_2_text = CTkLabel(master=sc, height=1, text="R=200Па/м")

b_7_5_1 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_1.bind('<Return>', b_7_5_1_logic)

b_7_5_2 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_2.bind('<Return>', b_7_5_2_logic)

b_7_5_3 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_3.bind('<Return>', b_7_5_3_logic)

b_7_5_4 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_4.bind('<Return>', b_7_5_4_logic)

b_7_5_5 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_5.bind('<Return>', b_7_5_5_logic)

b_7_5_6 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_6.bind('<Return>', b_7_5_6_logic)

b_7_5_7 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_7.bind('<Return>', b_7_5_7_logic)

b_7_5_8 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_8.bind('<Return>', b_7_5_8_logic)

b_7_5_9 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_9.bind('<Return>', b_7_5_9_logic)

b_7_5_10 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_10.bind('<Return>', b_7_5_10_logic)

b_7_5_11 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_11.bind('<Return>', b_7_5_11_logic)

b_7_5_12 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_12.bind('<Return>', b_7_5_12_logic)

b_7_5_13 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_13.bind('<Return>', b_7_5_13_logic)

b_7_5_14 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_14.bind('<Return>', b_7_5_14_logic)

b_7_5_15 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_15.bind('<Return>', b_7_5_15_logic)

b_7_5_16 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_16.bind('<Return>', b_7_5_16_logic)

b_7_5_17 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_17.bind('<Return>', b_7_5_17_logic)

b_7_5_18 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_18.bind('<Return>', b_7_5_18_logic)

b_7_5_19 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_19.bind('<Return>', b_7_5_19_logic)

b_7_5_20 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_20.bind('<Return>', b_7_5_20_logic)

b_7_5_21 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_5_21.bind('<Return>', b_7_5_21_logic)

b_7_6_text = CTkLabel(master=sc, height=1, text="раутитан flex/pink (Вт - dT = 20c*)")

b_7_6_1_1_text = CTkLabel(master=sc, height=1, text="16.2 * 2.6")

b_7_6_2_1_text = CTkLabel(master=sc, height=1, text="20 * 2.9")

b_7_6_3_1_text = CTkLabel(master=sc, height=1, text="25 * 3.7")

b_7_6_4_1_text = CTkLabel(master=sc, height=1, text="32 * 4.7")

b_7_6_5_1_text = CTkLabel(master=sc, height=1, text="40 * 5.5")

b_7_6_6_1_text = CTkLabel(master=sc, height=1, text="50 * 6.9")

b_7_6_7_1_text = CTkLabel(master=sc, height=1, text="63 * 8.6")

b_7_6_1_2_text = CTkLabel(master=sc, height=1, text="R=100Па/м")

b_7_6_2_2_text = CTkLabel(master=sc, height=1, text="R=150Па/м")

b_7_6_3_2_text = CTkLabel(master=sc, height=1, text="R=200Па/м")

b_7_6_1 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_1.bind('<Return>', b_7_6_1_logic)

b_7_6_2 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_2.bind('<Return>', b_7_6_2_logic)

b_7_6_3 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_3.bind('<Return>', b_7_6_3_logic)

b_7_6_4 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_4.bind('<Return>', b_7_6_4_logic)

b_7_6_5 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_5.bind('<Return>', b_7_6_5_logic)

b_7_6_6 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_6.bind('<Return>', b_7_6_6_logic)

b_7_6_7 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_7.bind('<Return>', b_7_6_7_logic)

b_7_6_8 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_8.bind('<Return>', b_7_6_8_logic)

b_7_6_9 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_9.bind('<Return>', b_7_6_9_logic)

b_7_6_10 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_10.bind('<Return>', b_7_6_10_logic)

b_7_6_11 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_11.bind('<Return>', b_7_6_11_logic)

b_7_6_12 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_12.bind('<Return>', b_7_6_12_logic)

b_7_6_13 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_13.bind('<Return>', b_7_6_13_logic)

b_7_6_14 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_14.bind('<Return>', b_7_6_14_logic)

b_7_6_15 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_15.bind('<Return>', b_7_6_15_logic)

b_7_6_16 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_16.bind('<Return>', b_7_6_16_logic)

b_7_6_17 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_17.bind('<Return>', b_7_6_17_logic)

b_7_6_18 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_18.bind('<Return>', b_7_6_18_logic)

b_7_6_19 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_19.bind('<Return>', b_7_6_19_logic)

b_7_6_20 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_20.bind('<Return>', b_7_6_20_logic)

b_7_6_21 = CTkEntry(master=sc, width=64, height=1, corner_radius=0, placeholder_text="резултат")

b_7_6_21.bind('<Return>', b_7_6_21_logic)

b_8 = CTkButton(master=sc, text="диаметар колектора", width=10, height=25, corner_radius=0, command=b_8_clicked)
b_8.grid(row=0, column=7)

b_8_text1 = CTkLabel(master=sc, height=1, text="ред број")

b_8_text2 = CTkLabel(master=sc, height=1, text="унутрашњи пречник цеви прикључка(мм)")

b_8_text3 = CTkLabel(master=sc, height=1, text="површина прикључка(мм2)")

b_8_1_1 = CTkLabel(master=sc, height=1, text="1")

b_8_1_2 = CTkLabel(master=sc, height=1, text="2")

b_8_1_3 = CTkLabel(master=sc, height=1, text="3")

b_8_1_4 = CTkLabel(master=sc, height=1, text="4")

b_8_1_5 = CTkLabel(master=sc, height=1, text="5")

b_8_1_6 = CTkLabel(master=sc, height=1, text="6")

b_8_1_7 = CTkLabel(master=sc, height=1, text="7")

b_8_1_8 = CTkLabel(master=sc, height=1, text="8")

b_8_1_9 = CTkLabel(master=sc, height=1, text="9")

b_8_1_10 = CTkLabel(master=sc, height=1, text="10")

b_8_1_11 = CTkLabel(master=sc, height=1, text="11")

b_8_1_12 = CTkLabel(master=sc, height=1, text="12")

b_8_2_1 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_2 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_3 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_4 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_5 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_6 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_7 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_8 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_9 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_10 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_11 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_2_12 = CTkEntry(master=sc, width=266, height=1, corner_radius=0)

b_8_3_1 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_1.bind('<Return>', b_8_3_1_logic)

b_8_3_2 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_2.bind('<Return>', b_8_3_2_logic)

b_8_3_3 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_3.bind('<Return>', b_8_3_3_logic)

b_8_3_4 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_4.bind('<Return>', b_8_3_4_logic)

b_8_3_5 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_5.bind('<Return>', b_8_3_5_logic)

b_8_3_6 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_6.bind('<Return>', b_8_3_6_logic)

b_8_3_7 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_7.bind('<Return>', b_8_3_7_logic)

b_8_3_8 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_8.bind('<Return>', b_8_3_8_logic)

b_8_3_9 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_9.bind('<Return>', b_8_3_9_logic)

b_8_3_10 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_10.bind('<Return>', b_8_3_10_logic)

b_8_3_11 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_11.bind('<Return>', b_8_3_11_logic)

b_8_3_12 = CTkEntry(master=sc, width=266, height=1, corner_radius=0, placeholder_text="резултат")

b_8_3_12.bind('<Return>', b_8_3_12_logic)

b_8_firstdata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_8_firstdata_text1 = CTkLabel(master=sc, text="укупна површина прикључака")
b_8_firstdata_text2 = CTkLabel(master=sc, text="мм2")

b_8_firstdata.bind('<Return>', b_8_1_logic)

b_8_seconddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_8_seconddata_text1 = CTkLabel(master=sc, text="еквивалентни дијаметар колектора")
b_8_seconddata_text2 = CTkLabel(master=sc, text="мм")

b_8_seconddata.bind('<Return>', b_8_2_logic)

b_8_thirddata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_8_thirddata_text1 = CTkLabel(master=sc, text="квадратни пресек колектора")
b_8_thirddata_text2 = CTkLabel(master=sc, text="мм")

b_8_thirddata.bind('<Return>', b_8_3_logic)

b_9 = CTkButton(master=sc, text="садржај воде у цевима", width=14, height=25, corner_radius=0, command=b_9_clicked)
b_9.grid(row=0, column=8)

b_9_1_text = CTkLabel(master=sc, height=1, text="називни отвор")

b_9_2_text = CTkLabel(master=sc, height=1, text="спољни пречник")

b_9_3_text = CTkLabel(master=sc, height=1, text="садржај воде л/м")

b_9_4_text = CTkLabel(master=sc, height=1, text="дужина цеви(м)")

b_9_5_text = CTkLabel(master=sc, height=1, text="укупно воде(л)")

b_9_text1 = CTkLabel(master=sc, height=1, text="навојне цеви према DIN 2240")

b_9_1_1 = CTkLabel(master=sc, height=1, text="DN10")

b_9_1_2 = CTkLabel(master=sc, height=1, text="DN15")

b_9_1_3 = CTkLabel(master=sc, height=1, text="DN20")

b_9_1_4 = CTkLabel(master=sc, height=1, text="DN25")

b_9_1_5 = CTkLabel(master=sc, height=1, text="DN32")

b_9_1_6 = CTkLabel(master=sc, height=1, text="DN40")

b_9_1_7 = CTkLabel(master=sc, height=1, text="DN50")

b_9_2_1 = CTkLabel(master=sc, height=1, text="17.2")

b_9_2_2 = CTkLabel(master=sc, height=1, text="21.3")

b_9_2_3 = CTkLabel(master=sc, height=1, text="26.9")

b_9_2_4 = CTkLabel(master=sc, height=1, text="33.7")

b_9_2_5 = CTkLabel(master=sc, height=1, text="42.4")

b_9_2_6 = CTkLabel(master=sc, height=1, text="48.3")

b_9_2_7 = CTkLabel(master=sc, height=1, text="60.3")

b_9_3_1 = CTkLabel(master=sc, height=1, text="0.123")

b_9_3_2 = CTkLabel(master=sc, height=1, text="0.201")

b_9_3_3 = CTkLabel(master=sc, height=1, text="0.366")

b_9_3_4 = CTkLabel(master=sc, height=1, text="0.581")

b_9_3_5 = CTkLabel(master=sc, height=1, text="1.01")

b_9_3_6 = CTkLabel(master=sc, height=1, text="1.37")

b_9_3_7 = CTkLabel(master=sc, height=1, text="2.16")

b_9_4_1 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_2 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_3 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_4 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_5 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_6 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_7 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_5_1 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_1.bind('<Return>', b_9_5_1_logic)

b_9_5_2 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_2.bind('<Return>', b_9_5_2_logic)

b_9_5_3 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_3.bind('<Return>', b_9_5_3_logic)

b_9_5_4 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_4.bind('<Return>', b_9_5_4_logic)

b_9_5_5 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_5.bind('<Return>', b_9_5_5_logic)

b_9_5_6 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_6.bind('<Return>', b_9_5_6_logic)

b_9_5_7 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_7.bind('<Return>', b_9_5_7_logic)

b_9_text2 = CTkLabel(master=sc, height=1, text="Бесавне цеви према DIN2449")

b_9_1_8 = CTkLabel(master=sc, height=1, text="DN40")

b_9_1_9 = CTkLabel(master=sc, height=1, text="DN50")

b_9_1_10 = CTkLabel(master=sc, height=1, text="DN60")

b_9_1_11 = CTkLabel(master=sc, height=1, text="DN65")

b_9_1_12 = CTkLabel(master=sc, height=1, text="DN80")

b_9_1_13 = CTkLabel(master=sc, height=1, text="DN90")

b_9_1_14 = CTkLabel(master=sc, height=1, text="DN100")

b_9_1_15 = CTkLabel(master=sc, height=1, text="DN110")

b_9_1_16 = CTkLabel(master=sc, height=1, text="DN125")

b_9_1_17 = CTkLabel(master=sc, height=1, text="DN150")

b_9_1_18 = CTkLabel(master=sc, height=1, text="DN200")

b_9_1_19 = CTkLabel(master=sc, height=1, text="DN250")

b_9_1_20 = CTkLabel(master=sc, height=1, text="DN300")

b_9_1_21 = CTkLabel(master=sc, height=1, text="DN350")

b_9_2_8 = CTkLabel(master=sc, height=1, text="44.5")

b_9_2_9 = CTkLabel(master=sc, height=1, text="57")

b_9_2_10 = CTkLabel(master=sc, height=1, text="70")

b_9_2_11 = CTkLabel(master=sc, height=1, text="76")

b_9_2_12 = CTkLabel(master=sc, height=1, text="89")

b_9_2_13 = CTkLabel(master=sc, height=1, text="102")

b_9_2_14 = CTkLabel(master=sc, height=1, text="108")

b_9_2_15 = CTkLabel(master=sc, height=1, text="121")

b_9_2_16 = CTkLabel(master=sc, height=1, text="133")

b_9_2_17 = CTkLabel(master=sc, height=1, text="159")

b_9_2_18 = CTkLabel(master=sc, height=1, text="219")

b_9_2_19 = CTkLabel(master=sc, height=1, text="273")

b_9_2_20 = CTkLabel(master=sc, height=1, text="323")

b_9_2_21 = CTkLabel(master=sc, height=1, text="355.6")

b_9_3_8 = CTkLabel(master=sc, height=1, text="1.23")

b_9_3_9 = CTkLabel(master=sc, height=1, text="2.08")

b_9_3_10 = CTkLabel(master=sc, height=1, text="3.22")

b_9_3_11 = CTkLabel(master=sc, height=1, text="3.85")

b_9_3_12 = CTkLabel(master=sc, height=1, text="5.35")

b_9_3_13 = CTkLabel(master=sc, height=1, text="7.09")

b_9_3_14 = CTkLabel(master=sc, height=1, text="7.93")

b_9_3_15 = CTkLabel(master=sc, height=1, text="10")

b_9_3_16 = CTkLabel(master=sc, height=1, text="12.3")

b_9_3_17 = CTkLabel(master=sc, height=1, text="17.7")

b_9_3_18 = CTkLabel(master=sc, height=1, text="33.7")

b_9_3_19 = CTkLabel(master=sc, height=1, text="53.2")

b_9_3_20 = CTkLabel(master=sc, height=1, text="75.3")

b_9_3_21 = CTkLabel(master=sc, height=1, text="90.5")

b_9_4_8 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_9 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_10 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_11 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_12 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_13 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_14 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_15 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_16 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_17 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_18 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_19 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_20 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_21 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_5_8 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_8.bind('<Return>', b_9_5_8_logic)

b_9_5_9 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_9.bind('<Return>', b_9_5_9_logic)

b_9_5_10 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_10.bind('<Return>', b_9_5_10_logic)

b_9_5_11 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_11.bind('<Return>', b_9_5_11_logic)

b_9_5_12 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_12.bind('<Return>', b_9_5_12_logic)

b_9_5_13 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_13.bind('<Return>', b_9_5_13_logic)

b_9_5_14 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_14.bind('<Return>', b_9_5_14_logic)

b_9_5_15 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_15.bind('<Return>', b_9_5_15_logic)

b_9_5_16 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_16.bind('<Return>', b_9_5_16_logic)

b_9_5_17 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_17.bind('<Return>', b_9_5_17_logic)

b_9_5_18 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_18.bind('<Return>', b_9_5_18_logic)

b_9_5_19 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_19.bind('<Return>', b_9_5_19_logic)

b_9_5_20 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_20.bind('<Return>', b_9_5_20_logic)

b_9_5_21 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_21.bind('<Return>', b_9_5_21_logic)

b_9_text3 = CTkLabel(master=sc, height=1, text="Бакарне цеви")

b_9_1_22 = CTkLabel(master=sc, height=1, text="DN8/0.8")

b_9_1_23 = CTkLabel(master=sc, height=1, text="DN10/0.8")

b_9_1_24 = CTkLabel(master=sc, height=1, text="DN12/1")

b_9_1_25 = CTkLabel(master=sc, height=1, text="DN15/1")

b_9_1_26 = CTkLabel(master=sc, height=1, text="DN18/1")

b_9_1_27 = CTkLabel(master=sc, height=1, text="DN22/1")

b_9_1_28 = CTkLabel(master=sc, height=1, text="DN28/1.2")

b_9_1_29 = CTkLabel(master=sc, height=1, text="DN35/1.5")

b_9_1_30 = CTkLabel(master=sc, height=1, text="DN42/1.5")

b_9_3_22 = CTkLabel(master=sc, height=1, text="0.03")

b_9_3_23 = CTkLabel(master=sc, height=1, text="0.06")

b_9_3_24 = CTkLabel(master=sc, height=1, text="0.08")

b_9_3_25 = CTkLabel(master=sc, height=1, text="0.13")

b_9_3_26 = CTkLabel(master=sc, height=1, text="0.2")

b_9_3_27 = CTkLabel(master=sc, height=1, text="0.3")

b_9_3_28 = CTkLabel(master=sc, height=1, text="0.52")

b_9_3_29 = CTkLabel(master=sc, height=1, text="0.8")

b_9_3_30 = CTkLabel(master=sc, height=1, text="1.2")

b_9_4_22 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_23 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_24 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_25 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_26 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_27 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_28 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_29 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_30 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_5_22 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_22.bind('<Return>', b_9_5_22_logic)

b_9_5_23 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_23.bind('<Return>', b_9_5_23_logic)

b_9_5_24 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_24.bind('<Return>', b_9_5_24_logic)

b_9_5_25 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_25.bind('<Return>', b_9_5_25_logic)

b_9_5_26 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_26.bind('<Return>', b_9_5_26_logic)

b_9_5_27 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_27.bind('<Return>', b_9_5_27_logic)

b_9_5_28 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_28.bind('<Return>', b_9_5_28_logic)

b_9_5_29 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_29.bind('<Return>', b_9_5_29_logic)

b_9_5_30 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_30.bind('<Return>', b_9_5_30_logic)

b_9_text4 = CTkLabel(master=sc, height=1, text="Rehau-rautitan flex")

b_9_1_31 = CTkLabel(master=sc, height=1, text="16x2.2")

b_9_1_32 = CTkLabel(master=sc, height=1, text="20x2.8")

b_9_1_33 = CTkLabel(master=sc, height=1, text="25x3.5")

b_9_1_34 = CTkLabel(master=sc, height=1, text="32x4.4")

b_9_1_35 = CTkLabel(master=sc, height=1, text="40x5.5")

b_9_1_36 = CTkLabel(master=sc, height=1, text="50x6.9")

b_9_1_37 = CTkLabel(master=sc, height=1, text="63x8.6")

b_9_2_31 = CTkLabel(master=sc, height=1, text="16")

b_9_2_32 = CTkLabel(master=sc, height=1, text="20")

b_9_2_33 = CTkLabel(master=sc, height=1, text="25")

b_9_2_34 = CTkLabel(master=sc, height=1, text="32")

b_9_2_35 = CTkLabel(master=sc, height=1, text="40")

b_9_2_36 = CTkLabel(master=sc, height=1, text="50")

b_9_2_37 = CTkLabel(master=sc, height=1, text="63")

b_9_3_31 = CTkLabel(master=sc, height=1, text="0.106")

b_9_3_32 = CTkLabel(master=sc, height=1, text="0.163")

b_9_3_33 = CTkLabel(master=sc, height=1, text="0.254")

b_9_3_34 = CTkLabel(master=sc, height=1, text="0.423")

b_9_3_35 = CTkLabel(master=sc, height=1, text="0.661")

b_9_3_36 = CTkLabel(master=sc, height=1, text="1.029")

b_9_3_37 = CTkLabel(master=sc, height=1, text="1.633")

b_9_4_31 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_32 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_33 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_34 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_35 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_36 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_37 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_5_31 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_31.bind('<Return>', b_9_5_31_logic)

b_9_5_32 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_32.bind('<Return>', b_9_5_32_logic)

b_9_5_33 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_33.bind('<Return>', b_9_5_33_logic)

b_9_5_34 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_34.bind('<Return>', b_9_5_34_logic)

b_9_5_35 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_35.bind('<Return>', b_9_5_35_logic)

b_9_5_36 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_36.bind('<Return>', b_9_5_36_logic)

b_9_5_37 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_37.bind('<Return>', b_9_5_37_logic)

b_9_text5 = CTkLabel(master=sc, height=1, text="Rehau-Rautherm S")

b_9_1_38 = CTkLabel(master=sc, height=1, text="10.1")

b_9_1_39 = CTkLabel(master=sc, height=1, text="14")

b_9_1_40 = CTkLabel(master=sc, height=1, text="16")

b_9_1_41 = CTkLabel(master=sc, height=1, text="17")

b_9_1_42 = CTkLabel(master=sc, height=1, text="20")

b_9_1_43 = CTkLabel(master=sc, height=1, text="25")

b_9_1_44 = CTkLabel(master=sc, height=1, text="32")

b_9_2_38 = CTkLabel(master=sc, height=1, text="10.1")

b_9_2_39 = CTkLabel(master=sc, height=1, text="14")

b_9_2_40 = CTkLabel(master=sc, height=1, text="16")

b_9_2_41 = CTkLabel(master=sc, height=1, text="17")

b_9_2_42 = CTkLabel(master=sc, height=1, text="20")

b_9_2_43 = CTkLabel(master=sc, height=1, text="25")

b_9_2_44 = CTkLabel(master=sc, height=1, text="32")

b_9_3_38 = CTkLabel(master=sc, height=1, text="0.049")

b_9_3_39 = CTkLabel(master=sc, height=1, text="0.095")

b_9_3_40 = CTkLabel(master=sc, height=1, text="0.113")

b_9_3_41 = CTkLabel(master=sc, height=1, text="0.113")

b_9_3_42 = CTkLabel(master=sc, height=1, text="0.201")

b_9_3_43 = CTkLabel(master=sc, height=1, text="0.327")

b_9_3_44 = CTkLabel(master=sc, height=1, text="0.539")

b_9_4_38 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_39 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_40 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_41 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_42 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_43 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_4_44 = CTkEntry(master=sc, width=103, height=1, corner_radius=0)

b_9_5_38 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_38.bind('<Return>', b_9_5_38_logic)

b_9_5_39 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_39.bind('<Return>', b_9_5_39_logic)

b_9_5_40 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_40.bind('<Return>', b_9_5_40_logic)

b_9_5_41 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_41.bind('<Return>', b_9_5_41_logic)

b_9_5_42 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_42.bind('<Return>', b_9_5_42_logic)

b_9_5_43 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_43.bind('<Return>', b_9_5_43_logic)

b_9_5_44 = CTkEntry(master=sc, width=103, height=1, corner_radius=0, placeholder_text="резултат")

b_9_5_44.bind('<Return>', b_9_5_44_logic)

b_9_6 = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_9_6_text1 = CTkLabel(master=sc, height=1, text="укупно садржај воде у цевима")
b_9_6_text2 = CTkLabel(master=sc, height=1, text="резултат")

b_9_6.bind('<Return>', b_9_6_logic)

b_9_7_text1 = CTkLabel(master=sc, height=1, text="обим")

b_9_7_text2 = CTkLabel(master=sc, height=1, text="површина")

b_9_7_text3 = CTkLabel(master=sc, height=1, text="фарба")

b_9_7_1_1 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_1.bind('<Return>', b_9_7_1_1_logic)

b_9_7_1_2 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_2.bind('<Return>', b_9_7_1_2_logic)

b_9_7_1_3 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_3.bind('<Return>', b_9_7_1_3_logic)

b_9_7_1_4 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_4.bind('<Return>', b_9_7_1_4_logic)

b_9_7_1_5 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_5.bind('<Return>', b_9_7_1_5_logic)

b_9_7_1_6 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_6.bind('<Return>', b_9_7_1_6_logic)

b_9_7_1_7 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_7.bind('<Return>', b_9_7_1_7_logic)

b_9_7_1_8 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_8.bind('<Return>', b_9_7_1_8_logic)

b_9_7_1_9 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_9.bind('<Return>', b_9_7_1_9_logic)

b_9_7_1_10 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_10.bind('<Return>', b_9_7_1_10_logic)

b_9_7_1_11 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_11.bind('<Return>', b_9_7_1_11_logic)

b_9_7_1_12 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_12.bind('<Return>', b_9_7_1_12_logic)

b_9_7_1_13 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_13.bind('<Return>', b_9_7_1_13_logic)

b_9_7_1_14 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_14.bind('<Return>', b_9_7_1_14_logic)

b_9_7_1_15 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_15.bind('<Return>', b_9_7_1_15_logic)

b_9_7_1_16 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_16.bind('<Return>', b_9_7_1_16_logic)

b_9_7_1_17 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_17.bind('<Return>', b_9_7_1_17_logic)

b_9_7_1_18 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_18.bind('<Return>', b_9_7_1_18_logic)

b_9_7_1_19 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_19.bind('<Return>', b_9_7_1_19_logic)

b_9_7_1_20 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_20.bind('<Return>', b_9_7_1_20_logic)

b_9_7_1_21 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_1_21.bind('<Return>', b_9_7_1_21_logic)

b_9_7_2_1 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_1.bind('<Return>', b_9_7_2_1_logic)

b_9_7_2_2 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_2.bind('<Return>', b_9_7_2_2_logic)

b_9_7_2_3 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_3.bind('<Return>', b_9_7_2_3_logic)

b_9_7_2_4 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_4.bind('<Return>', b_9_7_2_4_logic)

b_9_7_2_5 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_5.bind('<Return>', b_9_7_2_5_logic)

b_9_7_2_6 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_6.bind('<Return>', b_9_7_2_6_logic)

b_9_7_2_7 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_7.bind('<Return>', b_9_7_2_7_logic)

b_9_7_2_8 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_8.bind('<Return>', b_9_7_2_8_logic)

b_9_7_2_9 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_9.bind('<Return>', b_9_7_2_9_logic)

b_9_7_2_10 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_10.bind('<Return>', b_9_7_2_10_logic)

b_9_7_2_11 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_11.bind('<Return>', b_9_7_2_11_logic)

b_9_7_2_12 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_12.bind('<Return>', b_9_7_2_12_logic)

b_9_7_2_13 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_13.bind('<Return>', b_9_7_2_13_logic)

b_9_7_2_14 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_14.bind('<Return>', b_9_7_2_14_logic)

b_9_7_2_15 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_15.bind('<Return>', b_9_7_2_15_logic)

b_9_7_2_16 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_16.bind('<Return>', b_9_7_2_16_logic)

b_9_7_2_17 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_17.bind('<Return>', b_9_7_2_17_logic)

b_9_7_2_18 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_18.bind('<Return>', b_9_7_2_18_logic)

b_9_7_2_19 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_19.bind('<Return>', b_9_7_2_19_logic)

b_9_7_2_20 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_20.bind('<Return>', b_9_7_2_20_logic)

b_9_7_2_21 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_2_21.bind('<Return>', b_9_7_2_21_logic)

b_9_7_3_1 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_1.bind('<Return>', b_9_7_3_1_logic)

b_9_7_3_2 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_2.bind('<Return>', b_9_7_3_2_logic)

b_9_7_3_3 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_3.bind('<Return>', b_9_7_3_3_logic)

b_9_7_3_4 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_4.bind('<Return>', b_9_7_3_4_logic)

b_9_7_3_5 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_5.bind('<Return>', b_9_7_3_5_logic)

b_9_7_3_6 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_6.bind('<Return>', b_9_7_3_6_logic)

b_9_7_3_7 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_7.bind('<Return>', b_9_7_3_7_logic)

b_9_7_3_8 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_8.bind('<Return>', b_9_7_3_8_logic)

b_9_7_3_9 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_9.bind('<Return>', b_9_7_3_9_logic)

b_9_7_3_10 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_10.bind('<Return>', b_9_7_3_10_logic)

b_9_7_3_11 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_11.bind('<Return>', b_9_7_3_11_logic)

b_9_7_3_12 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_12.bind('<Return>', b_9_7_3_12_logic)

b_9_7_3_13 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_13.bind('<Return>', b_9_7_3_13_logic)

b_9_7_3_14 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_14.bind('<Return>', b_9_7_3_14_logic)

b_9_7_3_15 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_15.bind('<Return>', b_9_7_3_15_logic)

b_9_7_3_16 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_16.bind('<Return>', b_9_7_3_16_logic)

b_9_7_3_17 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_17.bind('<Return>', b_9_7_3_17_logic)

b_9_7_3_18 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_18.bind('<Return>', b_9_7_3_18_logic)

b_9_7_3_19 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_19.bind('<Return>', b_9_7_3_19_logic)

b_9_7_3_20 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_20.bind('<Return>', b_9_7_3_20_logic)

b_9_7_3_21 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_9_7_3_21.bind('<Return>', b_9_7_3_21_logic)

b_9_8 = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")

b_9_8.bind('<Return>', b_9_8_logic)

b_10 = CTkButton(master=sc, text="садржај воде у панел рад", width=12, height=25, corner_radius=0, command=b_10_clicked)
b_10.grid(row=0, column=9)

b_10_1_text = CTkLabel(master=sc, height=1, text="тип радиатора")

b_10_2_text = CTkLabel(master=sc, height=1, text="висина")

b_10_3_text = CTkLabel(master=sc, height=1, text="садржај воде по метру")

b_10_4_text = CTkLabel(master=sc, height=1, text="укупна дужина")

b_10_5_text = CTkLabel(master=sc, height=1, text="укупно воде")

b_10_1_1 = CTkLabel(master=sc, height=1, text="10")

b_10_1_2 = CTkLabel(master=sc, height=1, text="11")

b_10_1_3 = CTkLabel(master=sc, height=1, text="20")

b_10_1_4 = CTkLabel(master=sc, height=1, text="21")

b_10_1_5 = CTkLabel(master=sc, height=1, text="22")

b_10_1_6 = CTkLabel(master=sc, height=1, text="33")

b_10_2_1 = CTkLabel(master=sc, height=1, text="300")

b_10_2_2 = CTkLabel(master=sc, height=1, text="400")

b_10_2_3 = CTkLabel(master=sc, height=1, text="500")

b_10_2_4 = CTkLabel(master=sc, height=1, text="600")

b_10_2_5 = CTkLabel(master=sc, height=1, text="900")

b_10_2_6 = CTkLabel(master=sc, height=1, text="300")

b_10_2_7 = CTkLabel(master=sc, height=1, text="400")

b_10_2_8 = CTkLabel(master=sc, height=1, text="500")

b_10_2_9 = CTkLabel(master=sc, height=1, text="600")

b_10_2_10 = CTkLabel(master=sc, height=1, text="900")

b_10_2_11 = CTkLabel(master=sc, height=1, text="500")

b_10_2_12 = CTkLabel(master=sc, height=1, text="600")

b_10_2_13 = CTkLabel(master=sc, height=1, text="900")

b_10_2_14 = CTkLabel(master=sc, height=1, text="300")

b_10_2_15 = CTkLabel(master=sc, height=1, text="400")

b_10_2_16 = CTkLabel(master=sc, height=1, text="500")

b_10_2_17 = CTkLabel(master=sc, height=1, text="600")

b_10_2_18 = CTkLabel(master=sc, height=1, text="900")

b_10_2_19 = CTkLabel(master=sc, height=1, text="300")

b_10_2_20 = CTkLabel(master=sc, height=1, text="400")

b_10_2_21 = CTkLabel(master=sc, height=1, text="500")

b_10_2_22 = CTkLabel(master=sc, height=1, text="600")

b_10_2_23 = CTkLabel(master=sc, height=1, text="900")

b_10_2_24 = CTkLabel(master=sc, height=1, text="300")

b_10_2_25 = CTkLabel(master=sc, height=1, text="400")

b_10_2_26 = CTkLabel(master=sc, height=1, text="500")

b_10_2_27 = CTkLabel(master=sc, height=1, text="600")

b_10_2_28 = CTkLabel(master=sc, height=1, text="900")

b_10_3_1 = CTkLabel(master=sc, height=1, text="1.9")

b_10_3_2 = CTkLabel(master=sc, height=1, text="2.3")

b_10_3_3 = CTkLabel(master=sc, height=1, text="2.7")

b_10_3_4 = CTkLabel(master=sc, height=1, text="3.1")

b_10_3_5 = CTkLabel(master=sc, height=1, text="4.3")

b_10_3_6 = CTkLabel(master=sc, height=1, text="1.9")

b_10_3_7 = CTkLabel(master=sc, height=1, text="2.3")

b_10_3_8 = CTkLabel(master=sc, height=1, text="2.7")

b_10_3_9 = CTkLabel(master=sc, height=1, text="3.1")

b_10_3_10 = CTkLabel(master=sc, height=1, text="4.3")

b_10_3_11 = CTkLabel(master=sc, height=1, text="5.1")

b_10_3_12 = CTkLabel(master=sc, height=1, text="5.8")

b_10_3_13 = CTkLabel(master=sc, height=1, text="8.3")

b_10_3_14 = CTkLabel(master=sc, height=1, text="3.7")

b_10_3_15 = CTkLabel(master=sc, height=1, text="4.4")

b_10_3_16 = CTkLabel(master=sc, height=1, text="5.1")

b_10_3_17 = CTkLabel(master=sc, height=1, text="5.8")

b_10_3_18 = CTkLabel(master=sc, height=1, text="8.3")

b_10_3_19 = CTkLabel(master=sc, height=1, text="3.7")

b_10_3_20 = CTkLabel(master=sc, height=1, text="4.4")

b_10_3_21 = CTkLabel(master=sc, height=1, text="5.1")

b_10_3_22 = CTkLabel(master=sc, height=1, text="5.8")

b_10_3_23 = CTkLabel(master=sc, height=1, text="8.3")

b_10_3_24 = CTkLabel(master=sc, height=1, text="5.3")

b_10_3_25 = CTkLabel(master=sc, height=1, text="6.4")

b_10_3_26 = CTkLabel(master=sc, height=1, text="7.6")

b_10_3_27 = CTkLabel(master=sc, height=1, text="8.7")

b_10_3_28 = CTkLabel(master=sc, height=1, text="12.6")

b_10_4_1 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_2 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_3 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_4 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_5 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_6 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_7 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_8 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_9 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_10 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_11 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_12 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_13 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_14 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_15 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_16 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_17 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_18 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_19 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_20 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_21 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_22 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_23 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_24 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_25 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_26 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_27 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_4_28 = CTkEntry(master=sc, width=93, height=1, corner_radius=0)

b_10_5_1 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_1.bind('<Return>', b_10_5_1_logic)

b_10_5_2 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_2.bind('<Return>', b_10_5_2_logic)

b_10_5_3 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_3.bind('<Return>', b_10_5_3_logic)

b_10_5_4 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_4.bind('<Return>', b_10_5_4_logic)

b_10_5_5 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_5.bind('<Return>', b_10_5_5_logic)

b_10_5_6 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_6.bind('<Return>', b_10_5_6_logic)

b_10_5_7 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_7.bind('<Return>', b_10_5_7_logic)

b_10_5_8 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_8.bind('<Return>', b_10_5_8_logic)

b_10_5_9 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_9.bind('<Return>', b_10_5_9_logic)

b_10_5_10 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_10.bind('<Return>', b_10_5_10_logic)

b_10_5_11 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_11.bind('<Return>', b_10_5_11_logic)

b_10_5_12 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_12.bind('<Return>', b_10_5_12_logic)

b_10_5_13 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_13.bind('<Return>', b_10_5_13_logic)

b_10_5_14 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_14.bind('<Return>', b_10_5_14_logic)

b_10_5_15 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_15.bind('<Return>', b_10_5_15_logic)

b_10_5_16 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_16.bind('<Return>', b_10_5_16_logic)

b_10_5_17 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_17.bind('<Return>', b_10_5_17_logic)

b_10_5_18 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_18.bind('<Return>', b_10_5_18_logic)

b_10_5_19 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_19.bind('<Return>', b_10_5_19_logic)

b_10_5_20 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_20.bind('<Return>', b_10_5_20_logic)

b_10_5_21 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_21.bind('<Return>', b_10_5_21_logic)

b_10_5_22 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_22.bind('<Return>', b_10_5_22_logic)

b_10_5_23 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_23.bind('<Return>', b_10_5_23_logic)

b_10_5_24 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_24.bind('<Return>', b_10_5_24_logic)

b_10_5_25 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_25.bind('<Return>', b_10_5_25_logic)

b_10_5_26 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_26.bind('<Return>', b_10_5_26_logic)

b_10_5_27 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_27.bind('<Return>', b_10_5_27_logic)

b_10_5_28 = CTkEntry(master=sc, width=93, height=1, corner_radius=0, placeholder_text="резултат")

b_10_5_28.bind('<Return>', b_10_5_28_logic)

b_10_6 = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_10_6_text = CTkLabel(master=sc, text="укупно")

b_10_6.bind('<Return>', b_10_6_logic)

b_11 = CTkButton(master=sc, text="порвршина канала", width=6, height=25, corner_radius=0, command=b_11_clicked)
b_11.grid(row=0, column=10)

b_11_1_text = CTkLabel(master=sc, height=1, text="округли канали")

b_11_1_1_text = CTkLabel(master=sc, height=1, text="диаметар")

b_11_1_2_text = CTkLabel(master=sc, height=1, text="дужина")

b_11_1_3_text = CTkLabel(master=sc, height=1, text="површина")

b_11_1_1_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_1_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_2_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_1_3_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_1.bind('<Return>', b_11_1_3_1_logic)

b_11_1_3_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_2.bind('<Return>', b_11_1_3_2_logic)

b_11_1_3_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_3.bind('<Return>', b_11_1_3_3_logic)

b_11_1_3_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_4.bind('<Return>', b_11_1_3_4_logic)

b_11_1_3_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_5.bind('<Return>', b_11_1_3_5_logic)

b_11_1_3_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_6.bind('<Return>', b_11_1_3_6_logic)

b_11_1_3_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_7.bind('<Return>', b_11_1_3_7_logic)

b_11_1_3_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_8.bind('<Return>', b_11_1_3_8_logic)

b_11_1_3_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_9.bind('<Return>', b_11_1_3_9_logic)

b_11_1_3_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат")

b_11_1_3_10.bind('<Return>', b_11_1_3_10_logic)

b_11_1_4 = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_11_1_4_text = CTkLabel(master=sc, text="свега")

b_11_1_4.bind('<Return>', b_11_1_4_logic)

b_11_2_text = CTkLabel(master=sc, height=1, text="правоугални канали")

b_11_2_1_text = CTkLabel(master=sc, height=1, text="А(мм)")

b_11_2_2_text = CTkLabel(master=sc, height=1, text="В(мм)")

b_11_2_3_text = CTkLabel(master=sc, height=1, text="дужина(м)")

b_11_2_4_text = CTkLabel(master=sc, height=1, text="површина(м2)")

b_11_2_5_text = CTkLabel(master=sc, height=1, text="дебљина(мм)")

b_11_2_6_text = CTkLabel(master=sc, height=1, text="тежина(кг)")

b_11_2_1_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_11 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_12 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_13 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_14 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_15 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_16 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_17 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_18 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_19 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_20 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_21 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_22 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_1_23 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_11 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_12 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_13 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_14 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_15 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_16 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_17 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_18 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_19 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_20 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_21 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_22 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_2_23 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_11 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_12 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_13 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_14 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_15 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_16 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_17 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_18 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_19 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_20 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_21 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_22 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_3_23 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_4_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_1.bind('<Return>', b_11_2_4_1_logic)

b_11_2_4_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_2.bind('<Return>', b_11_2_4_2_logic)

b_11_2_4_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_3.bind('<Return>', b_11_2_4_3_logic)

b_11_2_4_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_4.bind('<Return>', b_11_2_4_4_logic)

b_11_2_4_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_5.bind('<Return>', b_11_2_4_5_logic)

b_11_2_4_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_6.bind('<Return>', b_11_2_4_6_logic)

b_11_2_4_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_7.bind('<Return>', b_11_2_4_7_logic)

b_11_2_4_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_8.bind('<Return>', b_11_2_4_8_logic)

b_11_2_4_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_9.bind('<Return>', b_11_2_4_9_logic)

b_11_2_4_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_10.bind('<Return>', b_11_2_4_10_logic)

b_11_2_4_11 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_11.bind('<Return>', b_11_2_4_11_logic)

b_11_2_4_12 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_12.bind('<Return>', b_11_2_4_12_logic)

b_11_2_4_13 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_13.bind('<Return>', b_11_2_4_13_logic)

b_11_2_4_14 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_14.bind('<Return>', b_11_2_4_14_logic)

b_11_2_4_15 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_15.bind('<Return>', b_11_2_4_15_logic)

b_11_2_4_16 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_16.bind('<Return>', b_11_2_4_16_logic)

b_11_2_4_17 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_17.bind('<Return>', b_11_2_4_17_logic)

b_11_2_4_18 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_18.bind('<Return>', b_11_2_4_18_logic)

b_11_2_4_19 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_19.bind('<Return>', b_11_2_4_19_logic)

b_11_2_4_20 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_20.bind('<Return>', b_11_2_4_20_logic)

b_11_2_4_21 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_21.bind('<Return>', b_11_2_4_21_logic)

b_11_2_4_22 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_22.bind('<Return>', b_11_2_4_22_logic)

b_11_2_4_23 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 1")

b_11_2_4_23.bind('<Return>', b_11_2_4_23_logic)

b_11_2_5_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_11 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_12 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_13 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_14 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_15 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_16 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_17 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_18 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_19 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_20 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_21 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_22 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_5_23 = CTkEntry(master=sc, width=94, height=1, corner_radius=0)

b_11_2_6_1 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_1.bind('<Return>', b_11_2_6_1_logic)

b_11_2_6_2 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_2.bind('<Return>', b_11_2_6_2_logic)

b_11_2_6_3 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_3.bind('<Return>', b_11_2_6_3_logic)

b_11_2_6_4 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_4.bind('<Return>', b_11_2_6_4_logic)

b_11_2_6_5 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_5.bind('<Return>', b_11_2_6_5_logic)

b_11_2_6_6 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_6.bind('<Return>', b_11_2_6_6_logic)

b_11_2_6_7 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_7.bind('<Return>', b_11_2_6_7_logic)

b_11_2_6_8 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_8.bind('<Return>', b_11_2_6_8_logic)

b_11_2_6_9 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_9.bind('<Return>', b_11_2_6_9_logic)

b_11_2_6_10 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_10.bind('<Return>', b_11_2_6_10_logic)

b_11_2_6_11 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_11.bind('<Return>', b_11_2_6_11_logic)

b_11_2_6_12 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_12.bind('<Return>', b_11_2_6_12_logic)

b_11_2_6_13 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_13.bind('<Return>', b_11_2_6_13_logic)

b_11_2_6_14 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_14.bind('<Return>', b_11_2_6_14_logic)

b_11_2_6_15 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_15.bind('<Return>', b_11_2_6_15_logic)

b_11_2_6_16 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_16.bind('<Return>', b_11_2_6_16_logic)

b_11_2_6_17 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_17.bind('<Return>', b_11_2_6_17_logic)

b_11_2_6_18 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_18.bind('<Return>', b_11_2_6_18_logic)

b_11_2_6_19 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_19.bind('<Return>', b_11_2_6_19_logic)

b_11_2_6_20 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_20.bind('<Return>', b_11_2_6_20_logic)

b_11_2_6_21 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_21.bind('<Return>', b_11_2_6_21_logic)

b_11_2_6_22 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_22.bind('<Return>', b_11_2_6_22_logic)

b_11_2_6_23 = CTkEntry(master=sc, width=94, height=1, corner_radius=0, placeholder_text="резултат 2")

b_11_2_6_23.bind('<Return>', b_11_2_6_23_logic)

b_11_2_7 = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат 1")
b_11_2_7_text1 = CTkLabel(master=sc, text="свега")
b_11_2_7_text2 = CTkLabel(master=sc, text="м2")

b_11_2_7.bind('<Return>', b_11_2_7_logic)

b_11_2_8 = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат 2")
b_11_2_8_text = CTkLabel(master=sc, text="кг")

b_11_2_8.bind('<Return>', b_11_2_8_logic)

b_12 = CTkButton(master=sc, text="спољња залузина", width=3, height=25, corner_radius=0, command=b_12_clicked)
b_12.grid(row=0, column=11)

b_12_1_firstdata = CTkEntry(master=sc, width=195, height=1)
b_12_1_firstdata_text1 = CTkLabel(master=sc, text="количина ваздуха")
b_12_1_firstdata_text2 = CTkLabel(master=sc, text="м3/ч")

b_12_1_seconddata = CTkEntry(master=sc, width=195, height=1)
b_12_1_seconddata_text1 = CTkLabel(master=sc, text="брзина у решетки")
b_12_1_seconddata_text2 = CTkLabel(master=sc, text="м/с")

b_12_1_thirddata = CTkEntry(master=sc, width=195, height=1)
b_12_1_thirddata_text = CTkLabel(master=sc, text="коефицјент решетке")

b_12_2_firstdata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_12_2_firstdata_text1 = CTkLabel(master=sc, text="поврсшина решетке")
b_12_2_firstdata_text2 = CTkLabel(master=sc, text="м2")

b_12_2_firstdata.bind('<Return>', b_12_2_1_logic)

b_12_2_seconddata = CTkEntry(master=sc, width=195, height=1)
b_12_2_seconddata_text1 = CTkLabel(master=sc, text="страна А решетке")
b_12_2_seconddata_text2 = CTkLabel(master=sc, text="мм")

b_12_3_firstdata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_12_3_firstdata_text1 = CTkLabel(master=sc, text="страна В решетке")
b_12_3_firstdata_text2 = CTkLabel(master=sc, text="мм")

b_12_3_firstdata.bind('<Return>', b_12_3_1_logic)

b_12_3_seconddata = CTkEntry(master=sc, width=195, height=1)
b_12_3_seconddata_text1 = CTkLabel(master=sc, text="страна А")
b_12_3_seconddata_text2 = CTkLabel(master=sc, text="мм")

b_12_3_thirddata = CTkEntry(master=sc, width=195, height=1)
b_12_3_thirddata_text1 = CTkLabel(master=sc, text="страна В")
b_12_3_thirddata_text2 = CTkLabel(master=sc, text="мм")

b_12_3_fourthdata = CTkEntry(master=sc, width=195, height=1, placeholder_text="резултат")
b_12_3_fourthdata_text1 = CTkLabel(master=sc, text="реална брзина на решетки")
b_12_3_fourthdata_text2 = CTkLabel(master=sc, text="м/с")

b_12_3_fourthdata.bind('<Return>', b_12_3_4_logic)

b_12_4_1_text1 = CTkLabel(master=sc,text="a")

b_12_4_1_text2 = CTkLabel(master=sc, height=1, text="b")

b_12_4_1_text3 = CTkLabel(master=sc, height=1, text="P")

b_12_4_2_text1 = CTkLabel(master=sc, text="димензије решетке")

b_12_4_2_text2 = CTkLabel(master=sc, text="живи пресек")

b_12_4_2_text3 = CTkLabel(master=sc, text="коефицијент решетке")

b_12_4_1 = CTkEntry(master=sc, width=75, height=1, corner_radius=0)

b_12_4_2 = CTkEntry(master=sc, width=75, height=1, corner_radius=0)

b_12_4_3 = CTkEntry(master=sc, width=80, height=1, corner_radius=0, placeholder_text="резултат 1")

b_12_4_3.bind('<Return>', b_12_4_3_logic)

b_12_4_4 = CTkEntry(master=sc, width=80, height=1, corner_radius=0)

b_12_4_5 = CTkEntry(master=sc, width=80, height=1, corner_radius=0, placeholder_text="резултат 2")

b_12_4_5.bind('<Return>', b_12_4_5_logic)

b_13 = CTkButton(master=sc, text="добици прозори", height=25, width=3, corner_radius=0, command=b_13_clicked)
b_13.grid(row=0, column=12)

b_13_1_text = CTkLabel(master=sc, height=1, text="добици")

b_13_1_1 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_1_1.bind('<Return>', b_13_1_1_logic)

b_13_1_2 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_1_2.bind('<Return>', b_13_1_2_logic)

b_13_1_3 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_1_3.bind('<Return>', b_13_1_3_logic)

b_13_1_4 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_1_4.bind('<Return>', b_13_1_4_logic)

b_13_2_1 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_2_1.bind('<Return>', b_13_2_1_logic)

b_13_2_2 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_2_2.bind('<Return>', b_13_2_2_logic)

b_13_2_3 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_2_3.bind('<Return>', b_13_2_3_logic)

b_13_2_4 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_2_4.bind('<Return>', b_13_2_4_logic)

b_13_3 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")
b_13_3_text1 = CTkLabel(master=sc, text="укупно")
b_13_3_text2 = CTkLabel(master=sc, text="Вт(W)")

b_13_3.bind('<Return>', b_13_3_logic)

b_13_4_text = CTkLabel(master=sc, height=1, text="површина прозора")

b_13_4_1 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_1_text = CTkLabel(master=sc, height=1, text="север")

b_13_4_2 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_2_text = CTkLabel(master=sc, height=1, text="северисток")

b_13_4_3 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_3_text = CTkLabel(master=sc, height=1, text="исток")

b_13_4_4 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_4_text = CTkLabel(master=sc, height=1, text="југоисток")

b_13_4_5 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_5_text = CTkLabel(master=sc, height=1, text="југ")

b_13_4_6 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_6_text = CTkLabel(master=sc, height=1, text="југозапад")

b_13_4_7 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_7_text = CTkLabel(master=sc, height=1, text="запад")

b_13_4_8 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)
b_13_4_8_text = CTkLabel(master=sc, height=1, text="северозапад")

b_13_5_1 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_1.bind('<Return>', b_13_5_1_logic)

b_13_5_2 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_2.bind('<Return>', b_13_5_2_logic)

b_13_5_3 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_3.bind('<Return>', b_13_5_3_logic)

b_13_5_4 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_4.bind('<Return>', b_13_5_4_logic)

b_13_5_5 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_5.bind('<Return>', b_13_5_5_logic)

b_13_5_6 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_6.bind('<Return>', b_13_5_6_logic)

b_13_5_7 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_7.bind('<Return>', b_13_5_7_logic)

b_13_5_8 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_8.bind('<Return>', b_13_5_8_logic)

b_13_5_9 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_9.bind('<Return>', b_13_5_9_logic)

b_13_5_10 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_10.bind('<Return>', b_13_5_10_logic)

b_13_5_11 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_11.bind('<Return>', b_13_5_11_logic)

b_13_5_12 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_12.bind('<Return>', b_13_5_12_logic)

b_13_5_13 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_13.bind('<Return>', b_13_5_13_logic)

b_13_5_14 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_14.bind('<Return>', b_13_5_14_logic)

b_13_5_15 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_15.bind('<Return>', b_13_5_15_logic)

b_13_5_16 = CTkEntry(master=sc, width=195, height=1, corner_radius=0, placeholder_text="резултат")

b_13_5_16.bind('<Return>', b_13_5_16_logic)

b_13_6_1 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)

b_13_6_2 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)

b_13_6_3 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)

b_13_6_4 = CTkEntry(master=sc, width=195, height=1, corner_radius=0)

clicks = 1

sc.bind('<F11>', fullscreen)

sc.bind('<Escape>', exit)

sc.mainloop()