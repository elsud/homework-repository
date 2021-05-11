from datetime import datetime, timedelta

import pytest

from homework6.oop2 import DeadlineError, Homework, HomeworkResult, Student, Teacher


@pytest.fixture
def student():
    first_name, last_name = "Student's name", "Student's last name"
    return Student(first_name, last_name)


@pytest.fixture
def teacher():
    first_name, last_name = "Teacher's name", "Teacher's last name"
    return Teacher(first_name, last_name)


@pytest.fixture
def late_homework():
    return Homework("Some task", 0)


@pytest.fixture
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
    result = student.do_homework(homework, "solution")
    assert isinstance(result, HomeworkResult)


def test_doing_homework_after_deadline(student, late_homework):
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(late_homework, "solution")


def test_if_init_of_homeworkresult_raises_error_when_it_gets_not_homework(student):
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(student, "homework", "solution")


def test_init_of_homeworkresult_when_it_gets_homework(student, homework):
    result = HomeworkResult(student, homework, "solution")
    assert result.author == student
    assert result.homework == homework
    assert result.solution == "solution"


def test_if_created_of_homeworkresult_valid(student, homework):
    before_creating = datetime.now()
    result = HomeworkResult(student, homework, "solution")
    after_creating = datetime.now()
    assert before_creating < result.created < after_creating


def test_is_created_of_homework_valid():
    before_creating = datetime.now()
    homework = Homework("Text", 4)
    after_creating = datetime.now()
    assert before_creating < homework.created < after_creating


def test_if_teacher_creates_homework(teacher):
    assert isinstance(teacher.create_homework("text", 2), Homework)


def test_check_homework_with_solution_less_than_5_gives_false(
    teacher, homework, student
):
    result = student.do_homework(homework, "1")
    assert not teacher.check_homework(result)
    assert not teacher.homework_done


def test_check_homework_with_solution_longer_than_5_gives_true_and_saves_in_homework_done(
    teacher, homework, student
):
    result = student.do_homework(homework, "123456")
    assert teacher.check_homework(result)
    assert teacher.homework_done[homework] == {result}


def test_reset_results_with_given_homework_deletes_this_homework_from_homework_done(
    teacher, homework, student
):
    Teacher.reset_results()
    result_1 = student.do_homework(homework, "solution")
    homework_2 = teacher.create_homework("another", 3)
    result_2 = student.do_homework(homework_2, "solution")
    teacher.check_homework(result_1)
    teacher.check_homework(result_2)
    Teacher.reset_results(homework)
    assert len(teacher.homework_done) == 1
    assert Teacher.homework_done[homework_2] == {result_2}


def test_if_eqaul_results_is_not_repeated_in_homework_done(teacher, homework, student):
    Teacher.reset_results()
    result = student.do_homework(homework, "solution")
    teacher_2 = Teacher("name", "last")
    teacher.check_homework(result)
    teacher_2.check_homework(result)
    assert teacher.homework_done == teacher_2.homework_done
    assert len(Teacher.homework_done) == 1


def test_reset_results_without_args_clear_homework_done(teacher, homework, student):
    Teacher.reset_results()
    result_1 = student.do_homework(homework, "solution")
    homework_2 = teacher.create_homework("another", 3)
    result_2 = student.do_homework(homework_2, "solution")
    teacher.check_homework(result_1)
    teacher.check_homework(result_2)
    assert len(teacher.homework_done) == 2
    Teacher.reset_results()
    assert len(teacher.homework_done) == 0
