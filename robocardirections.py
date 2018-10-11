
# coding: utf-8

# In[ ]:


import RPi.GPIO as io

io.setwarnings(False)

io.setmode(io.BOARD)

Motor_INPUT1 = 3
Motor_INPUT2 = 5



Port1 = 7          #L293D First Input
Port2 = 8          #L293D Second Input    
Port3 = 10         #L293D Third Input
Port4 = 11         #L293D Fourth Input


io.setup(Motor_INPUT1,io.IN)
io.setup(Motor_INPUT2,io.IN)


io.setup(Port1,io.OUT)
io.setup(Port2,io.OUT)
io.setup(Port3,io.OUT)
io.setup(Port4,io.OUT)

while True:

        c = io.input(Motor_INPUT1)
        d = io.input(Motor_INPUT2)
       
        print c
        
        print d
        
       
        
        if c==0 and d==1:
            io.output(Port1,True)
            io.output(Port2,False)
            io.output(Port3,False)
            io.output(Port4,False)
           
            print 'cd',c ,d 
            print 'Right'
                         
        if c==1 and d==0:
            io.output(Port1,False)
            io.output(Port2,False)
            io.output(Port3,True)
            io.output(Port4,False)
            
            print "cd", c ,d 
            print 'Left'

            

            
                                       

