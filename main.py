from tkinter import *

window = Tk()
window.title("℃ to℉ converter")
window.config(padx=50, pady=50)

my_label = Label(text="℃", font=("Futura", 15, "bold"))
my_label.grid(column=2, row=0,padx=10, pady=10)

to_f = Label(text="is equal to", font=("Futura", 20, "bold"))
to_f.grid(column=0, row=1,padx=10, pady=10)


input_f = Label(text="0", font=("Futura", 30, "bold"))
input_f.grid(column=1, row=1,padx=10, pady=10)

num_c = Label(text="℉", font=("Futura", 20, "bold"))
num_c.grid(column=2, row=1,padx=10, pady=10)

#input
input_c = Entry(width=10)
input_c.grid(row=0, column=1,padx=10, pady=10)

#button
def encode():
    temp_c = int(input_c.get())
    temp_f = temp_c * 1.8 + 32
    input_f.config(text=temp_f)

button = Button(text="℉ is...", command=encode)
button.grid(column=1, row=2,padx=10, pady=10)
window.mainloop()

