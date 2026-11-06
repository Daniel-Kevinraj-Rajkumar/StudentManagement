import student as s
l=[]
print("="*40)
print("Welcome to Student Management System")
while True:
	print("="*40)
	print("1. Add student")
	print("2. Display student details")
	print("3. Search student")
	print("4. Delete student")
	print("5. Exit")
	print("="*40)
	num=int(input("Enter your choice: "))
	if num == 1:
		s.add_student(l)
	elif num == 2:
		s.disp_details(l)
	elif num == 3:
		s.search_student(l)
	elif num == 4:
		s.delete_student(l)
	elif num == 5:
		print("Exiting program .")
		break
	else:
		print("Invalid input. Please try again.")
