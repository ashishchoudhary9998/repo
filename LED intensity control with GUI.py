from Tkinter import *
window = Tk()
import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                    #calling time to provide delays in program
from time import sleep
IO.setwarnings(False)           #do not show any warnings
IO.setmode (IO.BOARD)    
IO.setup(3,IO.OUT)           # initialize GPIO3 as an output.
p = IO.PWM(3,100)          #GPIO3 as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle

window.title("PWM BULB")
window.geometry('360x480')
window.configure(background = 'blue')

def bulb1():
    p.ChangeDutyCycle(0)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)
def bulb2():
    p.ChangeDutyCycle(10)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)
def bulb3():
    p.ChangeDutyCycle(25)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)
def bulb4():
    p.ChangeDutyCycle(40)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)
def bulb5():
    p.ChangeDutyCycle(50)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)
def bulb6():
    p.ChangeDutyCycle(65)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)
def bulb7():
    p.ChangeDutyCycle(80)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)
def bulb8():
    p.ChangeDutyCycle(100)               #change duty cycle for varying the brightness of LED.
    time.sleep(0.1)

btn = Button(window, text="0", bg = "#2196F3", command=bulb1)
btn.grid(column=36, row=360)
btn = Button(window, text="1", bg = "#2196F3", command=bulb2)
btn.grid(column=36, row=361)
btn = Button(window, text="2", bg = "#2196F3", command=bulb3)
btn.grid(column=36, row=362)
btn = Button(window, text="3", bg = "#2196F3", command=bulb4)
btn.grid(column=36, row=363)
btn = Button(window, text="4", bg = "#2196F3", command=bulb5)
btn.grid(column=36, row=364)
btn = Button(window, text="5", bg = "#2196F3", command=bulb6)
btn.grid(column=36, row=365)
btn = Button(window, text="6", bg = "#2196F3", command=bulb7)
btn.grid(column=36, row=366)
btn = Button(window, text="7", bg = "#2196F3", command=bulb8)
btn.grid(column=36, row=367)


window.mainloop()
