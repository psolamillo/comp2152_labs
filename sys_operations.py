import os
import sys
import platform
import socket

#Lab 9 Question 3.a.a, 3.a.b
#Machine Type and Processor Type
print(platform.machine())
print(platform.architecture())

#Lab 9 - Question 3.a.c, 3.a.d.
#Set and Get socket timeout

socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

#OS name
print(os.name)
print(platform.system())

#Process ID
print(os.getpid())

#File Descriptors
f_name = "fdpractice.txt"

#f1 = open(f_name,"r")
#print(f1)
#f1.close()

f = os.open(f_name, os.O_RDWR | os.O_CREAT)
print(f)

f_obj = os.fdopen(f, "a+")

f_obj.close()

print()

#Forking
print("Before fork:",os.getpid())
p = os.fork()
print("After fork:",os.getpid())


if p ==0:
    print("Child Process")
    print("Parent Process PID:",os.getppid())

else:
    print("Parent Process")
    os.wait()
    print("Child Process PID:",os.getpid())

print("Last line")