"""

Write a python code using function, file input and print each line with line number in the terminal.

*********************data.txt(File Extenstion)***********************

Python is an interpreted
High-level,gentral purpose programming language
Created by gudio van Rossum and first releasted in 1991
Its supports multiple programmig patterns[Web,Gui,Scriptting etc] 
It is support OOP's approach to develop applications

********************Location Path***************************

"C:/Users/ARUN G/Desktop/Chadura Tech"

"""

#program

#Write a python code using function, file input and print each line with line number in the terminal.


import os
os.chdir("C:/Users/ARUN G/Desktop/Chadura Tech")
filename=input("Enter the extension:")
f=open(filename,'r')
count=0
for i in f:
  count+=1
  print("Line",count,"",i)
f.close()


