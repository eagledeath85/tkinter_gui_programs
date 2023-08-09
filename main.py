import tkinter

def button_clicked():
    print("I got clicked!!!")
    my_label.config(text=input.get())


# Create a Tk instance (aka window)
window = tkinter.Tk()

# Adding a title to the window
window.title("My title")

# Setting a specific size to the window
window.minsize(width=500, height=300)


# LABEL
# Adding a label inside the window
my_label = tkinter.Label(text="This is a label", font=("Arial", 15, "italic"))

# To display the label onto the screen, the pack() method must be called on the my_label instance
# my_label.pack(side="top")

# Alternatively we can use either place() or grid() methods to place elements on the screen
    # place(x=int, y=int) method
my_label.place(x=43, y=145)

    # grid(column=int, row=int)
my_label.grid(column=0, row=0)

# 2 ways for changing the properties of my_label instance
    # Way 1
# my_label["text"] = "Updated text"
#     # Way 2
# my_label.config(text="This is an updated label")


# BUTTON
# Creating button
button = tkinter.Button(text="First button", command=button_clicked)
another_button = tkinter.Button(text="Second button")
# button.pack()
button.grid(column=1, row=1)
another_button.grid(column=2, row=0)


# ENTRY
# Creating a field to write text in it, and setting its width
input = tkinter.Entry(width=20)
# input.pack()
input.grid(column=3, row=2)
user_input = input.get()
print(user_input)


# Keep the window open
window.mainloop()