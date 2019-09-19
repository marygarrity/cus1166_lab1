def average_grade(roster): #accepts as input a list of Student Objects

    sum = 0
    avg = 0

    for student in roster:
        sum = sum + student.get_grade() #add up all grades

    # avg is sum divided by number of students in roster
    avg = sum / len(roster) #or just divide by 10
    return avg #returns average of current roster

#math is correct
