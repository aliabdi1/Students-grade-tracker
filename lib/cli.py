from db.models import Student, Grade
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main_menu():
    print("\nWelcome to the Students Grade Tracker!")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View All Students")
    print("4. View Grades by Student")
    print("5. Delete Student")
    print("6. Exit")

def add_student(session):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    try:
        student = Student(name=name, age=int(age))
        session.add(student)
        session.commit()
        print(f"Student {name} added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def add_grade(session):
    student_id = input("Enter student ID: ")
    subject = input("Enter subject: ")
    score = input("Enter score: ")
    try:
        grade = Grade(subject=subject, score=float(score), student_id=int(student_id))
        session.add(grade)
        session.commit()
        print("Grade added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_all_students(session):
    students = session.query(Student).all()
    for student in students:
        print(student)

def view_grades_by_student(session):
    student_id = input("Enter student ID: ")
    try:
        student = session.query(Student).get(int(student_id))
        if student:
            print(f"Grades for {student.name}: ")
            for grade in student.grades:
                print(grade)
        else:
            print("Student not found.")
    except Exception as e:
        print(f"Error: {e}")

def delete_student(session):
    student_id = input("Enter student ID: ")
    try:
        student = session.query(Student).get(int(student_id))
        if student:
            session.delete(student)
            session.commit()
            print("Student deleted successfully!")
        else:
            print("Student not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    engine = create_engine('sqlite:///students.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(session)
        elif choice == '2':
            add_grade(session)
        elif choice == '3':
            view_all_students(session)
        elif choice == '4':
            view_grades_by_student(session)
        elif choice == '5':
            delete_student(session)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
