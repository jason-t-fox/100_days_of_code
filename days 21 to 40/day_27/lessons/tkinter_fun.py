import tkinter
# from time import sleep

window = tkinter.Tk()
window.title("I am a title!")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="label1", font=("Ariel", 24, "bold"))
my_label["text"] = "new text"

input_field = tkinter.Entry(width=10)


def button_clicked():
    my_label["text"] = input_field.get()


button1 = tkinter.Button(text="click me", command=button_clicked)


my_label.pack()
button1.pack()
input_field.pack()

window.mainloop()
