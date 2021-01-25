students = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan", "Kate Walsh", "Shane Duffy"]
ages = [16, 17, 18, 17, 18, 15, 19]
marks = [90, 88, 50, 60, 100, 75, 95]


zipped_lists = zip(students, marks)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
sorted_students, sorted_marks = [ list(tuple) for tuple in tuples]

# Part 2
import matplotlib.pyplot as plt
zipped_lists = zip(marks, students)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
sorted_marks, sorted_students = [ list(tuple) for tuple in tuples]

plt.bar(sorted_students, sorted_marks)
plt.savefig("1MarksAscending.png")
plt.show()

# Part 3
zipped_lists = zip(marks, students)
sorted_pairs = sorted(zipped_lists, reverse = True)
tuples = zip(*sorted_pairs)
sorted_marks, sorted_students = [ list(tuple) for tuple in tuples]

plt.bar(sorted_students, sorted_marks)
plt.savefig("2MarksDescending.png")
plt.show()

# Part 4
zipped_lists = zip(students, ages)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
sorted_students, sorted_ages = [ list(tuple) for tuple in tuples]

plt.plot(sorted_students, sorted_ages)
plt.savefig("3StudentsAlphabetical.png")
plt.show()

# Part 5
zipped_lists = zip(students, ages)
sorted_pairs = sorted(zipped_lists, reverse = True)
tuples = zip(*sorted_pairs)
sorted_students, sorted_ages = [ list(tuple) for tuple in tuples]

plt.plot(sorted_students, sorted_ages)
plt.savefig("4StudentsReverseAlphabetical.png")
plt.show()

# Part 6
zipped_lists = zip(ages, students)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
sorted_ages, sorted_students = [ list(tuple) for tuple in tuples]

plt.plot(sorted_students, sorted_ages)
plt.savefig("5AgesAscending.png")
plt.show()

# Part 7
zipped_lists = zip(ages, students)
sorted_pairs = sorted(zipped_lists, reverse = True)
tuples = zip(*sorted_pairs)
sorted_ages, sorted_students = [ list(tuple) for tuple in tuples]

plt.plot(sorted_students, sorted_ages)
plt.savefig("6AgesDescending.png")
plt.show()
