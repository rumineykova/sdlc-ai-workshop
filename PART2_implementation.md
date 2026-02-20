# Part 2: Implementation with GitHub Copilot
**Time: 15 minutes**

---

## 🎯 Your Goal

Build a `Feedback` model and tests using Copilot autocomplete + your user stories from Part 1.

---

## 💻 Activity 1: Build the Model (7 min)

### Step 1: Let Copilot autocomplete

1. Create `src/models/feedback.py`
2. Start typing — Copilot will suggest the rest:

```python
"""
Feedback model for course feedback system.
Attributes: feedback_id, course_id, rating (1-5), comment, submitted_at, is_anonymous
"""
from datetime import datetime
from typing import Optional

class Feedback:
    """Represents student feedback for a course."""

    def __init__(self, feedback_id: str, course_id: str, rating: int,
                 # Press Tab to accept Copilot's suggestions
```

### Step 2: Verify your acceptance criteria

Open your `specification/user_stories_v2.md` from Part 1. Pick one criterion, e.g.:

> **Given** a rating outside 1-5, **When** submitted, **Then** reject with error

Select your `Feedback` class, press `Cmd+I` and ask:
> Does this class satisfy this criterion? If not, add the validation.

### Step 3: Quick test

Add at the bottom, click **▶ Run**:

```python
if __name__ == "__main__":
    f = Feedback("F1", "CS101", 4, "Great", datetime.now())
    print(f.to_dict())
```

---

## 🧪 Activity 2: Generate Tests (5 min)

### Step 3: Start typing, let Copilot continue

1. Create `tests/test_feedback.py`
2. Type the start, Copilot will suggest tests:

```python
import pytest
from datetime import datetime
from src.models.feedback import Feedback

class TestFeedback:
    def test_valid_feedback_creation(self):
        # Tab to accept Copilot's suggestions
```

### Step 4: Add tests for your acceptance criteria

If Copilot didn't cover your criteria from Part 1, press `Cmd+I` and ask:
> Generate a test for this acceptance criterion: [paste your criterion]

Run: `python3 -m pytest tests/test_feedback.py -v`

---

## ✅ Checkpoint

- [ ] `src/models/feedback.py` works
- [ ] `tests/test_feedback.py` passes
- [ ] Code satisfies at least one acceptance criterion from Part 1

---

**Next:** [Part 3: Code Review](PART3_review.md)
