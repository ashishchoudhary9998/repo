import RPi.GPIO as io
from Tkinter import *

window = Tk()

io.setwarnings(False)

io.setmode(io.BOARD)

window.title("motor")
window.geometry('360x480')
window.configure(background = 'blue')

Motor_INPUT1 = 3
Motor_INPUT2 = 5



Port1 = 7          #L293D First Input
Port2 = 8          #L293D Second Input    
Port3 = 10         #L293D Third Input
Port4 = 11         #L293D Fourth Input





io.setup(Port1,io.OUT)
io.setup(Port2,io.OUT)
io.setup(Port3,io.OUT)
io.setup(Port4,io.OUT)


def forward():       
        
    io.output(Port1,True)
    io.output(Port2,False)
    io.output(Port3,True)
    io.output(Port4,False)
           
            
def reverse():            
                         
    
    io.output(Port1,False)
    io.output(Port2,True)
    io.output(Port3,False)
    io.output(Port4,True)
            
            
def stop():

    
    io.output(Port1,False)
    io.output(Port2,False)
    io.output(Port3,False)
    io.output(Port4,False)

           
           

                                       
btn = Button(window, text="forward", bg = "#2196F3", command=forward)
btn.grid(column=36, row=360)
btn = Button(window, text="reverse", bg = "#2196F3", command=reverse)
btn.grid(column=36, row=361)
btn = Button(window, text="stop", bg = "#2196F3", command=stop)
btn.grid(column=36, row=362)


window.mainloop()
