from threading import Thread
from time import sleep

def Flow1():
    for i in range(10, 0, -1):
        print(f'Из первого потока: {i}')
        sleep(1)
        
def Flow2():
    for i in range(10, 0, -1):
        print(f'Из второго потока: {i}')
        sleep(1)
        
flow1= Thread(target=Flow1)
print(f"thread status: {flow1.is_alive()}")
flow1.start()
print(f"thread status: {flow1.is_alive()}")
flow1.join()
flow2= Thread(target=Flow2)
print(f"thread status: {flow2.is_alive()}")
flow2.start()
print(f"thread status: {flow2.is_alive()}")
flow2.join()
sleep(2)
print(f"thread status: {flow2.is_alive()}")

       

        

