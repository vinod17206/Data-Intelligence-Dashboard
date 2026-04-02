from multiprocessing import Process
def process_task(f,*a): p=Process(target=f,args=a); p.start(); p.join()
