'''
mouse=Controller()

print(mouse.position)

#mouse.position=(150,-300)

def autos(horizontal,vertical):   
    mouse.position=(horizontal,vertical)
autos(150,300)
'''



from pynput.mouse import Button, Controller
import random
import threading
mouse=Controller()


def autos():
    
    horizontal=random.choice([150,100,50,180,160,190])
    vertical=random.choice([200,150,300])

    mouse.position=(horizontal,vertical)
    print(mouse.position)
autos()



def excet():
    mouse.position=(200,200)
    mouse.position=(180,200)
    mouse.click(Button.right,2)
    mouse.click(Button.right,2)

    autos()
    print("Final Call")

def times():
    
    
    timer=threading.Timer(280.0,excet)
    timer.start()
    
times()



