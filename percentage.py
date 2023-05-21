if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # Creating a list of student names and marks
        name, *line = input().split()
        # Converting into float type 
        scores = list(map(float, line))
        # Creating a dictionary of student name and marks for eg. {A[56.0, 84.0, 90.0]}
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name] # query name from the user

    # For 2 decimal we use format(value, '.nf') n => upto how much decimal points
    print(format(sum(marks) / 3, '.2f'))

