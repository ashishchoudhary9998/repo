import RPi.GPIO as io
import time
from time import sleep
from Tkinter import*
window=Tk()

window.title("LED ON/OFF")
window.geometry('360x480')
window.configure(background = 'blue')


io.setwarnings(False)

io.setmode(io.BOARD)

io.setup(3,io.OUT)
led=3

TRIG1=5
ECHO1=7
io.setup(TRIG1,io.OUT)
io.setup(ECHO1,io.IN)

show=Label(window,text='             ')
show.grid(column=380, row=360)

def clicked():
    
        io.output(led,False)      
             
        sleep(1)

        window.configure(background = 'black')
        window.title("LED OFF")
def clicked1():
    
        io.output(led,True)      
             
        sleep(1)        

        window.configure(background = 'white')
        window.title("LED ON")

def ultra():
        io.output(TRIG1,False)
        sleep(0.2)

        io.output(TRIG1,True)
        sleep(0.00001)

        io.output(TRIG1,False)

        while io.input(ECHO1)==0:
            pulse_start=time.time()

        while io.input(ECHO1)==1:
            pulse_end=time.time()

        t1=pulse_end-pulse_start

        d= t1 * 17150
        d=round(d,2)

        return str(d)

def clicked2():        
        q=ultra()
        
        show.configure(text=q + "cm")

    
btn = Button(window, text="LED OFF", bg = "silver", command=clicked)
btn.grid(column=2, row=2)

btn = Button(window, text="LED ON", bg = "gold", command=clicked1)
btn.grid(column=4, row=2)

btn = Button(window, text="Enter", bg = "#2196F3", command=clicked2)
btn.grid(column=36, row=360)

            

window.mainloop()