# import statistics

students = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan", "Kate Walsh", "Shane Duffy"]
ages = [16, 17, 18, 17, 18, 15, 19]
marks = [90, 88, 50, 60, 100, 75, 95]

# Challenge 2
# Part 1
import matplotlib.pyplot as plt
plt.plot(students, marks, "ro")
plt.xlabel('Names')
plt.ylabel('Marks')
plt.title("Student marks")
plt.savefig("Plot1.png")
plt.show()

# Part 2 + 3
student_young = []
ages_young = []
marks_young = []
student_old = []
ages_old = []
marks_old = []
for i in range(len(ages)):
  if ages[i] <= 17:
    ages_young.append(ages[i])
    marks_young.append(marks[i])
    student_young.append(students[i])
  if ages[i] >= 18:
    ages_old.append(ages[i])
    marks_old.append(marks[i])
    student_old.append(students[i])

plt.plot(marks_young, "ro")
plt.plot(marks_old, "bs")
plt.ylabel('Marks')
plt.title("Student marks")
plt.savefig("Plot2.png")
plt.show()

# Part 4
average_young = sum(marks_young)/len(marks_young)
average_old = sum(marks_old)/len(marks_old)

averageGrades = [average_young, average_old]
xLabels = ["17 or younger", "18 or older"]

plt.bar(xLabels, averageGrades)
plt.xlabel("Ages")
plt.ylabel('Marks')
plt.title("Student average marks")
plt.savefig("Plot3.png")
plt.show()

