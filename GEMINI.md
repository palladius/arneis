# ♊ Arneis: Project Rules

## 🏛️ Philosophy
This is a "Harness" project. We focus on the plumbing around the LLM, not just the prompts.
Based on Fareed Khan's "Claude Code from Scratch".

## 🛠️ Tech Stack
- **Engine:** Google Gemini (Flash 2.5+ preferred for speed, Pro for reasoning).
- **Harness:** Python + UV.
- **Interface:** CLI + Telegram (via OpenClaw).

## 📋 Policies
- **Gemini First:** Every LLM call must prioritize Gemini models.
- **Self-Documenting:** The codebase should be its own wiki.
- **Safety:** Always backup before complex file operations.
