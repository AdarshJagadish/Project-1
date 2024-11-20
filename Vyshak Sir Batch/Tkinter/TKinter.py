import tkinter
win=tkinter.Tk()
win.title('Synnefo')
win.geometry=('200*200')
win.maxsize(400,400)
win.minsize(100,100)
win.config(background='aqua')

#Label Positioning
l1=tkinter.Label(win,text="Welcome")
l1.pack()
# l1.place(x=20,y=30)
# l1.grid(row=2,column=3)
l1.config(background='Red')
win.mainloop()