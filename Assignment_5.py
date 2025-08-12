# TASK1: Create a Dictionary of student Marks.

Students = {'Alice':85, 'Virat':25, 'Saurav':29, 'Ankush':25, 'Vijay':28}
m = input('Enter the student\'s name: ')
if m in Students:
    print(f'{m}\'s marks: {Students[m]}')
else:
    print("Student not found")

# TASK2: Demonstrate List Slicing:

list1 = list(range(1,11))
list1 = list1[:5]
print(list1)
list1.reverse()
print(list1)