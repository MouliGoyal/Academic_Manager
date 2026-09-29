# scheduler.py
# This file creates a simple study plan

import assignments

study_hours = []

def add_study_hours():

    print("===== Add Study Hours =====")
    day = input("Enter day: " )
    time = input("Enter available time: ")

    study_hours.append((day,time))
    print("Study hours added successfully!")

def generate_plan():

    print("===== Study Plan =====")

    if len(assignments.assignments) == 0:
        print("No assignments added.")
        return

    if len(study_hours) == 0:
        print("No study hours added.")
        return

    number = 0

    for assignment in assignments.assignments:

        if assignment["completed"] == False:

            if number < len(study_hours):
                day, time = study_hours[number]
                print("Assignment:", assignment["name"])
                print("Study on: ", day)
                print("Study time:", time)

                number = number + 1

    