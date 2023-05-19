if __name__ == '__main__':
    # Create a list (2D Array)
    students = []
    # Adding the logic
    for _ in range(int(input())):
        name = input()
        score = float(input())
       # Update the list
        students.append([name, score]) # 2D Array

    # Sort the list by score first, then by name
    students.sort(key= lambda col: (col[1], col[0]))

    # First value is the lowest
    lowest = second_lowest = students[0][1] # Starting we put the initial score first 
    value_update = 0
    i = 0
    size = len(students)

    # Loop through all second_max values in the list
    while i < size:
        if students[i][1] > second_lowest: # students[i][1] -> Grades
            second_lowest = students[i][1]
            value_update += 1
        if value_update == 1:
            print(students[i][0]) # Names
        # After finding the second lowest value, we're done 
        if lowest != second_lowest and value_update > 1:
            break
        i += 1

    # print(i)
    

        
