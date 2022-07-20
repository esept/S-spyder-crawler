from concurrent.futures import ThreadPoolExecutor # 线程池
from concurrent.futures import ProcessPoolExecutor # 进程池
'''
线程池和进程池
线程池 ：
    一次性开辟一些线程，用户给线程池提交任务
    线程人物的调用交给线程池完成
'''

def fn(name):
    for i in range(100):
        print(name,i)


if __name__ == '__main__':
    # 创建线程池: 创建有50个线程的线程池
    with ThreadPoolExecutor(50) as t: # 使用进程池的话可以直接替换
        for i in range(100):
            t.submit(fn,name = f"thread{i}")
    
    # 等待线程池中的任务全部执行完毕之后才继续执行with之外的代码--> 线程守护
    print("threadPoolExecutor function Done")
