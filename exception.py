#coding=utf-8
import os

def t():
    try:
        os.system("ls /abc")
    except BaseException:
        print('nihao')
    finally:
        raise IOError

def t1():
    try:
        t()
    except:IOError
    print('ioerror')

#assert 1==2
t1()
