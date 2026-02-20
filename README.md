# AI-Assisted SDLC Workshop
## A Short & Sweet Guide to Coding with GitHub Copilot

---

## What This Is

A hands-on workshop where you'll build a **Course Feedback System** using GitHub Copilot. You'll experience the full development cycle — from requirements to code review — with AI assistance.

---

## Prerequisites

- **VS Code** installed ([download](https://code.visualstudio.com/))
- **GitHub Copilot** extension installed and signed in
- **Python 3.8+** installed

---

## Getting Started

### 1. Download the Workshop

git clone 

### 2. Open in VS Code

```bash
cd sdlc-ai-workshop
code .
```

Or: Open VS Code → File → Open Folder → select `sdlc-ai-workshop`

### 3. Install Dependencies

Open the terminal in VS Code (`Ctrl+`` ` or View → Terminal):

```bash
pip3 install pytest
```

### 4. Verify Copilot is Active

- Look for the Copilot icon in the bottom-right status bar
- It should show as "ready" (not "disabled")
- If not signed in, click it and follow the prompts

---

## Workshop Structure

| Part | Time | What You'll Do |
|------|------|----------------|
| [Part 1: Requirements](workshop/PART1_requirements.md) | 10 min | Generate user stories with Copilot |
| [Part 2: Implementation](workshop/PART2_implementation.md) | 25 min | Build & test a Feedback model |
| [Part 3: Code Review](workshop/PART3_review.md) | 5-10 min | Find & fix a security issue |

---

## How to Use Copilot

| Action | How |
|--------|-----|
| **Accept suggestion** | Press `Tab` |
| **Dismiss suggestion** | Press `Esc` |
| **See alternatives** | Press `Alt+]` or `Alt+[` |
| **Inline chat** | Select code → `Cmd+I` (Mac) / `Ctrl+I` (Windows) |
| **Run Python file** | Click ▶ button (top-right) |

---

## Project Structure

```
sdlc-ai-workshop/
├── src/models/       ← You'll add feedback.py here
├── tests/            ← You'll add test_feedback.py here
├── workshop/         ← Instructions for each part
└── README.md         ← You are here
```

---

## Tips

- **Let Copilot lead** — start typing and see what it suggests
- **Use inline chat** (`Cmd+I`) for specific requests
- **Always test** — AI makes mistakes, catch them early
- **Iterate** — if the first suggestion isn't right, ask again

---

## Start Here

👉 [Part 1: Requirements](workshop/PART1_requirements.md)
