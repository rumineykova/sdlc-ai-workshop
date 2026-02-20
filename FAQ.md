# Workshop FAQ

---

## Setup Issues

**Q: "pip install -r requirements.txt" fails**

A: Try:
```bash
pip install --upgrade pip
pip install pytest black flake8
```

**Q: Tests won't run**

A: Make sure you're in the repository root and venv is activated:
```bash
source venv/bin/activate
python -m pytest tests/ -v
```

---

## AI Tool Issues

**Q: I hit rate limits on ChatGPT/Claude**

A: 
- Wait 30 seconds between requests
- Use shorter code examples in prompts
- Try a different AI tool temporarily
- Work with a partner and share access

**Q: AI generated code that doesn't work**

A: This is normal! 
1. Read the error message
2. Ask AI: "Fix this error: [paste error]"
3. Check for hallucinated imports/methods
4. Simplify your prompt and try again

---

## Workshop Questions

**Q: I'm running out of time**

A: Priorities:
1. Complete Part 1 (requirements) - this teaches prompting
2. Get basic `Feedback` model working in Part 2
3. Skip detailed testing if needed
4. Do security review in Part 3

**Q: My code works but doesn't match the style**

A: That's okay! The goal is learning, not perfect code.

**Q: Should I copy-paste all AI outputs?**

A: No! 
- Read the code first
- Understand what it does
- Test it
- Fix issues
- Then commit

---

## Technical Questions

**Q: Do I need to implement password hashing?**

A: No - just remove password from `to_dict()` for now. Full hashing is a bonus.

**Q: How do I ensure anonymity in Feedback?**

A: Don't store `student_id` in the Feedback class. Only store `course_id` and `rating`.

**Q: What if my tests fail?**

A:
1. Read the error carefully
2. Check if your code has the methods tests expect
3. Ask AI to fix specific test
4. Simplify the test if needed

---

## Best Practices

**Q: How do I write better prompts?**

A:
1. Be specific about requirements
2. Provide examples (few-shot)
3. Specify format you want
4. Add constraints
5. Iterate!

**Q: Can I use AI for everything?**

A: AI is a tool, not a replacement for thinking:
- ✅ Use AI for: code generation, test generation, finding patterns
- ⚠️ Verify: security issues, edge cases, business logic
- ❌ Don't trust: critical security code without testing

---

## After the Workshop

**Q: Can I continue working on this?**

A: Yes! Try:
- Add `FeedbackService` class
- Implement aggregate rating calculation
- Build a simple API
- Create a frontend

**Q: Where can I learn more?**

A: Resources:
- Anthropic Prompt Engineering Guide
- OpenAI Best Practices
- Course materials on AI tools
- Peer discussions

---

**Still stuck?** Ask an instructor or post in the discussion forum!
