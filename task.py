"""

1.	What is the difference between 32bit and 64bit computers? How much Maximum memory access they can have?

	What is the difference between 32bit and 64bit computers?

Parameter	32-bit processors	64-bit processors
Addressable space	It has 4 GB addressable space	64-bit processors have 16 GB addressable space
Application support	64-bit applications and programs won't work	32-bit applications and programs will work
OS support	Need a 32-bit operating system.	It can run on 32 and the 64-bit operating system.
System available	Support Windows 7, 8 Vista, XP, and, Linux.	Windows XP Professional, Windows Vista, Windows 7, Windows 8,Windows 10, Linux, and Mac OS X.
Memory limits	32-bit systems limited to 3.2 GB of RAM 32 bit Windows. It addresses limitation doesn't allow you to use full 4GB of Physical memory space.	64-bit systems will enable you to store up to 17 Billion GB of RAM.

	How much Maximum memory access they can have?

	A 64-bit computer (which means it has a 64-bit processor) can access more than 4 GB of RAM. If a computer has 16 GB of RAM, it better have a 64-bit processor. Otherwise, at least 12 GB of the memory will be inaccessible by the CPU

	A 32bit machine the maximum amount of memory usable is around 4GB. Actually, depending on the OS it might be less due to parts of the address space being reserved: On Windows you can only use 3.5GB for example. On 64bit you can indeed address 2^64 bytes of memory.

2.	What is a low level language and high level language? Give examples.

	Both High level language and low level language are the programming language’s types.
	The main difference between high level language and low level language is that, Programmers can easily understand or interpret or compile the high level language in comparison of machine.
	 On the other hand, Machine can easily understand the low level language in comparison of human beings.

Examples of high level languages are: C, C++, Java, Python, etc.

3.	Define an object in the context of object oriented programming.

	Object (is an instance of a class) ... In the class-based object-oriented programming paradigm, object refers to a particular instance of a class, where the object can be a combination of variables, functions, and data structures.

4.	What is Linux? Explain 5 Linux commands.
	Linux is an operating system's kernel. You might have heard of UNIX. Well, Linux is a UNIX clone. But it was actually created by Linus Torvalds from Scratch. Linux is free and open-source, that means that you can simply change anything in Linux and redistribute it in your own name! There are several Linux Distributions, commonly called “distros”.

•	 Ubuntu Linux
•	Red Hat Enterprise Linux
•	Linux Mint
•	Debian
•	Fedora


	ls — Use the "ls" command to know what files are in the directory you are in. You can see all the hidden files by using the command “ls -a”.

	touch — The touch command is used to create a file. It can be anything, from an empty txt file to an empty zip file. For example, “touch new.txt”.


	mkdir & rmdir — Use the mkdir command when you need to create a folder or a directory. For example, if you want to make a directory called “DIY”, then you can type “mkdir DIY”. Remember, as told before, if you want to create a directory named “DIY Hacking”, then you can type “mkdir DIY\ Hacking”. Use rmdir to delete a directory. But rmdir can only be used to delete an empty directory. To delete a directory containing files, use rm.

	mv — Use the mv command to move files through the command line. We can also use the mv command to rename a file. For example, if we want to rename the file “text” to “new”, we can use “mv text new”. It takes the two arguments, just like the cp command.

	pwd — When you first open the terminal, you are in the home directory of your user. To know which directory you are in, you can use the “pwd” command. It gives us the absolute path, which means the path that starts from the root. The root is the base of the Linux file system. It is denoted by a forward slash( / ). The user directory is usually something like "/home/username.



5.	Define Linux Kernel?
	The Linux kernel is a free and open-source, monolithic, Unix-like operating system kernel. ... As part of the kernel's functionality, device drivers control the hardware; "mainlined" (included in the kernel) device drivers are also meant to be very stable.
	A kernel is the lowest level of easily replaceable software that interfaces with the hardware in your computer. It is responsible for interfacing all of your applications that are running in “user mode” down to the physical hardware, and allowing processes, known as servers, to get information from each other using inter-process communication (IPC).

Three Types: Monolithic, Microkernel, And Hybrid


6.	What is git and what version installed on your Linux machine?

•	Git is a free and open source distributed version control system designed to handle     everything from small to very large projects with speed and efficiency.


•	What is version control?
Git is, first and foremost, a version control system (VCS). There are many version control systems out there: CVS, SVN, Mercurial, Fossil, and, of course, Git.
•	what version installed on your Linux machine
Check os version in Linux
The procedure to find os name and version on Linux:
1.	Open the terminal application (bash shell)
2.	For remote server login using the ssh: ssh user@server-name
3.	Type any one of the following command to find os name and version in Linux:
cat /etc/os-release
lsb_release -a
hostnamectl
4.	   Type the following command to find Linux kernel version:
uname -r
Let us see all examples in detailed.
/etc/os-release file
Type the following cat command:
$ cat /etc/os-release
Sample outputs:
NAME="Ubuntu"
VERSION="17.10 (Artful Aardvark)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 17.10"
VERSION_ID="17.10"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=artful
UBUNTU_CODENAME=artful
lsb_release command
The lsb_release command gives LSB (Linux Standard Base) and distribution-specific information on the CLI. The syntax is:
$ lsb_release -a
Sample outputs:
LSB Version:	:core-4.1-amd64:core-4.1-noarch
Distributor ID:	CentOS
Description:	CentOS Linux release 7.4.1708 (Core) 
Release:	7.4.1708
Codename:	Core
7.	Create a gitlab account and make a repository.

Create a gitlab account

Link: https://gitlab.com/users/sign_in

Create a repository:

Link: https://docs.gitlab.com/ee/user/project/repository/

Create a project:

Link: https://docs.gitlab.com/ee/gitlab-basics/create-project.html

"""

#Task Program

#PROGRAM

#Define an object in the context of object oriented programming.

#Examples in any object oriented language.

class Test:
  def add (self,x,y):
    print("Add=",x+y) 
obj = Test() 
obj.add(10,20) 

#Write a python code using class (at least 3 functions inside) and a Dictionary.

#Class :

class Person:
  sid=[]
  name=[]
  age=[]
  def nofp(self):
    self.n=int(input("Enter Number of person:"))
  def getData(self):
    for i in range(self.n):
      self.sid.append (int(input("Enter id:")))
      self.name.append (input("Enter name:"))
      self.age.append (int(input("Enter age:")))
  def printData(self):
    print("STUDENT DETAILS")
    print("===========================================")
    print("ID \t\t NAME \t\t AGE")
    print("===========================================")
    for i in range(self.n):
      print(self.sid[i],"\t\t", self.name[i],"\t\t", self.age[i])
p=Person()
p.nofp()
p.getData()
p.printData()

#Dictionary:
n=5
d={}
for i in range (1,n+1):
	d[i]=i**2
print(d)




#Write a python code to print your linux distribution name and kernelversion.

#Sample Coding:
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

#Sample Coding:
import platform
print('Uname:', platform.uname())
print()
print('Distribution :', platform.linux_distribution())
print('Machine :', platform.machine())
print('Node :', platform.node())
print('Processor :', platform.processor())
print('Release :', platform.release())
print('System :', platform.system())
print('Version :', platform.version())
print('Platform :', platform.platform())






