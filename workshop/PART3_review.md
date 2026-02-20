# Part 3: AI-Powered Code Review
**Time: 5-10 minutes**

---

## 🎯 Your Goal

Use Copilot to find and fix a security vulnerability in the `Student` model.

---

## 🔒 Activity: Security Review (5-10 min)

### Step 1: Find the vulnerability

Open `src/models/student.py` and select the entire file. Press `Cmd+I` / `Ctrl+I` and ask:

> Review this code for security vulnerabilities, do not fix them but explain where they are

### Step 2: Spot the issues

Copilot should flag these problems:
- **Password in `to_dict()`** — exposes credentials in API responses
- **Plaintext password storage** — should be hashed

### Step 3: Fix the critical issue

Select the `to_dict()` method, press `Cmd+I`, and ask:

> Remove password from this method to prevent credential exposure

Apply the fix.

### Step 4: Verify

Add a quick test at the bottom of `student.py`:

```python
if __name__ == "__main__":
    s = Student("S1", "test@test.com", "secret123", "Test", "User")
    print("password" not in s.to_dict())  # Should print: True
```

Click **▶ Run**. If it prints `True`, you're done.

---

## 🎓 Quick Reflection

- Did Copilot catch both issues?
- Did it suggest any false positives?
- Would you trust AI alone for security review?

---

## ✅ Checkpoint

- [ ] Fixed password exposure in `to_dict()`
- [ ] Verified the fix works
- [ ] Understand AI's limitations in security review

---

## 🎉 Workshop Complete!

### What You Accomplished

1. Generated requirements with different prompting techniques
2. Built a `Feedback` model with Copilot assistance
3. Created tests using AI suggestions
4. Found and fixed a security vulnerability

### Key Takeaways

| AI is good at | AI needs verification |
|--------------|----------------------|
| Code generation | Security issues |
| Test scaffolding | Business logic |
| Spotting obvious bugs | Edge cases |

**Golden rule:** Always test and review AI-generated code before shipping.

---

**Thank you for participating!**
