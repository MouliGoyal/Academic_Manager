#progress.py
#This file manages the progress of assignments

def mark_complete(assignments):
    if len(assignments) == 0:
        print("No assignments ")
        return

    for i in range(len(assignments)):
        print(i + 1, assignments[i]["name"])

    choice = int(input("Enter number: "))

    if choice >= 1 and choice <= len(assignments):
        assignments[choice - 1]["completed"] = True
        print("Completed!")
    else:
        print(" Invalid choice ")

def view_progress(assignments):
    completed = 0

    for assignment in assignments:
        if assignment["completed"]:
            completed += 1

    print("Total:", len(assignments))
    print("Completed:", completed)
    print("Pending:", len(assignments) - completed)