#coding=utf-8
import platform

DEBUG = False

def py_version():
    return platform.python_version_tuple()

def py_main_version():
    return py_version()[0]
