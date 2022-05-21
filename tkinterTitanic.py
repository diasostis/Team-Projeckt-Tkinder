#first window
import tkinter
from tkinter import BOTH
from unicodedata import name
root = tkinter.Tk()
root.title('Titanic')
root.iconbitmap = ('ship.ico')
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = 'grey')

#create widget
name_button = tkinter.Button(root, text = 'Data Pdf', bg='black', fg='white', borderwidth=5, activebackground='red')
name_button.pack()
name_button.config()
name_button_2 = tkinter.Button(root, text = 'Analyze Data', bg='black', fg='white', borderwidth=5, activebackground='red', font=('Arial', 18, 'bold'))
name_button_2.pack()

name_button_3 = tkinter.Button(root, text = 'Score', bg='black', fg='white', borderwidth=5, activebackground='red', font=('Arial', 22, 'bold'))
name_button_3.pack(padx = 10, pady = 50)

name_label_4 = tkinter.Label(root, text = 'We hope you liked our work', font =('Arial', 14, 'bold'), bg = 'green')
name_label_4.pack(pady = (0,10), ipadx = 50, ipady= 10 , anchor='n')

name_label_5 = tkinter.Label(root, text = "Developers, Triantafillidis Apostolos, Vasilis Verras, George", font = ('Arial', 10), bg = 'blue')
name_label_5.pack(fill = BOTH, expand = True, padx = 10, pady = 10)

root.mainloop()