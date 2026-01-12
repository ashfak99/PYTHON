students=[]

def add_student():
    print("\n---Add New Student---")
    name=input("Enter Name: ")
    roll_no=int(input("Enter Roll No: "))
    city=input("Enter City: ")
    student_data={
        "name": name,
        "roll": roll_no,
        "city": city
    }
    students.append(student_data)
    print(f"success! {name} added")

def search():
    print("\n---Search Student---")
    roll=int(input("Enter the roll no : "))
    found = False
    for s in students:
        if s["roll"] == roll:
            print("\n!!!STUDENT FOUND!!!\n")
            found=True
            print(f"Name : {s['name']}")
            print(f"City : {s['city']}")
            break
        if not found:
            print("Student not found")


while(True):
    choice=int(input("Please choose anyone.\n1.Add\n2.Search\n3.Show All\n4.Exit:  "))

    match choice:
        case 1:
            add_student()
        case 2:
            search()
        case 3:
            print(students)
        case 4:
            print("Bye Bye")
            break
        case _:
            print("!!!!!WRONG CHOICE!!!!!")