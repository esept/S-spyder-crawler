from threading import Thread # 线程类

        
'''

def func():
    for i in range(1000):
        print("func",i)

if __name__ == '__main__':
    t = Thread(target=func()) # 创建线程，并给线程分配任务
    t.start() # 多线程状态为：可以开始工作状态，具体的执行时间由cpu决定
    for i in range(1000):
        print("main",i)
'''


class Mythread(Thread):
    def run(self): # 当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print("mythread",i)
    
def func(name):
    for i in range(1000):
        print(name,i)
# if __name__ == '__main__':
#     t = Mythread()
#     # t.run() # 如果使用run(),这里就是方法的调用，是单线程
#     t.start() # 开启线程
#
#     for i in range(1000):
#         print("main",i)

if __name__ == '__main__':
    t1 = Thread(target=func,args = ("t1",)) # 传递参数必须是元组,里面的逗号是必须的
    t1.start()
    
    t2 = Thread(target=func,args = ("t2",))
    t2.start()