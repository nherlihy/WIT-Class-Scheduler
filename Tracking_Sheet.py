import itertools
import collections
import Queue

tracking_sheet_list = [["Comp1000", "Math2300", "Math1750", "English"],
["Comp1050", "Comp1200", "Math1850", "English"],
["Comp2000", "Comp2100", "Math2860", "HUSS"],
["Comp2350", "Comp2650", "Math2100", "HUSS"],
["Coop3000"],
["Comp3400", "Comp", "MathSci", "HUSS"],
["Coop4000"],
["Comp3350", "Comp3450", "Comp", "MathSci"],
["Coop6000"],
["Comp4960", "Comp", "Comp", "HUSS"],
["Comp5500", "Comp", "MathSci", "HUSS"]]

# Requirements to graduate BSCS

prerequisite_list = {"Math1850" : ["Math1750"],
"Math2100" : ["Math1850"],
"Math2860" : ["Math1850"],
"Math2100" : ["Math1850"],
"Comp1050" : ["Comp1000"],
"Comp1200" : ["Comp1000", "Math2300"],
"Comp2100" : ["Comp1050", "Comp1200"],
"Comp2350" : ["Comp1050", "Comp1200"],
"Comp2000" : ["Comp1050", "Comp1200"],
"Comp2650" : ["Comp1050", "Math2300"],
"Math2860" : ["Math1850"],
"Comp3450" : ["Comp2100", "Comp2350", "Comp2000"],
"Comp3350" : ["Comp2350", "Comp2000"],
"Comp3400" : ["Comp2350", "Comp2000"],
"Comp4960" : ["Comp2350", "Comp2000", "Comp2650"]
}

# Classes needed in order to take a specific class

offerings = {"Comp1000" : [True, True, False],
"Math2300" : [True, True, True],
"Math1750" : [True, True, False],
"Comp1050" : [True, True, False],
"Math1850" : [True, True, True],
"Comp1200" : [True, True, False],
"Comp2000" : [True, True, False],
"Comp2100" : [True, True, False],
"Math2860" : [True, True, False],
"Comp2350" : [True, True, False],
"Comp2650" : [True, True, False],
"Math2100" : [False, True, True],
"Comp3400" : [True, False, False],
"Comp3350" : [False, False, True],
"Comp3450" : [False, False, True],
"Comp4960" : [False, True, False],
"Comp5500" : [False, False, True]
}

# When the classes are offered, based on (fall, spring, summer) semesters

credits_list = ["Comp1000", "Math2300", "Math1750", "English",
"Comp1050", "Comp1200", "Math1850", "English", "Comp2100", "Math2860", "HUSS",
"Comp2350", "Comp2650", "Math2100", "HUSS",
"Coop3000",
"Comp3400", "Comp", "MathSci", "HUSS",
"Coop4000",
"Comp3350", "Comp", "MathSci",
"Coop6000",
"Comp4960", "Comp", "Comp", "HUSS"]

SEMESTERS = (("FALL", 0), ("SPRING", 1), ("SUMMER", 2))
SEMESTER_NAME, SEMESTER_INDEX = SEMESTERS[1]

print "Current semester: ", SEMESTER_NAME
print "Semeseter index: ", SEMESTER_INDEX

# Classes already taken

flattened_tracking_sheet  = list(itertools.chain(*tracking_sheet_list))

# Converts the tracking_sheet_list from a list of lists to a list

counted_classes = collections.Counter(flattened_tracking_sheet) - collections.Counter(credits_list)

# Compares the difference in both lists

# Converts counter to a list and prints

#if counted_classes has a class that is in the prerequisite_list then make sure the class has been taken in credits_list
#if counted_classes has a class in offerings then make sure its in the correct season

for counted_class in counted_classes:
    print counted_class
    if counted_class in prerequisite_list:
# Loop through all courses that have given course as a prerequisite
        for prereq_class in prerequisite_list[counted_class]:
            if prereq_class not in credits_list:
                print "error class not taken: ", prereq_class
                if prereq_class in offerings:
                    if offerings[prereq_class][SEMESTER_INDEX]:
                        print "class is offered this semester"
                    else:
                        print "class is not offered this semeseter"
                else:
                    print "Class is offered every semester"
