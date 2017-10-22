#!/usr/bin/python3
# coding: utf-8


from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    vartemp1 = input()
    p = Process(target=f, args=('bob',))
    p.start()
    print(p.run())
    vartemp = input()
    p.join()
