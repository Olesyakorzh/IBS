import threading
from urllib.request import urlopen

class WorkerThread(threading.Thread):
    def __init__(self, url_list, url_list_lock):
        super().__init__()
        self.url_list = url_list
        self.url_list_lock = url_list_lock
        
    def run(self):
        while True:
            next_url = self.grab_next_url()
            if next_url==None: break
            self.retrieve_url(next_url) 
            
    def grab_next_url(self):
        self.url_list_lock.acquire(True)
        if len(self.url_list)<1:
            next_url=None
        else:
            next_url=self.url_list[0]
            del self.url_list[0]
        self.url_list_lock.release()
        return next_url
    
    def retrieve_url(self, next_url):
        text=urlopen(next_url).read()
        print(f'{next_url}: {text}')
        
url_list=['http://linux.org.ru', 'http://kernel.org', 'http://python.org']
url_list_lock = threading.Lock()
worc_list=[]
for x in range(0, 3):
    new_t = WorkerThread(url_list, url_list_lock)
    worc_list.append(new_t)
    new_t.start()
    new_t.join()
    
         