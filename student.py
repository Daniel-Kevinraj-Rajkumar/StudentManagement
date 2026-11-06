def add_student(l):
	name=input("Enter student name to add: ")
	l.append(name)
	print(f"{name} has been added.\nModified list: {l}")

def disp_details(l):
	print(f"Student details: {l}")

def search_student(l):
	name=input("Enter student name to search: ")
	if name in l:
		print(f"{name} is present in list.")
	else:
		print(f"{name} is not present is list.")

def delete_student(l):
	name=input("Enter student name to delete: ")
	if name in l:
		l.remove(name)
		print(f"{name} has been removed.\nModified list: {l}")
	else:
		print(f"{name} is not present in list.")
