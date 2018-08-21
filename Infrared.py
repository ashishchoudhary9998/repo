
# coding: utf-8

# In[ ]:


import RPi.GPIO as io

io.setwarnings(False)

io.setmode(io.BOARD)

IR_INPUT = 12
Led = 18

io.setup(IR_INPUT,io.IN)
io.setup(Led,io.OUT)
while True:

    c = io.input(IR_INPUT)
    if(c==1):
        io.output(Led,True)
        print c       
                 
    elif(c==0):
        io.output(Led,False)
        print c
                            
                                   

