# Agentic AI Case Study Development Starter Kit

A starter kit for creating HBR-style MBA case studies from digital sources, guided by AI.

[![Template Version](https://img.shields.io/badge/template-v3.1.0-blue)](TEMPLATE_VERSION)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)

---

## What This Is

This repository is a **GitHub template** that gives you everything you need to develop a professional business school case study. You gather source materials (interviews, articles, financial reports), and AI guides you through the entire process — from assessing your sources to writing and verifying a four-document case study package.

### The Case Study Package

| Document | Audience | Purpose | Length |
|----------|----------|---------|--------|
| **Additional Sources** | Researchers | Raw materials, bibliography, exhibits | 3,000-5,000 words |
| **Main Case** | Students | Protagonist-centered narrative with strategic tension | 4,000-6,000 words |
| **Technical Supplement** | Students, Instructors | Industry context, frameworks, glossary | 2,500-4,000 words |
| **Teaching Note** | Instructors only | Discussion guide, board plans, timing | 2,500-4,000 words |

---

## Quick Start

### Step 1: Create Your Repository

Click the green **"Use this template"** button above, then **"Create a new repository"**. Name it something like `moderna-case-study` (you can rename this later). Set it to **Private**.

### Step 2: Get the Files onto Your Computer

Open a terminal and clone your new repository.

**Mac** — open Terminal (search "Terminal" in Spotlight):

```bash
cd ~/Desktop
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

**Windows** — open PowerShell (search "PowerShell" in Start menu):

```powershell
cd ~\Desktop
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

Replace `YOUR-USERNAME` and `YOUR-REPO-NAME` with your actual values. Use any folder you prefer — Desktop is just an example.

> **Tip**: On Mac, you can drag your project folder onto the Terminal icon to open it there. On Windows, right-click a folder in File Explorer and select "Open in Terminal."

<details>
<summary><strong>Alternative: Download ZIP (no git required)</strong></summary>

1. Go to your new repository on GitHub
2. Click the green **"Code"** button → **"Download ZIP"**
3. Unzip to any folder on your computer

Note: The ZIP option won't have git features (version history, pushing changes). You can still do all the case study work.
</details>

### Step 3: Choose Your AI Tool

Pick the option that fits your setup. **Options A and B are agentic** — they can read and edit your files directly. Option C works but requires more manual effort.

| Feature | Claude Code | VS Code + Copilot | Chat Tools |
|---------|-------------|-------------------|------------|
| Reads local files | Yes | Yes (Agent Mode) | No |
| Writes/edits files | Yes | Yes (Agent Mode) | No |
| Runs terminal commands | Yes | Yes | No |
| `/slash-commands` | Yes (16 skills) | No (use natural language) | No |
| Custom instructions | CLAUDE.md | .github/copilot-instructions.md + CLAUDE.md | N/A |
| Cost | Subscription | Free (GitHub Education) | Free tier varies |
| Best for | Full automation | Students with VS Code | Quick start, no setup |

#### Option A: Claude Code

Claude Code can read your files, run `/slash-commands`, and manage the entire workflow automatically.

1. Open your project in Claude Code
2. Say: **"Help me develop my case study"**
3. Or run: `/setup-case` to get started

#### Option B: VS Code + GitHub Copilot (Free for Students)

VS Code with **Copilot Agent Mode** can read and edit your local files, run terminal commands, and follow the custom instructions in this repo — making it a full agentic workflow.

1. Sign up for **GitHub Education** at [education.github.com](https://education.github.com) to get **Copilot Pro free** (unlimited completions, 300 premium requests/month)
2. Install [VS Code](https://code.visualstudio.com/) and the **GitHub Copilot** extension
3. Open your project folder in VS Code
4. Open the Copilot chat panel (click the Copilot icon in the sidebar) and select **Agent Mode**
5. Say: **"Help me develop my case study"**

Copilot reads `.github/copilot-instructions.md` automatically. Instead of `/slash-commands`, describe what you want in natural language (e.g., *"Evaluate my source quality"* instead of `/assess-sources`).

#### Option C: Chat Tools (ChatGPT, Claude.ai, Gemini)

Chat tools work but cannot read files on your computer directly. You must upload or paste content into the chat.

1. Open **[STARTER_PROMPT.md](STARTER_PROMPT.md)** and copy the prompt inside
2. Paste it into your chat tool
3. When the AI asks about your sources, **drag-and-drop** your source files into the chat or paste the text

> **Important**: Chat tools cannot run the `/slash-commands` or read your local files. The starter prompt is designed to guide you through the process conversationally instead.

#### Getting Tech Help

Running into issues with git, the terminal, or project setup? **Any AI tool can help you troubleshoot** — you don't need to use the same tool you're writing the case study with.

- **Paste the error message** into any AI chat (ChatGPT, Claude.ai, Gemini, Copilot) and ask for help
- **Describe what you were trying to do** and what happened instead
- Common issues: git authentication, cloning, file paths, OneDrive conflicts (see [Troubleshooting](#troubleshooting) below)

### Step 4: Configure Your Case

**Claude Code users**: Run `/setup-case` — it asks you questions and writes the config files automatically.

**VS Code + Copilot users**: Say *"Help me configure my case study"* in Copilot Agent Mode.

**Chat tool users**: The starter prompt will ask you about your company, protagonist, and topic.

**Manual setup**: Open `case-config.yaml` and replace the placeholder values.

### Step 5: Gather Sources and Write

Add research materials to `sources/` (transcripts, articles, financial reports). Then follow the AI-guided process to write your four documents.

**Save your progress** after each major step:

**Mac:**
```bash
git add -A && git commit -m "Complete Additional Sources draft" && git push
```

**Windows:**
```powershell
git add -A; git commit -m "Complete Additional Sources draft"; git push
```

Or in Claude Code, run `/git-update`.

---

## Workflow Overview

The process is **iterative**, not strictly linear. You'll cycle between sources and writing as gaps are discovered.

```
SETUP → SOURCES → ASSESS → WRITE → [gap found?] → back to SOURCES
                                  → [no gap] → VERIFY → PUBLISH
```

| Phase | What to Do | Skill Command |
|-------|-----------|---------------|
| 1. Configure | Set up case details | `/setup-case` |
| 2. Add Sources | Register source materials | `/add-sources` |
| 3. Assess | Evaluate source quality | `/assess-sources` |
| 4. Write | Create documents in order | `/write-document` |
| 5. Verify | Run quality checks | `/verify-all` |
| 6. Publish | Add disclaimers, export PDFs | `/add-disclaimers`, `/export-pdf` |

Check your progress anytime: `/check-status`

---

## What's in This Repository

| Path | Purpose |
|------|---------|
| `STARTER_PROMPT.md` | Prompt for chat tools (ChatGPT, Claude.ai, Gemini) |
| `case-config.yaml` | Central configuration (auto-written by `/setup-case`) |
| `verification-debt.yaml` | Tracks unverified AI-generated claims |
| `sources/` | Your research materials |
| `sources/Source_Registry.md` | Source catalog with quality tiers |
| `case-study/` | Where your four case documents will live |
| `exports/` | PDF exports for distribution |
| `templates/` | Detailed prompts, QA workflows, source guides |
| `.claude/skills/` | Claude Code skill definitions |
| `.github/copilot-instructions.md` | VS Code Copilot custom instructions |
| `PROJECT_CONTEXT.md` | Session continuity context |

---

## Skills Reference

These `/slash-commands` work in **Claude Code**. **VS Code + Copilot** users: ask for the same action in natural language (e.g., say *"Run all quality checks"* instead of `/verify-all`). See `.github/copilot-instructions.md` for the full equivalents table.

| Command | Purpose |
|---------|---------|
| `/setup-case` | Configure project (asks questions, writes files) |
| `/add-sources` | Register source materials with tier classification |
| `/assess-sources` | Evaluate source quality with go/no-go gate |
| `/write-document` | Guided document writing with inline verification |
| `/check-status` | Project dashboard with progress and debt tracking |
| `/verify-all` | Run all quality checks |
| `/verify-consistency` | Cross-document data point matching |
| `/verify-quotes` | Trace quotes back to source documents |
| `/verify-sources` | Check attribution completeness |
| `/verify-links` | Validate external URLs |
| `/validate-financials` | Check arithmetic and financial accuracy |
| `/assess-bias` | Analyze source perspective balance |
| `/verify-cross-document` | Structural alignment between documents |
| `/add-disclaimers` | Add AI methodology disclaimers |
| `/export-pdf` | Prepare documents for PDF export |
| `/git-update` | Stage, commit, and push changes |

---

## For Non-Business Cases

Writing about public policy, political leadership, or international development? See `templates/HKS_PUBLIC_POLICY_GUIDANCE.md` for adapted frameworks. Run `/setup-case` and select "public policy" when asked about case type.

---

## Troubleshooting

### "The AI can't see my files"

Chat tools (ChatGPT, Claude.ai, Gemini) **cannot** read files on your computer. You must:
- Drag-and-drop files into the chat window, OR
- Copy-paste the file contents

Claude Code and VS Code + Copilot (Agent Mode) can read your local files directly — no uploading needed.

### GitHub credentials / authentication issues

If `git push` asks for credentials:
1. Install [GitHub CLI](https://cli.github.com/): `gh auth login`
2. Or use a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

### OneDrive / iCloud path issues

If your project is in a synced folder (OneDrive, iCloud, Dropbox), git may behave unexpectedly. Move your project to a non-synced location:

**Mac:**
```bash
mv ~/Desktop/my-case-study ~/Documents/my-case-study
```

**Windows:**
```powershell
Move-Item ~\Desktop\my-case-study ~\Documents\my-case-study
```

### "I don't know which step to do next"

In Claude Code, run `/check-status` for a full project dashboard.

### "I made a mistake and want to undo"

If you committed recently, git has your history:
```bash
git log --oneline -5
```
Ask Claude Code for help reverting to a previous state.

---

## Acknowledgments

This methodology was developed through the creation of MBA case studies for ITEC-617 at American University's Kogod School of Business, Spring 2026.

---

*Template Version: 3.1.0*
