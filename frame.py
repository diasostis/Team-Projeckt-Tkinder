import tkinter
from tkinter import BOTH






root = tkinter.Tk()
root.title('Titanic')
root.iconbitmap
root.geometry('500x500')
#
#frames
name_label = tkinter.Label(root, text ='Pdf Data')
name_label.pack()
name_button = tkinter.Button(root, text='Press for Data')
name_button.grid(row=0, column=1)

#define frame
pack_frame = tkinter.Frame(root, bg='red')
gris_frame_1 = tkinter.Frame(root, bg='blue')
gris_frame_2 = tkinter.Frame(root, text='Grid system', borderwidth=5)

#pack frames into root
pack_frame.pack(fill=BOTH, expand=True)
gris_frame_1.pack(fill=BOTH, expand=True)
gris_frame_2.pack(fill=BOTH, expand=True)

#
tkinter.Label(pack_frame, text="text").pack()



#
root.mainloop()