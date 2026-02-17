grade_one = float(input("Enter the first grade: "))
grade_two = float(input("Enter the second grade: "))
grade_tree = float(input("Enter the third grade: "))

average = sum([grade_one, grade_two, grade_tree]) / 3
# average = (grade_one + grade_two + grade_tree) / 3

print(f"The average of the three grades is: {average:.2f}")
