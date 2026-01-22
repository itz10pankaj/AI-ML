## When to use MultiThreading 
# 1- I/O-bound tasks
# 2- Concurrent Operations 
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"{i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter,{letter}")

## Create two threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t=time.time()
# print_numbers()

# print_letters()
t1.start()
t2.start()

## Wait to end
t1.join()
t1.join()
  
finished_time=time.time()-t
print("finished_time",finished_time)