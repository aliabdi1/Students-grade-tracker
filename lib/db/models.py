from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grades = relationship('Grade', back_populates='student', cascade="all, delete")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    score = Column(Float, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    student = relationship('Student', back_populates='grades')
    
    def __repr__(self):
        return f"<Grade(id={self.id}, subject='{self.subject}', score={self.score})>"
    
    