import threading
import time
import inspect

class Thread(threading.Thread):

    def __init__(self, t,  *args):

        threading.Thread.__init__(self, target=t, args=args)
        self.start()

count = 0
lock = threading.Lock()

def incre():

    global count
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print(f"\n\ninside {caller}")
    print("acquiring lock")

    with lock:
        print("Lock Acquired")
        count += 1
        print(f"count: {count}")
        time.sleep(2)


def bye():
    while count < 5:
        incre()


def hello_there():
    while count < 5:
        incre()

def main():

    Thread(hello_there)
    Thread(bye)
