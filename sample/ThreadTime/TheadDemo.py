# coding=utf-8

'''
线程是CPU分配资源的基本单位。
但一个程序开始运行，这个程序就变成了一个进程，而一个进程相当于一个或者多个线程。
当没有多线程编程时，一个进程也是一个主线程，但有多线程编程时，一个进程包含多个线程，包括主线程。
使用线程可以实现程序的并发.
'''
import threading

import time


'''
python3对多线程支持的是 threading 模块，应用这个模块可以创建多线程程序，并且在多线程间进行同步和通信。
在python3 中，可以通过两种方法来创建线程：
第一：通过 threading.Thread 直接在线程中运行函数；第二：通过继承 threading.Thread 类来创建线程

'''

def threadfun(x, y):
    for i in range(x, y):
        print(i)

# 创建线程

ta = threading.Thread(target=threadfun,args=(1,6))
tb = threading.Thread(target=threadfun,args=(10,16))

# 调用

ta.start()
tb.start()

print('---------------------------------')
# 通过继承 thread.Thread 类 来创建线程
# 这种方法只需要重载 threading.Thread 类的 run 方法，然后调用 start()开启线程就可以

class mythread(threading.Thread):
    def run(self):
        for i in range(1, 5):
            print(i)

ma = mythread()
mb = mythread()
ma.start()
mb.start()

# join()方法
#
# join()作用是 调用 join() 的线程 阻塞直到 某一线程结束才继续执行
print('*' * 20 + "join" + '*' * 30)
class mythread1(threading.Thread):
    def run(self):
        self.i = 1
        print('%d'%(self.i))
        self.i = self.i + 1
        time.sleep(1)   # 睡眠一秒
        print('%d'%(self.i))
        time.sleep(1)

print('*' * 20 +"isAlive()"+ '*' * 30)
# isAlive()方法
#
# 这个方法用于判断线程是否运行。
#
# 1.当线程未调用 start()来开启时，isAlive()会返回False
#
# 2.但线程已经执行后并结束时，isAlive()也会返回False

class mythread2(threading.Thread):
    def run(self):
        time.sleep(2)


# name属性和daemon属性
class threadname(threading.Thread):
    def run(self):
        pass

# daemon属性用来设置线程是否随主线程退出而退出

# daemon属性用来设置线程是否随主线程退出而退出当 daemon = False 时，
# 线程不会随主线程退出而退出（默认时，就是 daemon = False）
#
# 当 daemon = True 时，当主线程结束，其他子线程就会被强制结束

class  threaddaemon(threading.Thread):
    def run(self):
        time.sleep(3)
        print('my thread over')

def main():
    ta = threaddaemon()
    ta.daemon = True
    ta.start()
    print('main thread over')


# 划重点

# 线程的同步---锁
# 当一个进程拥有多个线程之后，如果他们各做各的任务互没有关系还行，但既然属于同一个进程，
# 他们之间总是具有一定关系的。比如多个线程都要对某个数据进行修改，则可能会出现不可预料的结果。
# 为保证操作正确，就需要引入锁来进行线程间的同步。
# python3 中的 threading 模块提供了 RLock锁(可重入锁)。
# 对于某一时间只能让一个线程操作的语句放到 RLock的acquire 方法 和 release方法之间。
# 即 acquire()方法相当于给RLock 锁  上锁，而 release() 相当于解锁。

class threadlock(threading.Thread):
    def run(self):
        global x     # 申请一个全局变量
        lock.acquire()
        x += 10
        print('%s:%d' % (self.name, x))
        lock.release()

x = 0
lock = threading.RLock()  # 创建一个可重入锁
def lockdome():
    l = []
    for i in range(5):
        l.append(threadlock())  # 创建5个线程，并把他们放到一个列表中
    for i in l:
        i.start()      # 开启列表中的所有线程

# 线程的同步---Event对象
# Event对象存在于 threading 模块中。
# Event 实例管理着 一个内部标志，通过 set() 方法来将该标志设置成 True，
# 使用 clear() 方法将该标志重置成 False
# wait() 方法会使当前线程阻塞直到标志被设置成 True，
# wait()可以选择给他一个参数，代表时间，代表阻塞多长时间，
# 若不设置就是阻塞直到标志被设置为True
#
# isSet()方法  ：能判断标志位是否被设置为True

class Mon(threading.Thread):
    def run(self):
        Dinner.clear()
        print('Cooking dinner')
        time.sleep(5)
        Dinner.set()  # 标志设置为 True
        print(self.name, ': dinner is ok !')

class Son(threading.Thread):
    def run(self):
        while True:
            if Dinner.isSet():
                break
            else:
                print('dinner is not  ready!!')
                Dinner.wait(1)
        print(self.name, ': Event Dinner')

def EventDome():
    mon = Mon()
    son = Son()

    mon.name = 'Mon'
    son.name = 'Son'
    mon.start()
    son.start()


if __name__ == '__main__':
    ja = mythread1()

    ja.start()
    ja.join()  ##主线程等待 ta线程结束才继续执行

    print('main thead over')
    #
    ta = mythread2()
    print(ta.isAlive())
    ta.start()
    print(ta.isAlive())
    time.sleep(3)
    print(ta.isAlive())
    print('----- thread name ---------')
    name1 = threadname()
    name1.name='thread-linl'
    name2 = threadname()
    name1.start()
    name2.start()
    print(name1.name)
    print(name2.name)
    # deamon
    main()
    # rlock
    lockdome()
    # Event
    Dinner = threading.Event()
    EventDome()


