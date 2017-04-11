from datetime import datetime
from class_scheduler import ClassScheduler

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

prerequisite_list = {"Math1850": ["Math1750"],
                     "Math2100": ["Math1850"],
                     "Math2860": ["Math1850"],
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

credits_list = [ "Coop3000", "Coop4000" ,"Coop6000" ,"Comp1000" , "Math2300", "Math1750", "English1",
                       "Comp1050", "Comp1200", "Math1850", "English2",
                       "Comp2000", "Comp2100", "Math2860", "HUSS1",
                       "Comp2350", "Comp2650", "Math2100", "HUSS2",
                      
                       "Comp3400", "Comp1", "MathSci1", "HUSS3",
                       
                       "Comp3350", "Comp3450", "Comp2", "MathSci2",

                       "Comp4960", "Comp3", "Comp4", "HUSS4",
                       "Comp5500", "Comp5", "MathSci3", "HUSS5"]

classes_per_semester = 4
scheduler = ClassScheduler(tracking_sheet_list, prerequisite_list, offerings, credits_list, classes_per_semester)
time_start = datetime.now()
print "Start: %s\n" % time_start
for solution in scheduler.solve():
  print solution

time_finish = datetime.now()
print "\nFinish: %s\n" % time_finish
