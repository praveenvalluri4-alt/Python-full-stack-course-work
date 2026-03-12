"""
#star patterns

def star_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1,end="")
        print("")
n=int(input("enter your number:"))
star_pattern(n)
"""
"""
#attendence tracker

student_name =
student_status+

def show_menu():
    print("\n----attendence tracker----")
    print("1. add attendence")
    print("2.view attendence")
    print("3.exit")

    """
# Attendance Tracker

student_name = ""
student_status = ""

def show_menu():
    print("\n--- Attendance Tracker ---")
    print("1. Add Attendance")
    print("2. View Attendance")
    print("3. Exit")

def add_attendance():
    global student_name
    global student_status

    student_name = input("Enter name: ")
    student_status = input("Enter status (Present/Absent): ")

    print("Attendance added successfully")

def view_attendance():
    if student_name == "":
        print("No attendance record")
    else:
        print("\n--- Attendance Record ---")
        print(student_name, "-", student_status)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            print("Exiting the program")
            break

        else:
            print("Invalid choice")

main()