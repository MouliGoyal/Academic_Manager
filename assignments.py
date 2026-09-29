# assignments.py
# This file manages student assignments 

assignments = []

def add_assignment():

    print("===== Add Assignment =====")
    name = input("Enter assignment name: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline: ")

    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Enter priority : ")

    if choice == '1':
        priority = "High"
    elif choice == '2':
        priority = "Medium"
    else :
        priority = "Low"

    assignment = {
        "name": name,
        "subject": subject,
        "deadline": deadline,
        "priority": priority,
        "completed": False
    }

    assignments.append(assignment)

    print("Assignment added successfully!")

def view_assignments():

    print("===== Assignments =====")
    
    if len(assignments) == 0:
        print("No assignments added.")
    else:
        for assignment in assignments:

            print("Name:", assignment["name"])
            print("Subject:", assignment["subject"])
            print("Deadline:", assignment["deadline"])
            print("Priority:", assignment["priority"])

            if assignment["completed"]:
                print("Status: Completed")
            else:
                print("Status: Pending")

            print()


                