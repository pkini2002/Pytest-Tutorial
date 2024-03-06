import pytest
from source.school import Classroom, Student, Teacher, TooManyStudents


@pytest.fixture
def classroom():
    teacher = Teacher("Professor Snape")
    students = [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]
    course_title = "Potions"
    return Classroom(teacher, students, course_title)


def test_add_student(classroom):
    # Test adding a student to the classroom
    new_student = Student("Neville Longbottom")
    classroom.add_student(new_student)
    assert len(classroom.students) == 4


def test_add_too_many_students(classroom):
    # Test adding too many students to the classroom
    with pytest.raises(TooManyStudents):
        for _ in range(12):
            classroom.add_student(Student("Random Student"))


def test_remove_student(classroom):
    # Test removing a student from the classroom
    classroom.remove_student("Hermione Granger")
    assert len(classroom.students) == 2


def test_change_teacher(classroom):
    # Test changing the teacher of the classroom
    new_teacher = Teacher("Professor McGonagall")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Professor McGonagall"
