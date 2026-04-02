import threading
def thread_task(f,*a): t=threading.Thread(target=f,args=a); t.start(); t.join()
