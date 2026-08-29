students = []

while True:
    name = input("Enter Student Name = ")
    if name == "n":
        break
    print("For Stop, press ,n,")

    students.append(name)

for no, name in enumerate(students, start=1):
    print(no, ".", name)