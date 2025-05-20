from multiprocessing import Process, Manager
import time
from random import shuffle

def test(num: int)-> int:
    #time.sleep(num)
    print(f"{num} 처리 완료료")
    return num
    #can return use manager for proper return with type
    #..output_list.append(..)

if __name__ == "__main__":
    numbers = [30, 10, 5, 0, 20, 15] #if process is 1000 then too many so use chunks
    shuffle(numbers)

   # manager = Manager()
   # output_list = manager.list()

    chunks = []
    for i in range(4):
        chunks.append(numbers[i::4]) #cut process 4 each chunck 

    t = time.perf_counter()
                 
    #not use pool, make own process
    process_list =[]
    for num in numbers:
        process = Process(target=test, args=(num,)) #must put , to reg in tuple
        process_list.append(process)

    #for chunk in chunks:
       # process = Process(target=test, args=(chunk,output_list)) #must put , to reg in tuple
        #process_list.append(process)

    for process in process_list: #to start the start
        process.start()

    for process in process_list: #to join the process once the above finish each time
        process.join()
                                             
    duration = time.perf_counter()- t   #time will take based on value of number
    print(f"time take:{duration:.2f}") 