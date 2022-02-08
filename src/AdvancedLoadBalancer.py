from LoadBalancer import LoadBalancer
import threading
import time
import heapq
from datetime import datetime, timedelta
from random import random 
from random import seed
seed(42)


class AdvancedLoadBalancer(LoadBalancer):
    def __init__(self, servers):
        super().__init__(servers) 
        self.lock = threading.Lock()
        self.load = [0 for _ in servers]
        self.queue = []
        releasor = threading.Thread(target = self.clean_requests)
        releasor.setDaemon(True)
        releasor.start()

    
    def update_counter(self, server, load):
        self.lock.acquire()
        self.load[server] += load
        self.lock.release()


    def send_request(self):
        server = self.load.index(min(self.load))
        release_time = datetime.now() + timedelta(seconds=random() * 9 + 1)
        heapq.heappush(self.queue, (release_time, server))
        self.update_counter(server, 1)
        return self.servers[server]


    def clean_requests(self):
        while True:
            if self.queue and self.queue[0][0] < datetime.now():
                self.update_counter(heapq.heappop(self.queue)[1], -1)