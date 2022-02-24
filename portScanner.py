'''
Scans for available ports.
Open ports can be dangerous when the service listening on the port
is misconfigured, unpatched, vulnerable to exploits, or has poor network security rules. ...
The reason people call for closed ports because less open ports reduces your attack surface.
'''
import socket
import threading
from queue import Queue
#Local host (own comp) or add router
target = "192.168.1.254"
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.connect((target, port))
        return True
    
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        #FIFO
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open.".format(port))
            open_ports.append(port)
    

if __name__ == "__main__":
    port_list = range(1,1024)
    fill_queue(port_list)
    
    thread_list = []
    
    for t in range(100):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    
    for thread in thread_list:
        thread.start()
    
    for thread in thread_list:
        thread.join()
    
    print("Open ports are: ", open_ports)

