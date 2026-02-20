"""
Tests for Student model.
"""
import pytest
from datetime import datetime
from src.models.student import Student


class TestStudentModel:
    """Test suite for Student model."""
    
    def test_student_creation(self):
        """Test basic student creation."""
        student = Student(
            student_id="S001",
            email="alice@brunel.ac.uk",
            password="password123",
            first_name="Alice",
            last_name="Smith"
        )
        
        assert student.student_id == "S001"
        assert student.email == "alice@brunel.ac.uk"
        assert student.first_name == "Alice"
        assert student.last_name == "Smith"
    
    def test_get_full_name(self):
        """Test full name generation."""
        student = Student(
            student_id="S001",
            email="alice@brunel.ac.uk",
            password="password123",
            first_name="Alice",
            last_name="Smith"
        )
        
        assert student.get_full_name() == "Alice Smith"
    
    def test_enroll_in_course(self):
        """Test course enrollment."""
        student = Student(
            student_id="S001",
            email="alice@brunel.ac.uk",
            password="password123",
            first_name="Alice",
            last_name="Smith"
        )
        
        result = student.enroll_in_course("CS101")
        assert result is True
        assert "CS101" in student.enrolled_courses
