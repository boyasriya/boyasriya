#1.print hello world
print("HELLO WORLD")

#2.cheak it is real number or not
#variable_name.isdigit is used to cheak wheather the given input is a number(digit) or a alphabet
a=input("Enter the number:")
if a.isdigit():
	print("It is a real number:")
else:
	print("It is not a real number:")
	
#3.to add two numbers 
a1=int(input("Enter a number_1:"))
a2=int(input("Enter a number_2:"))
s=a1+a2
print("The sum of two numbers is",sum)
	
#4.to divide two numbers
a1=int(input("Enter a number_1:"))
a2=int(input("Enter a number_@:"))
if((type(a)=='int'or'float') and (type(b)=='int'or'float')):
	div=a/b
	print("The division is:",div)
else:
	print(The numbers are not the real numbers")


#5.To find the dot product of the given vectors/lists
# dot product of two vectors/two list 
n1=int(input("Enter how many elements do you want to add in a list:"))
#intialize the empty list
list_1=[]
for i in range(n1):
	el=int(input("Enter element:"))
	list_1.append(el)
print(list_1)
n2=int(input("Enter how many elements do you want to add in a list:"))
#intilise the empty list
list_2=[]
for i in range(n2):
	e2=int(input("Enter element:"))
	list_2.append(e2)
print(list_2)
#dot product
#by using for loop
dot_product=0
for i,j in zip(list_1,list_2):
	dot_product=dot_product+i*j
print(dot_product)

#6.determinat of the Matrix
def determinant(matrix):
	if len(matrix)!=2 or len(matrix[1])!=2:
		raise ValueError("Input matrix must be a 2*2 matrix")
	return matrix[0][0]*matrix[1][1]-matrix[0][1]
matrix_2=[[3,4],[3,4]]
result=determinant(matrix_2)
print("Determinant od 2*2 matrix",result)


























