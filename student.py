def add_student(l):
	name=input("Enter student name to add: ")
	l.append(name)
	print(f"{name} has been added.\nModified list: {l}")

def disp_details(l):
	print(f"Student details: {l}")

def search_student(l):
	name=input("Enter student name to search: ")
	if name in l:
		print(f"{name} exists.")
	else:
		print(f"{name} does not exist.")

def delete_student(l):
	name=input("Enter student name to delete: ")
	if name in l:
		l.remove(name)
		print(f"{name} has been removed.\nModified list: {l}")
	else:
		print(f"{name} does not exist.")

def update_student(l):
	name=input("Enter the student name to update: ")
	if name in l:
		newname=input("Enter the new name of the student: ")
		l[l.index(name)]=newname
		print(f"Modified list: {l}")
	else:
		print(f"{name} does not exist.")
