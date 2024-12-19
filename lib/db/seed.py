from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Grade

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding sample data
student1 = Student(name='John Doe', age=16)
student2 = Student(name='Jane Smith', age=15)

grade1 = Grade(subject='Math', score=95.0, student=student1)
grade2 = Grade(subject='English', score=88.0, student=student1)
grade3 = Grade(subject='Math', score=92.0, student=student2)
grade4 = Grade(subject='Science', score=89.0, student=student2)

session.add_all([student1, student2, grade1, grade2, grade3, grade4])
session.commit()
session.close()
