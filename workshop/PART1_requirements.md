# Part 1: Requirements Engineering with AI
**Time: 5 minutes**

---

## 🎯 Goal

Generate user stories for the **Course Feedback Submission** feature and see how prompts improve outputs.

---

## 🛠️ Setup

Open VS Code and the Copilot Chat panel (`Ctrl+Shift+I` / `Cmd+Shift+I`)

---

## Step 1: Basic Prompt

Paste into Copilot Chat:

```
Generate user stories for a course feedback feature where students rate courses 1-5 stars with optional comments. Use the /src folder as context. Save to specification/user_stories_v1.md
```

---

## Step 2: Add Context and Constraints

Paste into Copilot Chat:

```
Read specification/user_stories_v1.md and improve it with these requirements:
- Use "As a... I want... so that..." format
- Include acceptance criteria (Given/When/Then)
- Include edge cases
- Feedback must be anonymous
- Students can only rate courses they're enrolled in
- One submission per student per course

Save to specification/user_stories_v2.md
```

---

## What to Notice

Compare v1 and v2:
- v1 is generic, may lack structure
- v2 follows your format, includes edge cases, matches requirements

**Takeaway:** More specific prompts = better outputs.

---

## ✅ Checkpoint

- [ ] `specification/user_stories_v1.md` exists
- [ ] `specification/user_stories_v2.md` exists with structured user stories

---

**Next:** [Part 2: Implementation](PART2_implementation.md)
