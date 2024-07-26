from tkinter import *
from tkinter import messagebox
import random

me = Tk()
global a, life
me.geometry("354x640")

textin = StringVar()
life_left = StringVar()

def restart1():
    messagebox.showerror("showinfo","There is a number hidden in this game you need to find in 10 chance") 
    global a
    a = random.randint(1, 100)
    global life
    life = 10
    life_left.set(life)
    textin.set("Find no. 1 to 100")
    butlife = Button(me,
                     padx=-6,
                     pady=4,
                     bd=4,
                     bg='white',
                     text="Chance is",
                     font=("Courier New", 16, 'bold'))
    butlife.place(x=75, y=310)



me.title("made by Er.Mayur Mahajan")

melabel = Label(me,
                text="Find the Number",
                bg='dark gray',
                font=("Times", 20, 'bold'))

melabel.pack(side=TOP)

me.config(background='Dark gray')
operator = ""


def clickbut(number):
    global operator, life
    operator = operator + str(number)

    textin.set(operator)


def questions():
    answer = messagebox.askquestion("askquestion", "You want to play again?")
    if answer == "yes":
        restart1()
    else:
        Close()


def Start():
    try:
        global life

        life = life - 1
        life_left.set(life)
        b = int(operator)
        print(a)
        if b == a:
            textin.set("Win_Correct Number")
            questions()

        elif life == 0 or life < 0:
            textin.set("You loss")
            life_left.set(b)
            butlife = Button(me,
                             padx=-6,
                             pady=4,
                             bd=4,
                             bg='white',
                             text="Number is",
                             font=("Courier New", 16, 'bold'))
            butlife.place(x=75, y=310)
            questions()

        elif b < a:
            textin.set("Is Small")
            print("Your chance left", life)

        elif b > a:
            textin.set("Is Big")
            print("Your chance left", life)

    except:
        messagebox.showerror("Empty","Enter Number")


def clrbut():
    textin.set('')
    global operator
    operator = ''


metext = Entry(me,
               font=("Courier New", 20, 'bold'),
               textvar=textin,
               width=25,
               bd=5,
               bg='powder blue')
metext.pack()

melife = Entry(me,
               font=("Courier New", 20, 'bold'),
               textvar=life_left,
               width=2,
               bd=5,
               bg='powder blue')
melife.pack()
melife.place(x=205, y=310)


def equlbut():
    Start()
    global operator
    operator = ''


but1 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(1),
              text="1",
              font=("Courier New", 16, 'bold'))

but1.place(x=10, y=100)

but2 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(2),
              text="2",
              font=("Courier New", 16, 'bold'))

but2.place(x=10, y=170)

but3 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(3),
              text="3",
              font=("Courier New", 16, 'bold'))

but3.place(x=10, y=240)

but4 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(4),
              text="4",
              font=("Courier New", 16, 'bold'))

but4.place(x=75, y=100)

but5 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(5),
              text="5",
              font=("Courier New", 16, 'bold'))

but5.place(x=75, y=170)

but6 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(6),
              text="6",
              font=("Courier New", 16, 'bold'))

but6.place(x=75, y=240)

but7 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(7),
              text="7",
              font=("Courier New", 16, 'bold'))

but7.place(x=140, y=100)

but8 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(8),
              text="8",
              font=("Courier New", 16, 'bold'))

but8.place(x=140, y=170)

but9 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(9),
              text="9",
              font=("Courier New", 16, 'bold'))

but9.place(x=140, y=240)

but0 = Button(me,
              padx=14,
              pady=14,
              bd=4,
              bg='white',
              command=lambda: clickbut(0),
              text="0",
              font=("Courier New", 16, 'bold'))

but0.place(x=10, y=310)

butclear = Button(me,
                  padx=14,
                  pady=119,
                  bd=4,
                  bg='white',
                  text="CE",
                  command=clrbut,
                  font=("Courier New", 16, 'bold'))

butclear.place(x=270, y=100)

butequal = Button(me,
                  padx=125,
                  pady=14,
                  bd=4,
                  bg='white',
                  command=equlbut,
                  text="ENTER",
                  font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=380)

restart_button = Button(me, text="Restart", command=restart1)

restart_button.pack(pady=400)
restart_button.pack(padx=200)
restart_button.place(x=200, y=150)


#exit button
def Close():
    me.destroy()


exit_button = Button(me, text="Exit", command=Close)

exit_button.pack(pady=400)
exit_button.pack(padx=400)
exit_button.place(x=205, y=100)
restart1()
me.mainloop()