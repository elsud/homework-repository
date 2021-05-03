"""Module with classes of Hoework, Student and Teacher.
Homework has text, deadline in days and datetime object when it was created.
Also it has method "is_active" which return boolean.
Student and Teacher has first_name and last_name.
Student can do omework whrn it's not deadline yet.
Teacher can create homework, give it text and deadline."""

import datetime


class Homework:
    """Class with text and deadline of homework."""

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        """Checking if homework can be done or it's too late."""
        return datetime.datetime.now() < self.deadline + self.created


class Student:
    """Class of student, can get homework to do."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework):
        """Doing homework if it's not deadline. Returns Homework object."""
        if not homework.is_active():
            print("You are late")
            return None
        return homework


class Teacher:
    """Class of teacher, which can create homework with text and deadline."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, deadline):
        """Creating Homework object."""
        return Homework(text, deadline)
