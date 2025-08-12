from tkinter import *
import math

#constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

#functions
def start_timer():
    global reps
    reps += 1
    work_sec= WORK_MIN * 60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_sec=LONG_BREAK_MIN * 60
    if reps%2!=0:
        count_down(work_sec) #green
        text.config(text="Work",fg=GREEN)
    elif reps%2==0 and reps%8!=0:
        count_down(short_break_sec)#pink
        text.config(text="Break",fg=PINK)
    elif reps%8==0:
        count_down(long_break_sec)#red
        text.config(text="Break",fg=RED)

def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=''
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        check_mark.config(text=marks)

def reset_timer():
    global reps
    reps=0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text='Timer',fg=GREEN)
    check_mark.config(text='')



window=Tk()
window.title("Pomodoro App")
window.config(padx=200, pady=100,bg=YELLOW)

canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

text=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 50, "bold"))
text.grid(column=1, row=0)
check_mark=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,18))
check_mark.grid(column=1, row=3)

start_button=Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(column=0, row=2)
reset_button=Button(text="reset",command=reset_timer,highlightthickness=0)
reset_button.grid(column=2,row=2)

window.mainloop()
