class Employee:
	def work(self):
		print("Employee works")

class Student:
	def study(self):
		print("Student studies")

class WorkingStudent(Employee, Student): # Множественное наследование от классов Employee и student
	pass

tom = WorkingStudent()
tom.work()
tom.study()