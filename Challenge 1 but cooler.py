#-----------------------------------------------------------------------------------------------------#

import statistics
from time import sleep as s
from os import system, name



#-----------------------------------------------------------------------------------------------------#

students = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan", "Kate Walsh", "Shane Duffy"]
ages = [16, 17, 18, 17, 18, 15, 19]
marks = [90, 88, 50, 60, 100, 75, 95]

#-----------------------------------------------------------------------------------------------------#


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'     # Just to make the output more colorful 
    RED = '\033[91m'
    WHITE = '\033[0m'  
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    

"""
[CHALLENGE ONE]
"""




# Part 1
print("")
print("")
print(bcolors.BOLD + bcolors.UNDERLINE + "Task One" + bcolors.WHITE)
total = 0
for i in range(len(ages)):
  total += ages[i]
print("")
average = total/len(ages)
print("")
print("The average age of the students is: ")
print("")
print(bcolors.GREEN + str(round(average,2))+ bcolors.WHITE)
print("")
print("")

# Part 2
print(bcolors.BOLD + bcolors.UNDERLINE + "Task Two" + bcolors.WHITE)
print("")
print(bcolors.WHITE + "The average mark of the students is: ")
print("")
average = sum(marks)/len(marks)
print(bcolors.GREEN + str(round(average,2)) + bcolors.WHITE)

# Part 3 + 4 
print("")
print("")
print(bcolors.UNDERLINE + bcolors.BOLD + "Task Three and Four" + bcolors.WHITE)
print("")
print(bcolors.WHITE + "The highest and lowest ages in the list are: " + bcolors.GREEN)
print("")
print(min(ages))
print(max(ages))
print("")
print(bcolors.WHITE + "The students' names of these ages are: " + bcolors.GREEN)
print("")
print(students[ages.index(min(ages))])
print(students[ages.index(max(ages))] + bcolors.WHITE)

# # Part 3 + 4 
# youngest = 100
# youngestIndex = -1
# oldest = 0
# oldestIndex = -1
# for i in range(len(ages)):
#   if ages[i] < youngest:
#     youngest = ages[i]
#     youngestIndex = i
#   if ages[i] > oldest:
#     oldest = ages[i]
#     oldestIndex = i

# print(students[youngestIndex],":",youngest)
# print(students[oldestIndex],":",oldest)

# Part 5
print("")
print("")
print(bcolors.UNDERLINE + bcolors.BOLD + "Task Five" + bcolors.WHITE)
orderedMarks = sorted(marks)
print("")
print(bcolors.GREEN + "The median mark is: ")
print("")
print(str(orderedMarks[len(orderedMarks)//2]) + bcolors.WHITE)





