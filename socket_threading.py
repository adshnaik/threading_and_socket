import threading
import socket
from queue import Queue 


print_lock = threading.Lock()
target = "pythonprogramming.net"

def portscan(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print("port: ",port," is open")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(1,30):
    t = threading.Thread(target=threader)
    t.deamon = True
    t.start()
    
for worker in range(1,101):
    q.put(worker)
    
q.join()
        


