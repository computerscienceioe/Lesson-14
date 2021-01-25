
students = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan", "Kate Walsh", "Shane Duffy"]
ages = [16, 17, 18, 17, 18, 15, 19]
marks = [90, 88, 50, 60, 100, 75, 95]

# Challenge 3
# Part 1
grades = []
for i in range(len(marks)):
  if marks[i] <= 100 and marks[i] >= 90:
    grades.append("A")
  elif marks[i] < 90 and marks[i] >= 80:
    grades.append("B")
  elif marks[i] < 80 and marks[i] >= 70:
    grades.append("C")
  elif marks[i] < 70 and marks[i] >= 60:
    grades.append("D")
  elif marks[i] < 60 and marks[i] >= 0:
    grades.append("F")

print(grades)

# Part 2
possible_grades = ["A", "B", "C", "D", "F"]
frequency_grades = [0, 0, 0, 0, 0]
# Option 1
# for i in range(len(grades)):
#   if grades[i] == possible_grades[0]:
#     frequency_grades[0] += 1
#   elif grades[i] == possible_grades[1]:
#     frequency_grades[1] += 1
#   elif grades[i] == possible_grades[2]:
#     frequency_grades[2] += 1
#   elif grades[i] == possible_grades[3]:
#     frequency_grades[3] += 1
#   elif grades[i] == possible_grades[4]:
#     frequency_grades[4] += 1

# Option 2
for i in range(len(grades)):
  for j in range(len(possible_grades)):
    if grades[i] == possible_grades[j]:
      frequency_grades[j] += 1

print(frequency_grades)

import matplotlib.pyplot as plt
plt.bar(possible_grades, frequency_grades)
plt.xlabel("Grades")
plt.ylabel('Frequency')
plt.title("Frequency of student grades")
plt.savefig("Plot1.png")
plt.show()

# Part 3
plt.pie(frequency_grades, labels=possible_grades)
plt.title("Frequency of student grades")
plt.savefig("Plot2.png")
plt.show()
