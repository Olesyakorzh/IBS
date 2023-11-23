"""
import threading
import time

def clock(interval):
    while True:
        print(f'Time: {time.ctime()}')
        time.sleep(interval)
t = threading.Thread(target=clock, args=(5,))
t.daemon = True
t.start()
t.join()
""" 
import threading
import time

class ClockThread(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval
        
    def run(self):
        while True:
            print(f'Time: {time.ctime()}')
            time.sleep(self.interval)
            
t = ClockThread(5)
t.start()
t.join()


