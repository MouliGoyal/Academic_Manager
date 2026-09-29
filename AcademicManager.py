# main.py
# Main program for the Study Management application

import timetable
import assignments
import scheduler
import progress

def show_menu() :
    print("===== Study Management Application =====")
    print("1. Add Class")
    print("2. View Timetable")
    print("3. Add Assignment")
    print("4. View Assignments")
    print("5. Add Study Hours")
    print("6. Generate Study Schedule")
    print("7. Mark Assignment as Completed")
    print("8. View Completed Assignments")
    print("9. Exit")

def main() :

    while True:
        show_menu()
        choice = input("Enter your choice : ")

        if choice == '1':
            timetable.add_class()

        elif choice == '2':
            timetable.view_timetable()

        elif choice == '3':
            assignments.add_assignment()

        elif choice == '4':
            assignments.view_assignments()

        elif choice == '5':
            scheduler.add_study_hours()

        elif choice == '6':
            scheduler.generate_plan()

        elif choice == '7':
            progress.mark_complete(assignments.assignments)
            
        elif choice == '8':
            progress.view_progress(assignments.assignments)

        elif choice == '9':
            print("Exiting the application. Goodbye!")
            
        else:
            print("Invalid choice. Please try again.")

main()