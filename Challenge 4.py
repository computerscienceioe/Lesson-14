students = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan", "Kate Walsh", "Shane Duffy"]
ages = [16, 17, 18, 17, 18, 15, 19]
marks = [90, 88, 50, 60, 100, 75, 95]

# Zips all the lists together.
# The list we want to sort by must be first
zipped_lists = zip(students, marks)
# Sorts the lists
sorted_pairs = sorted(zipped_lists)
# Unzips the lists
tuples = zip(*sorted_pairs)
# Breaks the combined list back into individual lists
sorted_students, sorted_marks = [ list(tuple) for tuple in tuples]

# Prints the sorted lists
print(sorted_marks)
print(sorted_students)

stop = 0
for i in range(len(sorted_students)):
  if (sorted_students[i][0] <= "L"):
    stop += 1


print(stop)
a_l_students = sorted_students[:stop]
a_l_marks = sorted_marks[:stop]
print(a_l_students)
print(a_l_marks)

# Part 1
import statistics
a_l_average_mark = statistics.mean(a_l_marks)
print(a_l_average_mark);

import matplotlib.pyplot as plt
plt.plot(a_l_students, a_l_marks)
plt.show()


# Part 2
zipped_lists = zip(a_l_marks, a_l_students)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
sorted_marks, sorted_students = [ list(tuple) for tuple in tuples]

plt.plot(sorted_students, sorted_marks)
plt.show()

# Part 3
median_mark = statistics.median(marks)
median_student = students[marks.index(median_mark)]
print(median_mark)
print(median_student)
