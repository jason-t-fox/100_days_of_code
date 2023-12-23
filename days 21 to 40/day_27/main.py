import tkinter

window = tkinter.Tk()
window.title("Mile to Km")
window.config(padx=20, pady=20)


# window.minsize(width=400, height=200)

def cal_km():
    input_value = input_box.get()
    km_calc_value = f"{float(input_value) / 0.62137119:.2f}"
    Km_calc_label["text"] = km_calc_value

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=2, column=3)

Km_label = tkinter.Label(text="Km")
Km_label.grid(row=3, column=3)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row=3, column=1)

Km_calc_label = tkinter.Label(text="0")
Km_calc_label.grid(row=3, column=2)

calculate_button = tkinter.Button(text="Calculate", command=cal_km)
calculate_button.grid(row=4, column=2)

input_box = tkinter.Entry()
input_box.grid(row=2, column=2)

window.mainloop()
