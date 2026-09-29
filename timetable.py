#timetable.py
#This file manages the college timetable

timetable = []

def add_class():

    print("===== Add Class =====")
    day = input("Enter day: ")
    subject = input("Enter subject: ")
    time = input("Enter class time: ")

    class_info = {
        "day": day,
        "subject": subject,
        "time": time
    }

    timetable.append(class_info)
    print("Class added successfully!")

def view_timetable():
    print("===== Timetable =====")
    
    if len(timetable) == 0:
        print("No classes scheduled.")
    else:
        for class_info in timetable:
            print(
                class_info["day"],
                class_info["time"],
                class_info["subject"]
            )
