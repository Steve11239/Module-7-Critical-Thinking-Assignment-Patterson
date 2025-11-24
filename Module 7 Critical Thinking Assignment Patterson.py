#Student: Steve Patterson
#Contact Phone: 248.783.6493
#Contact School E-mail: hybridcalibratorsrule@gmail.com
#Contact Student E-mail: steven.patterson@csuglobal.edu
#Course Section: 25FD-CSC500-1 – Principles of Programming
#Course Module: Critical Thinking Module 7

# dictionary in a method to save the course and room number
def course_number_room():
    course_rooms = {
        "CSC101": 3004,
        "CSC102": 4501,
        "CSC103": 6755,
        "NET110": 1244,
        "COM241": 1411
    }
    return course_rooms
# dictionary in a method to save the course and instructor name
def course_number_instructor():
    course_instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }
    return course_instructors
# dictionary in a method to save the course and the starting time
def course_number_time():
    course_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }
    return course_times

def main():
    # call the methods and have the dictionary in a local copy
    rooms = course_number_room()
    instructors = course_number_instructor()
    times = course_number_time()
    # display the courses available for the user to choose from
    print("Please enter one of the following courses:")
    for course in rooms.keys():
        print(course)
    # continue to loop to allow for multiple entries
    while True:
        course_input = input("Enter a course number from the list provided: (or enter 'q' to quit)").upper()
        # if the user want to quit break the loop
        if course_input == "Q":
            print("Thank You and have a Great Semester!")
            break

        try:
            # grab the room, instructor and time from the dictionaries
            room = rooms[course_input]
            instructor = instructors[course_input]
            time = times[course_input]
            # print the requested information
            print("\nRequested Course Information")
            print(f"Course Number: {course_input}")
            print(f"Course Room: {room}")
            print(f"Course Instructor: {instructor}")
            print(f"Course Meeting Time: {time}")
            print("Have a great course!")
        # have an exception incase the user does not enter an available course
        except KeyError:
            print("\nError: This course could not be found, please try again.")

# the main
if __name__ == "__main__":
    main()


