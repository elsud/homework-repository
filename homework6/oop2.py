"""Module with classes of Homework, HomeworkResult, Student and Teacher.

Homework has such attributes as text, deadline in days and datetime object
when it was created. Also it has method showing is task active or it's too late.

Student and Teacher inherit from Person attributes of first_name and last_name.
Student can do homework by getting Homework object and returning
HomeworkResult object when it's not deadline yet.

Teacher can create Homework by giving it text and deadline, check homework
by getting HomeworkResult and checking if the length of solution string is more than 5 symbols.
Also he has class attribute homework_done which keeps as a dict all successfully
checked HomeworkResults without their repeating grouped by Homework as a key.
Teacher can reset results of specific Homework or reset all items of homework_done.

HomeworkResult instance gets student, homework and string with solution.
It has attributes of homework for coincident object, solution for string with solution,
author with instance of student and created with datetime object.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Exception which raises when student try to do homework after deadline"""


class Person:
    """Parent class for initialization of Teacher and Student."""

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Homework:
    """Class with text and deadline of homework."""

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Checking if homework can be done or it's too late."""
        return datetime.datetime.now() < self.deadline + self.created


class HomeworkResult:
    """Class with solution of homework. Checks if it gets Homework object."""

    def __init__(self, student: object, homework: object, solution: str):
        self.author = student
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.created = datetime.datetime.now()


class Student(Person):
    """Class of student, can get homework to do."""

    def do_homework(self, homework: object, solution: str) -> HomeworkResult:
        """Doing homework if it's not deadline."""
        if not homework.is_active():
            raise DeadlineError("You are late")
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    """Class of teacher, which can create homework with text and deadline,
    check homework and save it in homework_done or delete it from homework_done."""

    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Creating Homework object."""
        return Homework(text, deadline)

    def check_homework(self, homework_result: object) -> bool:
        """Checking if the length of solution is more than 5 symbols
        and adding HomeworkResult to homework_done if it's True."""
        if len(homework_result.solution) > 5:
            self.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: object = None) -> None:
        """Deleting solutions of Homework from homework_done or clearing
        all homework_done if there isn't any given Homework."""
        if isinstance(homework, Homework):
            del cls.homework_done[homework]
        else:
            cls.homework_done.clear()
