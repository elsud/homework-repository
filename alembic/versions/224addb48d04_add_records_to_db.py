"""Add records to db

Revision ID: 224addb48d04
Revises: 8927199b2e4e
Create Date: 2021-06-02 14:03:28.052255

"""
from homework12.models import Student, Teacher, session

# revision identifiers, used by Alembic.
revision = "224addb48d04"
down_revision = "8927199b2e4e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    student = Student("Ivan", "Petrov")
    student2 = Student("Anna", "Ryzova")
    teacher = Teacher("Alex", "Bykov")
    teacher2 = Teacher("Olga", "Dorskaya")

    session.add(student)
    session.add(student2)
    session.add(teacher)
    session.add(teacher2)

    homework = teacher.create_homework("Math task", 5)
    student.do_homework(homework, "solution for math")
    student2.do_homework(homework, "another solution for math")

    homework2 = teacher2.create_homework("Logical task", 3)
    student2.do_homework(homework2, "blablabla")

    session.commit()
    session.close()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    session.query(Student).delete()
    session.query(Teacher).delete()
    session.commit()
    session.close()
    # ### end Alembic commands ###