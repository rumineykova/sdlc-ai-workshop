# Python Coding Standards
## Brunel University CS Department

---

## 1. Code Style

All Python code must follow:
- **PEP 8** style guide
- **Type hints** for all function parameters and returns
- **Docstrings** for all classes and public methods
- **Maximum line length:** 88 characters

---

## 2. Security Requirements

### Password Handling

❌ **NEVER store passwords in plaintext**

```python
# WRONG
class User:
    def __init__(self, password: str):
        self.password = password  # Plaintext!
```

✅ **ALWAYS hash passwords**

```python
# CORRECT
from passlib.hash import pbkdf2_sha256

class User:
    def __init__(self, password: str):
        self.password_hash = pbkdf2_sha256.hash(password)
```

### Data Exposure

❌ **NEVER include sensitive data in API responses**

```python
# WRONG
def to_dict(self):
    return {
        "user_id": self.user_id,
        "password": self.password  # Exposed!
    }
```

✅ **EXCLUDE sensitive fields**

```python
# CORRECT
def to_dict(self):
    return {
        "user_id": self.user_id,
        "email": self.email
        # password NOT included
    }
```

### Student Privacy

For student data systems:
- Feedback must be **anonymous** (no student_id in feedback records)
- Grades are **confidential** (only visible to student and instructor)
- Contact information requires **consent** to share

---

## 3. Required Practices

### Input Validation

ALL user inputs must be validated:

```python
def create_feedback(rating: int, comment: str):
    if not 1 <= rating <= 5:
        raise ValueError("Rating must be between 1 and 5")
    
    if comment and len(comment) > 1000:
        raise ValueError("Comment too long")
```

### Error Handling

Use specific exceptions with clear messages:

```python
# ✅ Good
if age < 0:
    raise ValueError("Age cannot be negative")

# ❌ Bad
if age < 0:
    raise Exception("Invalid")
```

---

## 4. Prohibited Practices

**FORBIDDEN:**
- Using `eval()` on user input
- Storing passwords in plaintext
- SQL injection (use parameterized queries)
- Hardcoded credentials or secrets

---

**Last Updated:** January 2026
