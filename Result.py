sub1=int(input("Enter first subjuct marks:"))
sub2=int(input("Enter second subjuct marks:"))
sub3=int(input("Enter third subjuct marks:"))
sub4=int(input("Enter fourth subjuct marks:"))
sub5=int(input("Enter fifth subjuct marks:"))
sub6=int(input("Enter sixsth subjuct marks:"))

Sum=sub1+sub2+sub3+sub4+sub5+sub6
Avg=Sum/6
if(sub1>=35 and sub2>=35 and sub3>=35 and sub4>=35 and sub5>=35 and sub6>=35):
	print("pass")
else:
	print("Fail")
if(Avg>=90):
	print("Distinction")
elif(Avg>=80):
	print("First class")
elif(Avg>=70):
	print("Second class")
elif(Avg>=60):
	print("Third class")
elif(Avg>=35):
	print("Pass class")
elif(Avg<35):
	print("Fail")
if(Sum==510):
	print("A+")
elif(Sum==450):
	print("B+")
elif(Sum==350):
	print("C+")
else:
	print("C")
	
print("sum of all subjucts=",Sum)
print("avrage of total marks=",Avg)