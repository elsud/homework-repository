from datetime import datetime, timedelta

import pytest

from homework5.oop1 import Homework, Student, Teacher


@pytest.fixture()
def student():
    first_name, last_name = "Student's name", "Student's last name"
    return Student(first_name, last_name)


@pytest.fixture()
def teacher():
    first_name, last_name = "Teacher's name", "Teacher's last name"
    return Teacher(first_name, last_name)


@pytest.fixture()
def late_homework():
    return Homework("Some task", 0)


@pytest.fixture()
def homework():
    return Homework("Some task", 5)


def test_init_student(student):
    assert student.first_name == "Student's name"
    assert student.last_name == "Student's last name"


def test_init_teacher(teacher):
    assert teacher.first_name == "Teacher's name"
    assert teacher.last_name == "Teacher's last name"


def test_text_deadline_and_active_of_homework(homework):
    assert homework.text == "Some task"
    assert homework.deadline == timedelta(days=5)
    assert homework.is_active()


def test_homework_after_deadline_is_not_active(late_homework):
    assert not late_homework.is_active()


def test_creating_homework(teacher):
    text, deadline = "Learn functions", 0
    homework = teacher.create_homework(text, deadline)
    assert isinstance(homework, Homework)
    assert homework.text == text
    assert homework.deadline == timedelta(days=deadline)


def test_doing_homework_in_time(student, homework):
    assert student.do_homework(homework) == homework


def test_doing_homework_after_deadline(capsys, student, late_homework):
    student.do_homework(late_homework)
    out, _err = capsys.readouterr()
    assert out.strip() == "You are late"


def test_is_created_valid():
    before_creating = datetime.now()
    homework = Homework("Text", 4)
    after_creating = datetime.now()
    assert before_creating < homework.created < after_creating
