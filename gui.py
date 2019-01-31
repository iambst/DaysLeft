from tkinter import *

days = 90
my_window = Tk()
w = 150
h = 75
x = 1375
y = 675
# use width x height + x_offset + y_offset (no spaces!)
my_window.geometry("%dx%d+%d+%d" % (w, h, x, y))

label = Label(my_window,bg='bisque', text=str(days)+" days", bd=1,relief="solid", font="Times 24", width=15, height=4)
label.pack()
my_window.configure(bg='dark orange')
my_window.overrideredirect(True)
my_window.mainloop()
