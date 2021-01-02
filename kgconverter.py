from tkinter import *

window = Tk()

# Functions
def all_functions():

    gram_conv = int(enter_kg_value.get()) * 1000
    grams_result.insert(END, str(gram_conv) + ' grams' )

    gram_conv = int(enter_kg_value.get()) * 2.20
    pounds_result.insert(END, str(gram_conv) + ' pounds' )

    gram_conv = int(enter_kg_value.get()) * 35.27
    ounces_result.insert(END, str(gram_conv) + ' ounces' )
    



# Row 0 Widgets

cell_title = Label(window, text = 'Enter Kg')
cell_title.grid(row = 0, column = 0)

enter_kg_value = StringVar()
enter_kg = Entry(window, textvariable = enter_kg_value)
enter_kg.grid(row = 0, column = 1)

convert_button = Button(window, text = 'Convert', command = all_functions)
convert_button.grid(row = 0, column = 2)

# Row 1 Widgets - Answers(output)

grams_result = Text(window, height = 1, width = 20, borderwidth = 5)
grams_result.grid(row = 1, column = 0)

pounds_result = Text(window, height = 1, width = 20, borderwidth = 5)
pounds_result.grid(row = 1, column = 1)

ounces_result = Text(window, height = 1, width = 26, borderwidth = 5)
ounces_result.grid(row = 1, column = 2)

window.mainloop()