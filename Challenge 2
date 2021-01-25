import matplotlib.pyplot as plt

students = [
    "John Smith", "Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan",
    "Kate Walsh", "Shane Duffy"
]
ages = [16, 17, 18, 17, 18, 15, 19]
marks = [90, 88, 50, 60, 100, 75, 95]

ages_young = []
marks_young = []
students_young = []
ages_older = []
marks_older = []

x_axis = ['17 or younger', '18 or older']

for i in range(len(ages)):
    if ages[i] <= 17:
        ages_young.append(ages[i])
        marks_young.append(marks[i])
    elif ages[i] <= 18:
        ages_older.append(ages[i])
        marks_older.append(marks[i])

average_young = sum(marks_young) / len(marks_young)
average_older = sum(marks_older) / len(marks_older)

print(average_young)
print(average_older)


plt.bar(x_axis, average_young, color=(0,0.5,0))
plt.bar(x_axis, average_older, color=(0,0.5,0))
plt.title("Average marks in different age groups")
plt.ylabel("Average Marks")
plt.show()
