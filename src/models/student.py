"""
Student model for the course management system.
"""
from typing import Optional, List
from datetime import datetime


class Student:
    """Represents a student in the system."""
    
    def __init__(
        self,
        student_id: str,
        email: str,
        password: str,  # SECURITY ISSUE: Storing plain text password
        first_name: str,
        last_name: str,
        enrollment_date: Optional[datetime] = None
    ):
        self.student_id = student_id
        self.email = email
        self.password = password  # SECURITY ISSUE: No hashing
        self.first_name = first_name
        self.last_name = last_name
        self.enrollment_date = enrollment_date or datetime.now()
        self.enrolled_courses: List[str] = []
    
    def enroll_in_course(self, course_id: str) -> bool:
        """Enroll student in a course."""
        self.enrolled_courses.append(course_id)
        return True
    
    def get_full_name(self) -> str:
        """Return student's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def to_dict(self) -> dict:
        """Convert student to dictionary."""
        return {
            "student_id": self.student_id,
            "email": self.email,
            "password": self.password,  # SECURITY ISSUE: Exposing password
            "first_name": self.first_name,
            "last_name": self.last_name,
            "enrollment_date": self.enrollment_date.isoformat(),
            "enrolled_courses": self.enrolled_courses
        }
