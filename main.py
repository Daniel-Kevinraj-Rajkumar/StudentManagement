import student as s
l=[]
print("="*40)
print("Welcome to Student Management System")
while True:
	print("="*40)
	print("1. Add student")
	print("2. Display student details")
	print("3. Search for a student")
	print("4. Exit")
	print("="*40)
	num=int(input("Enter your choice: "))
	if num == 1:
		s.add_student(l)
	elif num == 2:
		s.disp_details(l)
	elif num == 3:
		s.search_student(l)
	elif num == 4:
		print("Exiting program .")
		break
	else:
		print("Invalid input. Please try again.")
