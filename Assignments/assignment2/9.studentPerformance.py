#9. You have a dictionary containing a list of students with their names and scores. For each student, calculate their average score. Based on the average, classify them as 'Excellent' (≥90), 'Good' (80-89), or 'Average' (<80). Store the results in a new dictionary and display them.

studentsMarks = {
    "AA": [95,92,88],
    "BB": [75,80,82],
    "CC": [85,88,84],
    "DD": [70,65,72],
    "EE": [10,40,50]
}       

studentAverage = {}

for name,scores in studentsMarks.items():
    avgScore = sum(scores)/len(scores)

    if avgScore >= 90:
        status = 'Excellent'
    elif avgScore >=80:
        status = 'Good'
    else:
        status ='Average'

    studentAverage[name] = {"Average": round(avgScore, 2), "Status": status}

for name, info in studentAverage.items():
    print(f"{name}: Average = {info['Average']}, Status = {info['Status']}")        

