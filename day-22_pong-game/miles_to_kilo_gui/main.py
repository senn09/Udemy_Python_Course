from tkinter import *

window = Tk()
window.minsize(width=300,height=300)
window.title("Mile to Km Converter")

miles_label = Label(text="miles")
miles_label.grid(row= 0, column=2)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row= 1, column=0)

miles_entry = Entry(width=20)
miles_entry.grid(row=0, column=1)

calc_km_label = Label()
calc_km_label.grid(row=1, column=1)

def calc_km():
    miles =  float(miles_entry.get())
    new_km = (miles * 1.609).__round__()
    calc_km_label.config(text=new_km)

calc_button = Button(text="go fuck yourself", command=calc_km)
calc_button.grid(row=2, column=1)

window.mainloop()