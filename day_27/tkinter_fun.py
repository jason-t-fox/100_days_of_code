import tkinter

window = tkinter.Tk()
window.title("I am a title!")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="label1", font=("Ariel", 24, "bold"))
other_label = tkinter.Label(text="label2", font=("Ariel", 24, "bold"))
my_label.pack(side="left")
other_label.pack(side="left")

window.mainloop()
