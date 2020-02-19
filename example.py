Examples in any object oriented language.

class Test:  
  def add (self,x,y): 
		print("Add=",x+y) 
obj = Test() 
obj.fun(10,20)

python code using class (at least 3 functions inside) and a Dictionary.

class Person:
		sid=[]
name=[]
age=[]
def nofp(self):
		self.n=int(input(“Enter number of person:”))
def getData(self):
		for i in range(self.n):
			self.sid.append (int(input(“Enter id:”))
			self.name.append (int(input(“Enter name:”))
			self.ageappend (int(input(“Enter age:”))
	       def printData(self):
		print(“STUDENT DETAILS”)
		print(“================”)
		print(“ID \t\t NAME \t\t AGE”)
		print(“================”)
		for i in range(self.n):
			print(self.sid[i],”\t\t”, self.sname[i],”\t\t”, self.age[i])
p=Person()
p.nofp()
p.getData()
p.printData()

	Dictionary:
	n=5
	d={}
	for i in range (1,n+1):
		d[i]=i**2
	print(d)
  
  
  
  Example:
f = open ("demofile.txt", "r") 
print (f.read ())

Example: Return the 5 first character of the file.
f = open ("demofile.txt", "r")
print(f.read(5))

You can return one line by using the read line() method:
Example:
Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())

	By calling readline() two times, you can read the two first lines:
Example:
Read two line of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
Close File:
	It is a good practice to always close the file when you are done with it.
Example:
Close the file when you are finish with it:
f = open("demofile.txt", "r")
print(f.readline())
f.close()

	That means we are able to ask the user for input.

Example:
print("Enter your name:")
x = input()
print("Hello ", x)


