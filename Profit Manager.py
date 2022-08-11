# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:00:05 2022

@author: PC_RC
"""

from tkinter import *
root = Tk()

root.title("Profit Manager")
root.geometry("500x500")
root.configure(background="yellow")

month = Label(root)
month_tuple = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profit = Label(root)
profit_tuple = (23984, 74653, 12534, 20000, 34000, 45100, 97080, 12000, 67900, 56700, 34100, 78461)
max_profit_label = Label(root)
min_profit_label = Label(root)


month["text"] = month_tuple
profit = profit_tuple

def maximum_profit():
    max_profit = max(profit_tuple)
    max_profit_index = profit_tuple.index(max_profit)
    print(max_profit_index)

    max_profit_month = month_tuple[max_profit_index]
    print("The max profit of "+ str(max_profit)+ " was recorded in the month of "+ str(max_profit_month))
    max_profit_label["text"] = "The maximum profit of "+ str(max_profit)+ " was recorded in the month of "+ str(max_profit_month)
    

def minimum_profit():
    min_profit = min(profit_tuple)
    min_profit_index = profit_tuple.index(min_profit)
    print(min_profit_index)

    min_profit_month = month_tuple[min_profit_index]
    print("The min profit of "+ str(min_profit)+ " was recorded in the month of "+ str(min_profit_month))
    min_profit_label["text"] = "The minimum profit of "+ str(min_profit)+ " was recorded in the month of "+ str(min_profit_month)
    
btn_max = Button(root)    
btn_max = Button(root, text=" Show Max Profitable Month ", fg="blue", command = maximum_profit)
btn_min = Button(root)
btn_min = Button(root, text=" Show Min Profitable Month ", fg="blue", command = minimum_profit)
month.place(relx = 0.5, rely = 0.3, anchor = CENTER)
profit.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn_max.place(relx = 0.5, rely = 0.7, anchor = CENTER)
max_profit_label.place(relx = 0.5, rely = 0.8, anchor = CENTER)
btn_min.place(relx = 0.5, rely = 0.9, anchor = CENTER)
btn_min.place(relx = 0.5, rely = 0.10, anchor = CENTER)

root.mainloop()
