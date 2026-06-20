import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Ravi", 85])
    writer.writerow(["Priya", 90])
    writer.writerow(["Kiran", 78])

print("Data written successfully")





import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)





with open("sample.txt", "r") as file:
    data = file.read()

words = data.split()
print("Number of words:", len(words))