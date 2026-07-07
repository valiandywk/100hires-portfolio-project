# 100Hires Portfolio Project

This repository contains the completion of the assignments for the 100Hires application process.

---

## Step 1: Initial Setup

### Tools Installed
- **Cursor IDE**: Downloaded and installed the AI-powered code editor.
- **Claude Code & Codex Extensions**: Installed via Cursor's marketplace and authenticated.
- **Git & GitHub**: Utilized for version control and remote hosting.

### Issues Encountered & Solutions
* **Issue:** Prompted to generate a GitHub Personal Access Token (PAT) during the initial `git clone`.
* **Solution:** Generated a classic token via GitHub Developer Settings with repo scopes to authenticate Cursor IDE.
* **Issue:** Local Git repository got overwritten and detached by a system update, causing dependency conflicts.
* **Solution:** Re-initialized Git locally, utilized Python Virtual Environments (`venv`) to isolate dependencies, and successfully merged unrelated histories to push the data securely.

---

## Step 2: Expert Research (AI-Powered SEO Content Production)

For the research phase, I selected **AI-Powered SEO Content Production** as the core topic. I specifically avoided generic marketers and targeted technical SEOs, SaaS founders, and semantic search specialists (e.g., Kevin Indig, Aleyda Solis, Mike King) who are actively building LLM workflows and analyzing how Generative Engine Optimization (GEO) impacts search.

### Methodology & AI Tool Usage
- **Sources Compiled:** 10 high-signal experts curated in `/research/sources.md` based on practical execution rather than just theory.
- **YouTube Transcripts:** Prompted Claude within Cursor to author a Python script (`fetch_transcripts.py`) utilizing the `youtube-transcript-api`. Implemented graceful error handling and API fallback mechanisms to bypass local environment restrictions.
- **LinkedIn Posts:** Compiled raw insights from the chosen experts and formatted them into clean, structured markdown files within the `/research/linkedin-posts/` directory.
