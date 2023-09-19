if __name__ == '__main__':
    # Initialize an empty list to store student names and grades
    students = []

    # Get the number of students from the user
    n = int(input())

    # Get the student names and grades
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    scores = sorted(list(set([score for name, score in students])))
    second_lowest_score = scores[1]

    # Get the names of students with the second lowest grade
    second_lowest_students = sorted([name for name, score in students if score == second_lowest_score])

    # Print the names of students with the second lowest grade
    for student in second_lowest_students:
        print(student)