# import statistics

students = ["John Smith","Jane Doe", "Mary Murphy", "Michael Lawlor", "Conor Whelan", "Kate Walsh", "Shane Duffy"]
ages = [16, 17, 18, 17, 18, 15, 19]
marks = [90, 88, 50, 60, 100, 75, 95]

# Challenge 1
# Part 1
total = 0
for i in range(len(ages)):
  total += ages[i]
print(total)
average = total/len(ages)
print(round(average,2))

# Part 2
average = sum(marks)/len(marks)
print(round(average,2))

# Part 3 + 4 option 1
print(min(ages))
print(max(ages))
print(ages.index(min(ages)))
print(ages.index(max(ages)))
print(students[ages.index(min(ages))])
print(students[ages.index(max(ages))])

# Part 3 + 4 option 2
youngest = 100
youngestIndex = -1
oldest = 0
oldestIndex = -1
for i in range(len(ages)):
  if ages[i] < youngest:
    youngest = ages[i]
    youngestIndex = i
  if ages[i] > oldest:
    oldest = ages[i]
    oldestIndex = i

print(students[youngestIndex],":",youngest)
print(students[oldestIndex],":",oldest)

# Part 5
orderedMarks = sorted(marks)
print(orderedMarks)
print(orderedMarks[len(orderedMarks)//2])
