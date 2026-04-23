students = []

def calculate_result(name, maths, science, english):

    total = maths + science + english
    percentage = total / 3

    if maths >= 35 and science >= 35 and english >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "D"

    student = {
        "name": name,
        "total": total,
        "percentage": percentage,
        "result": result,
        "grade": grade
    }

    students.append(student)


def show_all():

    if len(students) == 0:
        print("\nNo records found.")
        return

    print("\n📋 ALL STUDENT RESULTS")

    for s in students:
        print("----------------------")
        print("Name:", s["name"])
        print("Total:", s["total"])
        print("Percentage:", round(s["percentage"],2))
        print("Result:", s["result"])
        print("Grade:", s["grade"])


def search_student():

    name = input("\nEnter student name to search: ")

    found = False

    for s in students:
        if s["name"].lower() == name.lower():
            print("\nStudent Found")
            print("Name:", s["name"])
            print("Percentage:", round(s["percentage"],2))
            print("Grade:", s["grade"])
            found = True

    if found == False:
        print("Student not found.")


def show_topper():

    if len(students) == 0:
        print("\nNo records found.")
        return

    topper = students[0]

    for s in students:
        if s["percentage"] > topper["percentage"]:
            topper = s

    print("\n🏆 TOPPER")
    print("Name:", topper["name"])
    print("Percentage:", round(topper["percentage"],2))


def failed_students():

    print("\n❌ FAILED STUDENTS")

    found = False

    for s in students:
        if s["result"] == "FAIL":
            print(s["name"])
            found = True

    if found == False:
        print("No failed students.")


while True:

    print("\n📚 STUDENT RESULT MANAGER")
    print("1. Add Student Result")
    print("2. Show All Results")
    print("3. Search Student")
    print("4. Show Topper")
    print("5. Failed Students")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        maths = int(input("Maths Marks: "))
        science = int(input("Science Marks: "))
        english = int(input("English Marks: "))

        calculate_result(name, maths, science, english)

        print("Record Added Successfully!")

    elif choice == "2":
        show_all()

    elif choice == "3":
        search_student()

    elif choice == "4":
        show_topper()

    elif choice == "5":
        failed_students()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")