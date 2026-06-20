'''
,value
convert into table formate

'''


import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Ravi", 85])
    writer.writerow(["Priya", 90])
    writer.writerow(["Kiran", 78])

print("Data written successfully")








