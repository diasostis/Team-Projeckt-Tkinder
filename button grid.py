import tkinter

root = tkinter.Tk()
root.title('Titanic')
root.geometry('500x500')
root.resizable(0,0)

name_button = tkinter.Button(root, text = "Data Pdf file", bg='black', fg='white', borderwidth=5, activebackground='red')
name_button.grid(row=0, column=0, columnspan=2, )
time_button = tkinter.Button(root, text='Data Analysis', bg='black', fg='white', borderwidth=5, activebackground='red')
time_button.grid(row=1, column=0, columnspan=2, padx= 10, pady=10, ipadx=15)
place_button = tkinter.Button(root, text='Score', bg='black', fg='white', borderwidth=5, activebackground='red')
place_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=15)

root.mainloop()