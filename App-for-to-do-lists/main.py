from tkinter import Tk,Label,Entry,Button,font,END

window=Tk()
window.title("To-Do List")
window.minsize(height=200, width=300)
window.config(padx=20, pady=20)

title_label=Label(text="To-Do List", font=("Arial", 24, "bold"))
title_label.grid(row=0, column=1)

task_entry=Entry(width=30)
task_entry.grid(row=1, column=0, columnspan=2)
task_entry.focus()
def mark_task_done(task_label):
    font_style=font.Font(family=task_label,overstrike=True)
    task_label.config(font=font_style)

def remove_task(task_label, check_button, remove_button):
    task_label.destroy()
    check_button.destroy()
    remove_button.destroy()
    task_entry.delete(0, END)
def add_task():
    task=task_entry.get()
    task_label=Label(text=task)
    task_label.grid(row=2, column=0)
    check_button=Button(text="✓", command=lambda: mark_task_done(task_label))
    check_button.grid(row=2, column=1)
    remove_button=Button(text="X", command=lambda: remove_task(task_label,check_button,remove_button))
    remove_button.grid(row=2, column=2)
add_task_button=Button(text="Add Task", width=15, command=add_task)
add_task_button.grid(row=1,column=2)


window.mainloop()

