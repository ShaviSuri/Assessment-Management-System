# import pandas as pd

choice = input('''Welcome to the Student and Assessment Management System
<A>add details of a student.
<I>insert assignment marks of a student
<S>search assessment marks for a student.
<Q>quit.\n''')

def AddStudent():
	stu_id = input("Please enter the student ID: ")
	stu_name = input("Please enter the student name: ")
	course = input("Please enter the course: ")
	print("\n\nThank You!")
	with open('student.txt',mode='a') as my_file:
		text = my_file.write("\n"+stu_id+" "+ stu_name+" "+ course)

	print("The details of the student you entered are as follows:")
	print("Student ID: "+stu_id)
	print("Student name: "+stu_name)
	print("Please enter the course: "+course)
	print("The record has been successfully added to the students.txt file.\n")
	loop= input("Do you want to enter details for another student (Y/N)?")
	if loop == 'Y':
		AddStudent()
	elif loop == 'N':
		pass
	else:
		print("Invalid input")

def InsertMarks():
	stu_id = input("Please enter the student ID: ")
	sbj_code = input("Please enter the subject code: ")
	assess_no = input("Please enter the assessment number: ")
	marks = input("Please enter assessment marks: ")
	print("\n\nThank You!")
	with open('assessment.txt',mode='a') as my_file:
		text = my_file.write("\n"+stu_id+" "+ sbj_code+" "+ assess_no+" "+marks)

	print("The details of the student you entered are as follows:")
	print("Student ID: "+stu_id)
	print("Student code: "+sbj_code)
	print("Assessment number: "+assess_no)
	print("Assessment marks: "+marks)
	print("The record has been successfully added to the assessment.txt file.\n")
	loop= input("Do you want to enter details for another assessment (Y/N)?")
	if loop == 'Y':
		InsertMarks()
	elif loop == 'N':
		pass
	else:
		print("Invalid input")

def Search():
	stu_id = input("Please enter the student ID: ")
	
	with open('student.txt') as my_file:
		for line in my_file:
			if stu_id in line:
				stu_detail = line.split()
				if stu_id == stu_detail[0]:
					print("A Student has been found: ")
					print("Student ID: "+stu_detail[0])
					print("Student Name: "+stu_detail[1])
					print("course: "+stu_detail[2]+"\n\n")
					break
				else:
					print("Id does not exist!!")
				break
	

	with open('assessment.txt') as my_file:
		for line in my_file:
			if stu_id in line:
				assess_detail = line.split()
				if stu_id == assess_detail[0]:
					print("Subject Code: "+assess_detail[1])
					print("Assessment Number: "+assess_detail[2])
					print("Marks: "+assess_detail[3]+"\n")
	print("Thank You!\n")

	loop= input("Do you want to enter details for another assessment (Y/N)?")
	if loop == 'Y':
		Search()
	elif loop == 'N':
		pass
	else:
		print("Invalid input")

				

if choice == 'A':
	AddStudent()
elif choice == 'I':
	InsertMarks()
elif choice == 'S':
	Search()
elif choice == 'Q':
	print("Exiting the software.....")
	pass
else:
	print("Invalid input")

