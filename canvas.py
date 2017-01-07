"""Module for interacting with Canvas

Author: Jeff Bell
"""

import requests
import auth

_ROOT_URL = "https://utexas.instructure.com/api/v1"

def get_json(request_path):
    """Return the JSON result for the given request path"""
    url = _ROOT_URL + request_path
    params = {"access_token" : auth.TOKEN, "per_page" : 50}
    response = requests.get(url, params=params)
    response = response.json()
    return response

def get_favorite_courses():
    """Return JSON response for user's favorite courses"""
    path = "/users/self/favorites/courses"
    return get_json(path)

def get_assignments(course_id):
    """Get assignments for given course"""
    path = "/courses/{}/assignments".format(course_id)
    return get_json(path)

def get_submissions(course_id, assignment_id):
    """Get submissions for given assignment"""
    path = "/courses/{}/assignments/{}/submissions/self".format(course_id, 
            assignment_id)
    return get_json(path)
