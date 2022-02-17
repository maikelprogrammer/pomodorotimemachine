from tkinter import *
import math
import pyttsx3

PINK="#BB6464"
LIGHT_GREEN= "#C1DEAE"
GRAY="#524A4E"
SKYBLUE="#54BAB9"
WORK_TIME=25
SHORT_BREAK=5
LONG_BREAK=20
reps=0
timer=None

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text="00:00")
    text_label.config(text="TIMER")
    tick_label.config(text="")
    global reps
    reps=0


def  start():
    global reps
    reps+=1
    work_minute=WORK_TIME*60
    short_minute=SHORT_BREAK*60
    long_minute=LONG_BREAK*60

    if reps>8:
        pyttsx3.speak("hey jonathan your pomodoro technique is over.have a good day")
        window.after_cancel(timer)

    elif reps %8==0:
        pyttsx3.speak("hey jonathan ,take a long break")
        time_set(long_minute)
        text_label.config(text="LONG BREAK",font=("courier",50,"bold"),fg="red")

    elif reps%2==0:
        pyttsx3.speak("hey jonathan take a short break")
        time_set(short_minute)
        text_label.config(text="SHORT BREAK", font=("courier", 50, "bold"),fg=PINK)

    else:
        pyttsx3.speak("hey jonathan your work time is begin,start doing work.")
        time_set(work_minute)
        text_label.config(text="WORK TIME", font=("courier", 50, "bold"),fg=GRAY)



def time_set(count):
    minutes=math.floor(count/60)
    secs=count%60

    if secs<10:
        secs=f"0{secs}"
    canvas.itemconfig(canvas_text,text=f"{minutes}:{secs}")
    if count >0:
        global timer
        timer=window.after(1000,time_set,count-1)
    else:
        start()
        work=""
        tick_1=math.floor(reps/2)
        for i in range(tick_1):
            work+="✔"
        tick_label.config(text=work)

window=Tk()
window.title("POMODORO TIME TECHNIQUE")
window.config(padx=100,pady=50,bg=LIGHT_GREEN)

text_label=Label(text="TIMER",font=("courier",50,"bold"),bg=LIGHT_GREEN,fg=SKYBLUE)
text_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=LIGHT_GREEN,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas_text=canvas.create_text(106,130,text="00:00",fill="white",font=("courier",30,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="START",font=(20),command=start)
start_button.grid(column=0,row=2)

reset_button=Button(text="RESET",font=(20),command=reset)
reset_button.grid(column=2,row=2)

tick_label=Label(bg=LIGHT_GREEN,fg="red",font=(50))
tick_label.grid(column=1,row=3)

window.mainloop()
