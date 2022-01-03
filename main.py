# An App with buttons ToDoList App.
# by Yara ElSakka.
# 31.12.21: initial draft.
# 03.01.22: updated code.
# HOMEWORK NOTES:
# https://harmonious-motion-f4e.notion.site/TKINTER-HOMEWORK-61283a502faf466e94405262b23dfa93
# HOMEWORK Video in:
# https://www.icloud.com/iclouddrive/0b5Ry5qZvDaUzg4ns_jf_EtVA#Homework

from tkinter import *

# Program functions:
# function for (add todolist button):
def addTodofunc():
    print("Add todo button is pressed!")
    thereisText = inputBox.get()
    if thereisText != "":
        listBox.insert(END, thereisText)
    else:
        print("Please enter Text First! Thank You ..")

# function for (delete todolist button):
def deleteTodofunc():
    print("delete todo button is pressed!")
    listBox.delete(ANCHOR)

# Start App screen (window):
programScreen = Tk()
programScreen.title("Yara Todo List App 2022")
programScreen.geometry("600x500")
programScreen.resizable(0, 0)
programScreen.config(bg="#DB6B97")  # Configuration
# End App screen (window).

# BUTTON WIDGET (close button):
buttonClose = Button(text = "close program", command = programScreen.destroy)
# NEW *** use pady for padding (adding widgets to the window using .pack()
buttonClose.pack(pady = 40)

# HOMEWORK: TODO please use the PDF for help
# 3. Create a listbox to display the todo list
listBox = Listbox()
listBox.pack(pady = 20)

# 4. Create an input field to add todo
inputBox = Entry()
inputBox.pack(pady = 20)

# 1. Create a addTodo button
buttonAddtodo = Button(text = "Add ToDo List", command = addTodofunc)
buttonAddtodo.pack(pady = 20)

# 2. Create a deleteTodo button
buttonDeletetodo = Button(text = "Delete ToDo List", command = deleteTodofunc)
buttonDeletetodo.pack(pady = 5)

mainloop()
# end of code.
# 03.01.22