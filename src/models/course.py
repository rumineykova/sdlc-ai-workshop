"""
Course model for the course management system.
"""
from typing import List
from datetime import datetime


class Course:
    """Represents a course in the system."""
    
    def __init__(
        self,
        course_id: str,
        title: str,
        description: str,
        instructor: str,
        max_students: int = 50
    ):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor = instructor
        self.max_students = max_students
        self.enrolled_students: List[str] = []
        self.created_at = datetime.now()
    
    def is_full(self) -> bool:
        """Check if course has reached maximum enrollment."""
        return len(self.enrolled_students) >= self.max_students
    
    def add_student(self, student_id: str) -> bool:
        """Add a student to the course."""
        if self.is_full():
            return False
        if student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)
        return True
    
    def to_dict(self) -> dict:
        """Convert course to dictionary."""
        return {
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor,
            "max_students": self.max_students,
            "enrolled_students": self.enrolled_students,
            "enrollment_count": len(self.enrolled_students),
            "created_at": self.created_at.isoformat()
        }
