'''
一般情况下，当程序处于IO操作时，线程都会处于阻塞状态
当程序遇到了IO操作时，可以选择性的切换到其他任务上
'''

async def func():
    
    print("hello im salia")

if __name__ == '__main__':
    func() # 此时的函数是yi bu xie cheng