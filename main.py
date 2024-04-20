import tkinter

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=500, height=300)

def click_button():
    user_input = my_entry.get()
    print(user_input)


#label
my_label = tkinter.Label(text="this is a label", font=('Arial', 20, "italic"))
my_label.config(bg="white", fg="black")
#my_label.pack()
my_label.grid(row=0, column=1)

#button
my_button = tkinter.Button(text="this is a button", command=click_button)
#my_button.pack()
my_button.grid(row=1, column=2)

#entry
my_entry = tkinter.Entry(width=50)
#my_entry.pack()
my_entry.grid(row=2, column=3)


window.mainloop()

