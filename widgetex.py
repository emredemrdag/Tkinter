from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

#label
label = Label(text="my label")
label.config(bg="black")
label.config(fg="red")
label.config(padx=10, pady=10)
label.pack()

#button
def button_click():
    print("button clicked")
    print(text.get("1.0", END))
    # 1.0 -> 1-> line , 0-> character

buton = Button(text="button", command=button_click)
buton.config(padx=10, pady=10)
buton.pack()

#entry
entry = Entry(width=20)
entry.pack()

#multiline text
text = Text(width=30, height=10)
text.focus()
text.pack()

#scale
def scale_selected(value):
    print(value)
scale = Scale(from_=0, to=50, command=scale_selected)
scale.pack()

#spinbox
def spinbox_selected():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
checkbutton = Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
checkbutton.pack()

#radio button
def radio_selected():
    print(radio_check_state.get())
radio_check_state = IntVar()
radiobutton = Radiobutton(text="1. option", value=10, variable=radio_check_state, command=radio_selected)
radiobutton_2 = Radiobutton(text="2. option", value=20, variable=radio_check_state, command=radio_selected)
radiobutton.pack()
radiobutton_2.pack()

#listbox
def listbox_selected(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox()
name_list = ["aaaa", "bbbb", "cccc", "dddd","eeee"]
for i in range(len(name_list)):
    listbox.insert(i, name_list[i])
listbox.bind('<<ListboxSelect>>', listbox_selected)
listbox.pack()

window.mainloop()