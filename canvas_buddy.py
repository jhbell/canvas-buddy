#! /usr/bin/env python3.5

"""CanvasBuddy

Canvas command line tool for students

With this application you can:
    View courses
    View grades
    View assignments

All from your command line

Author: Jeff Bell
"""

import canvas

class Colors:
    RED =       "\033[31m"
    GREEN =     "\033[32m"
    YELLOW =    "\033[33m"
    BLUE =      "\033[34m"

    RESET =     "\033[0m"

class CanvasBuddy:

    def select_course(self):
        """Select a course from the dashboard favorites"""
        courses_json = canvas.get_favorite_courses()
        selection = -1

        while selection <= 0 or selection > len(courses_json):
            try:
                print(Colors.YELLOW, "Please select a course below...", 
                        Colors.RESET)
                self.show_courses(courses_json)
                selection = int(input(">> "))
            except(ValueError):
                print(Colors.RED, "You must enter a number below!", Colors.RESET)

        selection_string = "You selected: {}".format(selection)
        print(selection_string)

        course_id = courses_json[selection - 1]["id"]

        return course_id

    def show_courses(self, courses_json):
        """Show an enumerated list of favorited courses"""
        print(Colors.GREEN, "🎓  Your Courses 🎓", Colors.RESET)
        course_count = 1
        for course in courses_json:
            name = course["name"]
            format_string = "{}{}.{} {}".format(Colors.BLUE, 
                    course_count, Colors.RESET, name)
            course_count += 1
            
            print(format_string)

    def show_assignments(self, course_id):
        """Show the grades for all assignments"""
        print(Colors.BLUE, "📓  Grades 📓", Colors.RESET)

        assignments_json = canvas.get_assignments(course_id)
        for assignment in assignments_json:
            name = str(assignment["name"])
            points_possible = str(assignment["points_possible"])
            assignment_id = assignment["id"]

            submissions_json = canvas.get_submissions(course_id, assignment_id)
            grade = str(submissions_json["grade"])

            format_string = "{:<50.45} {}{:<6.5}{}/{:>6.6}".format(name,
                    Colors.GREEN, grade, Colors.RESET, points_possible)
            print(format_string)


"""Begin script code"""
canvas_buddy = CanvasBuddy()
run = True

while run:
    course = canvas_buddy.select_course()
    canvas_buddy.show_assignments(course)

    try:
        print("Continue? (y/n)")
        selection = str(input(">> ")).lower()
        if selection != "y":
            run = False
    except(ValueError):
        pass

