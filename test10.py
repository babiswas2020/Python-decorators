from threading import Thread
from time import time
from time import sleep
import random

def task(str1):
   print(f"Obtained task {str1}")
   sleep(4)
   print(f"Executing task {str1}")
   print(f"Completed task {str1}")


if __name__=="__main__":
   thread_pool=[]
   taskpool=["task"+str(random.choice([1,2,3,4,5])) for i in range(12)]
   for i in range(12):
      t=Thread(target=task,args=(random.choice(taskpool),))
      thread_pool.append(t)
   for thread in thread_pool:
       thread.start()
   for thread in thread_pool:
       thread.join()

      
   
   