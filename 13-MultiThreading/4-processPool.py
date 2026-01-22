from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers(num):
    time.sleep(1)
    return f"{num*num}"

numbers=[1,2,3,4,5]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executors:
        results=executors.map(print_numbers,numbers)

    for result in results:
        print(result)


# t=time.time()
# finished_time=time.time()-t