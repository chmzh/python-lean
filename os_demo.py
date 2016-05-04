#coding=utf-8
import os
#获取环境变量
print (os.environ["JAVA_HOME"])

#当前进程的用户
print (os.environ["LOGNAME"])
print (os.getlogin())

os.putenv("key_a","val_a")

print (os.getenv("key_a","d"))

#改变路径
os.chdir("../")
os.system("ls")
#获取当前工作目录
print (os.getcwd())


#改变当前工作目录
fd = os.open("../../",4)
os.fchdir(fd)
#获取当前工作目录
print (os.getcwd())

print (os.ctermid())

#当前进程有效组ID
print (os.getegid())
print (os.getgid())

#当前进程有效用户ID
print (os.geteuid())
print (os.getuid())

#获取指定进程ID所属的组
#print (os.getpgid(123))

#当前进程组ID
print (os.getpgrp())
#当前进程ID
print (os.getpid())


#当前进程父进程ID
print (os.getppid())

#Return a tuple (ruid, euid, suid) denoting the current process’s real, effective, and saved user ids.
#print (os.getresuid())

#Return a tuple (rgid, egid, sgid) denoting the current process’s real, effective, and saved group ids.
#print (os.getresgid())

#返回当前进程真实用户ID
print (os.getuid())



