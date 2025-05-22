from multiprocessing.pool import Pool, ThreadPool
from multiprocessing import Process
import time
from random import shuffle

def test(num: int)-> int:
    time.sleep(num)
    print(f"{num} 처리 완료료")
    return num

if __name__ == "__main__":
    numbers = [30, 10, 5, 0, 20, 15]
    #for imap_unordered, will add 30-p1 while that add 10-p2
    #so p2 will finish first then add 10,5,0,20 then p1 will finish then add 15-p1
    #imap_unordered will print finish based on the first that finish not input arrangement
    #if just imap, will print based on input arrangement
    shuffle(numbers) #to shuffle number that are input in arrangement to get faster

    t = time.perf_counter()
    #making pool with number of process inside
    with ThreadPool(2) as pool:
        #for result in pool.imap(test, numbers):
        for result in pool.imap_unordered(test, numbers):
            print(result)                      # the more argument in pool more faster
           
    duration = time.perf_counter()- t   #time will take based on value of number
    print(f"time take:{duration:.2f}")  # if number is 30 - means its gonna takes 30 sec
    #for num in numbers:
        #test(num)
