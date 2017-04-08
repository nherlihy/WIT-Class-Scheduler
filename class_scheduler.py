from constraint import *

from datetime import datetime

SEMESTERS = (("FALL", 0), ("SPRING", 1), ("SUMMER", 2))

class ClassScheduler:

	def __init__(self, courses, prerequisites, offerings, credits):
		self.courses = courses
		self.prerequisites = prerequisites
		self.offerings = offerings
		self.credits = credits
		self.remaining_courses = self.get_remaining_courses()
		self.current_semester = self.get_starting_semester()
		self.problem = Problem()

	def get_remaining_courses(self):
		return list(set(self.courses) - set(self.credits))

	def get_starting_semester(self):
		now = datetime.now()
		month = now.month

		if month in range(1,5):
			current_semester = SEMESTERS[2]
		elif month in range(5,9):
			current_semester = SEMESTERS[0]
		else:
			current_semester = SEMESTERS[1]

		return current_semester

	def solve(self):
		if (len(self.remaining_courses) % 4) == 0:
			remaining_semesters = len(self.remaining_courses) / 4
		else:
			remaining_semesters = (len(self.remaining_courses) / 4) + 1

		for course in self.remaining_courses:
			semester_offerings = []
			if course in self.offerings:
				offered = self.offerings[course]
				if offered[0]:
					semester_offerings.append(1)
				if offered[1]:
					semester_offerings.append(2)
				if offered[2]:
					semester_offerings.append(3)
			
			else:
				map(lambda num:semester_offerings.append(num), xrange(1,4))

			self.problem.addVariable(course, semester_offerings)


		print self.problem._variables
		for course in self.remaining_courses:
			if course in self.prerequisites:
				for req in self.prerequisites[course]:
					if req not in self.credits:
						self.problem.addConstraint(lambda course1, course2: course1 > course2, [course, req])

		self.problem.addConstraint(SomeInSetConstraint([3], 4, True))
		return self.problem.getSolutions()




		

