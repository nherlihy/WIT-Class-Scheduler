import sys
import operator
from constraint import *
from datetime import datetime

tracking_sheet_list = ["Comp1000", "Math2300", "Math1750", "English1",
                       "Comp1050", "Comp1200", "Math1850", "English2",
                       "Comp2000", "Comp2100", "Math2860", "HUSS1",
                       "Comp2350", "Comp2650", "Math2100", "HUSS2",
                       "Coop3000",
                       "Comp3400", "Comp1", "MathSci1", "HUSS3",
                       "Coop4000",
                       "Comp3350", "Comp3450", "Comp2", "MathSci2",
                       "Coop6000",
                       "Comp4960", "Comp3", "Comp4", "HUSS4",
                       "Comp5500", "Comp5", "MathSci3", "HUSS5"]

offerings = {"Comp1000": [True, True, False],
             "Math2300": [True, True, True],
             "Math1750": [True, True, False],
             "Comp1050": [True, True, False],
             "Math1850": [True, True, True],
             "Comp1200": [True, True, False],
             "Comp2000": [True, True, False],
             "Comp2100": [True, True, False],
             "Math2860": [True, True, False],
             "Comp2350": [True, True, False],
             "Comp2650": [True, True, False],
             "Math2100": [False, True, True],
             "Comp3400": [True, False, False],
             "Comp3350": [False, False, True],
             "Comp3450": [False, False, True],
             "Comp4960": [False, True, False],
             "Comp5500": [False, False, True]
             }

prerequisite_list = {"Math1850": ["Math1750"],
                     "Math2100": ["Math1850"],
                     "Math2860": ["Math1850"],
                     "Math2100": ["Math1850"],
                     "Comp1050": ["Comp1000"],
                     "Comp1200": ["Comp1000", "Math2300"],
                     "Comp2100": ["Comp1050", "Comp1200"],
                     "Comp2350": ["Comp1050", "Comp1200"],
                     "Comp2000": ["Comp1050", "Comp1200"],
                     "Comp2650": ["Comp1050", "Math2300"],
                     "Math2860": ["Math1850"],
                     "Comp3450": ["Comp2100", "Comp2350", "Comp2000"],
                     "Comp3350": ["Comp2350", "Comp2000"],
                     "Comp3400": ["Comp2350", "Comp2000"],
                     "Comp4960": ["Comp2350", "Comp2000", "Comp2650"]
                     }

problem = Problem()

for course in tracking_sheet_list:
	semester_offerings = []
	if course in offerings:
		offered = offerings[course]
		if offered[0]:
			semester_offerings.append(1)
			semester_offerings.append(4)
			semester_offerings.append(7)
		if offered[1]:
			semester_offerings.append(2)
			semester_offerings.append(5)
			semester_offerings.append(8)
		if offered[2]:
			semester_offerings.append(3)
			semester_offerings.append(6)
			semester_offerings.append(9)
	else:
		map(lambda num:semester_offerings.append(num), xrange(1,10))
	
	problem.addVariable(course, semester_offerings)

for key,courses in prerequisite_list.iteritems():
	for course in courses:
		problem.addConstraint(lambda course1, course2: course1 > course2, [key, course])

# for num in range(1,9):
# 	problem.addConstraint(SomeInSetConstraint([num], 4, True))
problem.addConstraint(SomeInSetConstraint([1], 4, True))
problem.addConstraint(SomeInSetConstraint([2], 4, True))
problem.addConstraint(SomeInSetConstraint([3], 4, True))
problem.addConstraint(SomeInSetConstraint([4], 4, True))
# problem.addConstraint(SomeInSetConstraint([5], 4, True))

time_start = datetime.now()
print "Start: %s\n" % time_start
solution = problem.getSolution()
time_finish = datetime.now()
print "Finish: %s\n" % time_finish
print solution

# for sol in solutions:
# 	print sol
# 	print "\n\n\n"






# max_val = solution[max(solution, key=lambda i: solution[i])]
# sorted_dict = sorted(solution.items(), key=lambda x:x[1])


# print "MAX: %s" % max_val

# for item in sorted_dict:
# 	course, semester_num = item
# 	print "%s --- %s" % (course, semester_num) 


	




