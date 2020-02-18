tutorgroups=[["Year one",15,18,16],
            ["Year two",17,13,12],
            ["Year three",14,21,12],
            ["Year four",15,15,15],
            ["Year five",16,16,16]]
schoolTotal=0
year1Total=0
year2Total=0
year3Total=0
year4Total=0
year5Total=0
aboveAverage=0
belowAverage=0
#total number of student in the school
for a in range(0,5):
    for b in range(1,4):
        schoolTotal+=tutorgroups[a][b]
print("The total number of student in the school is",schoolTotal)

#total number of student in each year
for c in range(1,4):
    year1Total+=tutorgroups[0][c]
    year2Total+=tutorgroups[1][c]
    year3Total+=tutorgroups[2][c]
    year4Total+=tutorgroups[3][c]
    year5Total+=tutorgroups[4][c]
print("The total number of student in year 1 is",year1Total)
print("The total number of student in year 2 is",year2Total)
print("The total number of student in year 3 is",year3Total)
print("The total number of student in year 4 is",year4Total)
print("The total number of student in year 5 is",year5Total)

#average tutor group size
averageSize=schoolTotal/15
print("The average tutor group size is",averageSize)

#above and below average groups
for a in range(0,5):
    for b in range(1,4):
        if tutorgroups[a][b]>averageSize:
            aboveAverage+=1
        elif tutorgroups[a][b]<averageSize:
            belowAverage+=1
print("The number of tutor groups above the average size are",aboveAverage)
print("The number of tutor groups below the average size are",belowAverage)
