from datetime import timedelta
from unittest import mock

import pytest

from homework12.models import DeadlineError, HomeworkResult, Session, Student, Teacher


@pytest.fixture(scope="function")
def db_session():
    session = Session()
    with mock.patch("homework12.models.session", new=session):
        yield session
    session.rollback()
    session.close()


def test_init_student(db_session):
    student = Student("s", "S")
    db_session.add(student)
    student = db_session.query(Student).filter(Student.first_name == "s").first()
    assert student.last_name == "S"


def test_init_teacher(db_session):
    teacher = Teacher("t", "T")
    db_session.add(teacher)
    assert teacher.first_name == "t"
    assert teacher.last_name == "T"
    assert db_session.query(Teacher).filter(Teacher.last_name == "T").first()


def test_is_homework_created_with_all_attributes(db_session):
    teacher = Teacher("t", "T")
    db_session.add(teacher)
    homework = teacher.create_homework("HW", 7)
    assert homework.teacher == teacher
    assert homework.deadline == timedelta(7)
    assert homework.is_active()


def test_homework_after_deadline_is_not_active(db_session):
    teacher = Teacher("t", "T")
    db_session.add(teacher)
    bad_hw = teacher.create_homework("Too late", 0)
    assert not bad_hw.is_active()


def test_if_doing_not_homework_raises_typeerror(db_session):
    student = Student("s", "S")
    db_session.add(student)
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        student.do_homework("homework", "solution")


def test_homeworkresult_is_in_table(db_session):
    teacher = Teacher("t", "T")
    db_session.add(teacher)
    homework = teacher.create_homework("HW", 7)
    student = Student("s", "S")
    db_session.add(student)
    student.do_homework(homework, "long solution")
    result = homework.results[0]
    assert result.solution == "long solution"
    assert result.homework == homework
    assert result.author == student
    assert student.homework_results == homework.results


def test_doing_homework_after_deadline_raises_deadlineerror(db_session):
    student = Student("bad", "student")
    teacher = Teacher("t", "T")
    db_session.add(student)
    homework = teacher.create_homework("Too late", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(homework, "doesn't matter")


def test_homeworkresult_with_short_solution_is_not_in_table(db_session):
    student = Student("bad", "student")
    db_session.add(student)
    teacher = Teacher("t", "T")
    homework = teacher.create_homework("HW", 7)
    student.do_homework(homework, "1")
    assert not student.homework_results


def test_homeworkresult_with_the_same_solution_is_not_in_table(db_session):
    student = Student("s", "S")
    student2 = Student("bad", "student")
    db_session.add(student)
    db_session.add(student2)
    teacher = Teacher("t", "T")
    homework = teacher.create_homework("HW", 7)
    student.do_homework(homework, "long solution")
    student2.do_homework(homework, "long solution")
    assert not student2.homework_results


def test_reset_results_with_given_homework_deletes_solutions_for_that_homework(
    db_session,
):
    student = Student("s", "S")
    teacher = Teacher("t", "T")
    homework = teacher.create_homework("HW", 7)
    student.do_homework(homework, "long solution")
    student.do_homework(homework, "another solution")
    teacher.reset_results(homework)
    assert (
        not db_session.query(HomeworkResult)
        .filter(HomeworkResult.homework == homework)
        .all()
    )


def test_reset_results_without_args_clear_all_homeworkresults(db_session):
    student = Student("s", "S")
    teacher = Teacher("t", "T")
    homework = teacher.create_homework("HW", 7)
    hw = teacher.create_homework("to delete", 4)
    student.do_homework(homework, "solution to delete")
    student.do_homework(hw, "another solution")
    teacher.reset_results()
    assert not db_session.query(HomeworkResult).all()
