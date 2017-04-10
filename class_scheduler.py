from constraint import *

from datetime import datetime

SEMESTERS = (("FALL", 0), ("SPRING", 1), ("SUMMER", 2))

class ClassScheduler:

	def __init__(self, courses, prerequisites, offerings, credits, num_classes):
		self.courses = courses
		self.prerequisites = prerequisites
		self.offerings = offerings
		self.credits = credits
		self.remaining_courses = list(set(self.courses) - set(self.credits))

		if num_classes > len(self.remaining_courses):
			self.num_classes = len(self.remaining_courses)
		else:
			self.num_classes = num_classes

		self.starting_semester = self.calc_starting_semester()

		if (len(self.remaining_courses) % self.num_classes) == 0:
			self.remaining_semesters = (len(self.remaining_courses) / self.num_classes, False)
		else:
			self.remaining_semesters = ((len(self.remaining_courses) / self.num_classes) + 1, True)

		self.semester_cycles = self.remaining_semesters[0] / 3
		self.problem = Problem()

	"""
		Detrmines starting semester based on current month

		returns - Tuple with values (SemesterName, SemesterNumber)
		
		SemesterNumbers
			0 : Fall
			1 : Spring
			2: Summer
	"""
	def calc_starting_semester(self):
		month = datetime.now().month

		if month in range(1,5):
			starting_semester = SEMESTERS[2]
		elif month in range(5,9):
			starting_semester = SEMESTERS[0]
		else:
			starting_semester = SEMESTERS[1]

		return starting_semester

	"""
		Determines the number of each semester(fall, spring, summer) 
		depending on the starting semesterand the number of reaming semesters

		returns - Tuple with values(NumberFallSemesters, NumberSpringSemesters, NumberSummerSemesters)
	"""
	def calc_num_semesters(self):
		fall_semesters = 0
		spring_semesters = 0 
		summer_semesters = 0

		if self.semester_cycles > 0:
			for num in range(0, self.semester_cycles):
				fall_semesters += 1
				spring_semesters += 1
				summer_semesters += 1

			semester_remainder = self.remaining_semesters[0] % 3
			if semester_remainder == 1:
				if self.starting_semester[1] == 0:
					fall_semesters += 1
				elif self.starting_semester[1] == 1:
					spring_semesters += 1
				else:
					summer_semesters +=1
			elif semester_remainder == 2:
				if self.starting_semester[1] == 0:
					fall_semesters += 1
					spring_semesters +=1
				elif self.starting_semester[1] == 1:
					spring_semesters += 1
					summer_semesters += 1
				else:
					summer_semesters +=1
					fall_semesters += 1

		else:
			if self.starting_semester[1] == 0:
				fall_semesters += 1
				if self.remaining_semesters[0] == 2:
					spring_semesters += 1

			elif self.starting_semester[1] == 1:
				spring_semesters += 1
				if self.remaining_semesters[0] == 2:
					summer_semesters += 1

			else:
				summer_semesters += 1
				if self.remaining_semesters[0] == 2:
					fall_semesters += 1

		return (fall_semesters, spring_semesters, summer_semesters)

	"""
		Determines the domains for courses based on when they are offered and
		how many of each semesters there will be

		returns - list with number values representing the semesters
		
		number % 3 == 1 -> Fall Semester
		number % 3 == 2 -> Spring Semester
		number % 3 == 3 -> Summer Semester 

	"""
	def calc_course_offerings(self, course, fall_semesters, spring_semesters, summer_semesters):
		semester_offerings = []

		# Course has is not offered every semester
		if course in self.offerings:
			offered = self.offerings[course]
			if offered[0] and fall_semesters > 0:
				semester_offerings.append(1)
				if fall_semesters > 1:
					for num in range(1,fall_semesters):
						semester_offerings.append((num * 3) + 1)

			if offered[1] and spring_semesters > 0:
				semester_offerings.append(2)
				if spring_semesters > 1:
					for num in range(1, spring_semesters):
						semester_offerings.append((num * 3) + 2)

			if offered[2] and summer_semesters > 0:
				semester_offerings.append(3)
				if summer_semesters > 1:
					for num in range(1, summer_semesters):
						semester_offerings.append((num* 3) + 3)
		
		# Course is offered every semester
		else:
			if self.semester_cycles > 0:
				map(lambda num:semester_offerings.append(num), xrange(1, (self.semester_cycles  * 3) + 1))

				semester_remainder = self.remaining_semesters[0] % 3
				if semester_remainder == 1:
					if self.starting_semester[1] == 0:
						semester_offerings.append((self.semester_cycles * 3)+ 1)
					elif self.starting_semester[1] == 1:
						semester_offerings.append((self.semester_cycles * 3)+ 2)
					else:
						semester_offerings.append((self.semester_cycles * 3)+ 3)

				elif semester_remainder == 2:
					if self.starting_semester[1] == 0:
						semester_offerings.append((self.semester_cycles * 3)+ 1)
						semester_offerings.append((self.semester_cycles * 3)+ 2)
					elif self.starting_semester[1] == 1:
						semester_offerings.append((self.semester_cycles * 3)+ 2)
						semester_offerings.append((self.semester_cycles * 3)+ 3)
						summer_semesters += 1
					else:
						semester_offerings.append((self.semester_cycles * 3)+ 3)
						semester_offerings.append((self.semester_cycles * 3)+ 1)
			else:
				if self.remaining_semesters[0] > 1:
					semester_offerings.append(self.starting_semester[1])

					if self.starting_semester[1] == 1:
						semester_offerings.append(2)

					elif self.starting_semester[1] == 2:
						semester_offerings.append(3)

					else:
						semester_offerings.append(1)


				else:
					semester_offerings.append(self.starting_semester[1])

		return semester_offerings

	"""
		Sets constrains for the problem. These include prerequisites and 
		number of classes per semester constraints
	"""
	def set_constraints(self):
		# Handles all prerequisites constraints
		for course in self.remaining_courses:
			if course in self.prerequisites:
				for req in self.prerequisites[course]:
					if req not in self.credits: # Only add constraint if the course hasn't been taken
						self.problem.addConstraint(lambda course1, course2: course1 > course2, [course, req])

		# One semester will not be filled
		if self.remaining_semesters[1]:
			if self.semester_cycles > 0 and self.remaining_semesters[0] == 3:
				if self.starting_semester[1] == 0:
					self.problem.addConstraint(SomeInSetConstraint([1], self.num_classes, True))
					self.problem.addConstraint(SomeInSetConstraint([2], self.num_classes, True))
				elif self.starting_semester[1] == 1: 
					self.problem.addConstraint(SomeInSetConstraint([2], self.num_classes, True))
					self.problem.addConstraint(SomeInSetConstraint([3], self.num_classes, True))
				else:
					self.problem.addConstraint(SomeInSetConstraint([3], self.num_classes, True))
					self.problem.addConstraint(SomeInSetConstraint([1], self.num_classes, True))

			elif self.semester_cycles > 0:
				last_semester = self.starting_semester[1] + self.remaining_semesters[0]

				for course in self.problem._variables:
					if course not in self.offerings:
						constraint_list = self.problem._variables[course]
				constraint_list.remove(last_semester)

				for semester in constraint_list:
					self.problem.addConstraint(SomeInSetConstraint([semester], self.num_classes, True))

			else:
				self.problem.addConstraint(SomeInSetConstraint([self.starting_semester[1]], self.num_classes, True))
		
		# All semester will have the number of classes
		else:
			if self.semester_cycles > 0:
				for semester in range(1, self.remaining_semesters[0]+1):
					self.problem.addConstraint(SomeInSetConstraint([semester], self.num_classes, True))
			
			# Covers scenrio where self.num_classes is set to len(self.remaining_courses)
			else:
				if self.remaining_semesters[0] == 1:
					self.problem.addConstraint(SomeInSetConstraint([self.starting_semester[1]], self.num_classes, True))	
				else:
					self.problem.addConstraint(SomeInSetConstraint([self.starting_semester[1]], self.num_classes, True))

					if self.starting_semester[1] == 1:
						self.problem.addConstraint(SomeInSetConstraint([2], self.num_classes, True))
					elif self.starting_semester[1] == 2:
						self.problem.addConstraint(SomeInSetConstraint([3], self.num_classes, True))
					else:
						self.problem.addConstraint(SomeInSetConstraint([1], self.num_classes, True))


	def normalize_solutions(self, solutions):
		year = datetime.now().year
		normalized_solutions = []
		for solution in solutions:
			print solution
			schedule = {}
			for course,semester in solution.iteritems():
				semester_number = semester % 3 
				year_number = semester / 3

				if semester_number == 1:
					value = SEMESTERS[0][0] + " " + str(year + year_number)
				elif semester_number == 2:
					value = SEMESTERS[1][0] + " " + str(year + year_number)
				else:
					value = SEMESTERS[2][0] + " " + str(year + year_number)
				schedule[course] = value

			print schedule
			print "---------------------------"
			normalized_solutions.append(schedule)
		return normalized_solutions


	"""
		Solves the problem using above class methods

		returns - List of solutions

		Solutions are dictionaries with key:value pairs representing  Course: Semester
	"""
	def solve(self):
		fall_semesters, spring_semesters, summer_semesters = self.calc_num_semesters()

		for course in self.remaining_courses:
			self.problem.addVariable(course, self.calc_course_offerings(course, fall_semesters, spring_semesters, summer_semesters))
		
		self.set_constraints()
		solutions =self.problem.getSolutions()
		return solutions



	# def clean_solution(self, solution):






		

