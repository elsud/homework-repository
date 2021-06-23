"""Creating dabase main.db using SQLAlchemy and creating tables
homework, homework_results, students, teachers in it.
Also start session which should be closed.
"""
import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Interval,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///homework12/main.db", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Homework(Base):
    """Class with text of homework and deadline.
    An instance of that class is created by teacher.
    It has references to teacher who create it and homework_result.

    :param teacher: instance of Teacher who created homework
    :type teacher: Teacher
    :param text: text of homework task
    :type text: str
    :param deadline: deadline for homework in days, it will be
    converted to timedelta
    :type deadline: int
    """

    __tablename__ = "homeworks"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    deadline = Column(Interval)
    created = Column(DateTime)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="homeworks")
    results = relationship("HomeworkResult", back_populates="homework")

    def __init__(self, teacher: "Teacher", text: str, deadline: int):
        self.teacher = teacher
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def __repr__(self) -> str:
        """String representation for Homework.
        :return: the text and name of the teacher
        :rtype: str
        """
        return f"Homework '{self.text}' from {self.teacher}"

    def is_active(self) -> bool:
        """Checking if homework can be done or it's too late.
        :return: can homework be done or not
        :rtype: bool
        """
        return datetime.datetime.now() < self.deadline + self.created


class HomeworkResult(Base):
    """Class with solution of homework. It is created by teacher after
    he checks solution of student.

    :param student: instance of Student whose solution it is
    :type student: Student
    :param homework: instance of Homework to which there's solution
    :type homework: Homework
    :param solution: solution of homework
    :type solution: str
    """

    __tablename__ = "homeworkresults"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("students.id"))
    author = relationship("Student", back_populates="homework_results")
    homework_id = Column(Integer, ForeignKey("homeworks.id"))
    homework = relationship("Homework", back_populates="results")
    solution = Column(String)
    created = Column(DateTime)

    def __init__(self, student: "Student", homework: "Homework", solution: str):
        self.author = student
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()

    def __repr__(self) -> str:
        """String representation for HomeworkResult.
        :return: text of the homework, name of the student
        and text of the solution
        :rtype: str
        """
        return f"Solution for {self.homework.text}: {self.solution}"


class Student(Base):
    """Class to represent student. Has first_name and last_name.
    Student can do homework

    :param first_name: first name of the student
    :type first_name: str
    :param last_name: last name of the student
    :type last_name: str
    """

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    homework_results = relationship("HomeworkResult", back_populates="author")

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """String representation of the Student instance.
        :return: first name and last name
        :rtype: str
        """
        return f"{self.first_name} {self.last_name}"

    def do_homework(self, homework: "Homework", solution: str) -> None:
        """Doing homework if it's not deadline and giving it
        to the teacher to check it.
        :param homework: an instance of Homework to do
        :type homework: Homework
        :param solution: solution for homework
        :type solution: str
        """
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        if not homework.is_active():
            raise DeadlineError("You are late")
        homework.teacher.check_homework(self, homework, solution)


class Teacher(Base):
    """Class to represent teacher. Has first_name and last_name.
    Teacher can create homework and check solutions.

    :param first_name: first name of the teacher
    :type first_name: str
    :param last_name: last name of the teacher
    :type last_name: str
    """

    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    homeworks = relationship("Homework", back_populates="teacher")

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """String representation of the Teacher instance.
        :return: first name and last name
        :rtype: str
        """
        return f"{self.first_name} {self.last_name}"

    def create_homework(self, text: str, deadline: int) -> Homework:
        """Creating Homework object and adding it to the table homework
        without commiting.
        :param text: text of the homework
        type text: str
        :param deadline: count of the days during which homework can be done
        :type deadline: int
        :return: an instance of Homework
        :rtype: Homework
        """
        new_hw = Homework(self, text, deadline)
        session.add(new_hw)
        return new_hw

    @staticmethod
    def check_homework(student: "Student", homework: "Homework", solution: str) -> bool:
        """Checking if the length of solution is more than 5 symbols
        and adding HomeworkResult to the table without commiting if it's True.
        :param student: the student who is an author of the solution to check
        :type student: Student
        :param homework: the homework to check solution to it
        :type homework: Homework
        :param solution: the solution of the homework to check
        :type solution: str
        :return: boolean if this is a new solution and if its length
        is more than 5 symbols
        :rtype: bool
        """
        if len(solution) > 5:
            is_exist = (
                session.query(HomeworkResult)
                .filter(
                    HomeworkResult.homework == homework,
                    HomeworkResult.solution == solution,
                )
                .all()
            )
            if not is_exist:
                session.add(HomeworkResult(student, homework, solution))
                return True
        return False

    @classmethod
    def reset_results(cls, homework: "Homework" = None) -> None:
        """Deleting solutions for given homework from table or clearing
        all homework_results table without commiting.
        :param homework: homework solutions for which should delete
        :type homework: Homework or None
        """
        if homework:
            session.query(HomeworkResult).filter(
                HomeworkResult.homework == homework
            ).delete()
        else:
            session.query(HomeworkResult).delete()


class DeadlineError(Exception):
    """Exception which raises when student try to do homework after deadline"""


session = Session()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session.close()
