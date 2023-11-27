from threading import Thread
from time import sleep

def Flow(thread_name):
    ###todo. Сообщение, что старт потока 1.
    for i in range(10, 0, -1):
        print(f'Из первого потока: {i}')
        sleep(1)
        ###todo. Сообщение конца потока 1.
       
    for i in range(10, 0, -1):
        print(f'Из второго потока: {i}')
        sleep(1)  
         ###todo. Сообщение конца потока 2.
### Формирование задач для запуска в параллель.

flow1= Thread(target=Flow, args=(1, ))                    
flow2= Thread(target=Flow, args=(2,))

###Запуск потоков.
flow1.start()
sleep(2.1)
print(f"thread status: {flow1.is_alive()}")
flow2.start()
print(f"thread status: {flow2.is_alive()}")
###Объединение потоков
flow1.join()
flow2.join()
print(f"thread status: {flow1.is_alive()}")
print(f"thread status: {flow2.is_alive()}")

###todo Сообщение, что все потоки завершились.

       

        

