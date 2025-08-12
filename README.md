### TASK1: Create a Dictionary of Student Marks

1. Dictionary creation:
  * Students is a dictionary that stores student names as keys and their marks as values.
  * Example: 'Alice': 85 means Alice scored 85 marks.

2. Taking user input:
  * The program prompts the user to enter the name of a student with:
          m = input('Enter the student\'s name: ')
  * The user types a name (like "Virat").

3. Checking if student exists:
  * if m in Students: checks if the entered name exists as a key in the Students dictionary.
  * This means it looks to see if the student is in the list.

4. Displaying marks or error message:
  * If the student exists in the dictionary, it prints the student’s name and their marks:
          print(f'{m}\'s marks: {Students[m]}')
  *  For example, if the user inputs "Virat", the program outputs:
  *  Virat's marks: 25
  * If the student does not exist, it prints:
          print("Student not found")

### TASK2: Demonstrate List Slicing 

1. list(range(1, 11))
  * Creates a list of numbers from 1 to 10:
  * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

2. list1 = list1[:5]
  * Slices the first 5 elements of the list, so now list1 becomes:
  * [1, 2, 3, 4, 5]

3. print(list1)
  * Prints the sliced list:
  * [1, 2, 3, 4, 5]

4. list1.reverse()
  * Reverses list1 in place (changes original list):
  * Now list1 becomes:
  * [5, 4, 3, 2, 1]

5. print(list1)
  * Prints the reversed list:
  * [5, 4, 3, 2, 1]
