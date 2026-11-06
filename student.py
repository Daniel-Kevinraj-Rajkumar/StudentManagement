def add_student(l):
	name=input("Enter student name: ")
	l.append(name)
	print(f"{name} has been added. Modified list is {l}")

def disp_details(l):
	print(f"Student details:\n{l}")

def search_student(l):
	name=input("Enter student name: ")
	if name in l:
		print(f"{name} is present in list.")
	else:
		print(f"{name} is not present is list.")
