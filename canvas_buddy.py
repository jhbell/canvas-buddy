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

import requests
import auth

class CanvasBuddy:

    def __init__(self):
        self._ROOT_URL = "https://utexas.instructure.com/api/v1"

    def get_favorite_courses(self):
        """Return the request json for favorite courses"""
        path = "/users/self/favorites/courses"

        return self.get_json(path)

    def show_courses(self, courses_json):
        course_count = 1
        for course in courses_json:
            name = course["name"]
            format_string = "{}. {}".format(course_count, name)
            course_count += 1
            
            print(format_string)

    def select_course(self):
        courses_json = self.get_favorite_courses()
        self.show_courses(courses_json)
        selection = int(input(">> "))
        selection_string = "You selected: {}".format(selection)
        print(selection_string)

    def get_json(self, request_path):
        url = "".join([self._ROOT_URL, request_path])
        auth_token = {"access_token" : auth.TOKEN}

        response = requests.get(url, params=auth_token)
        response = response.json()

        return response

"""Begin script portion"""
canvas_buddy = CanvasBuddy()

canvas_buddy.select_course()
