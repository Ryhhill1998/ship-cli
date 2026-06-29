# Ryan Henzell-Hill — Context File

## Current Role
Data Platform Engineer at BMLL, London (Apr 2026 – Present). Part of a platform team that manages how all applications run on AWS, handles workload orchestration via Celery queues, and builds CLIs and infrastructure tooling for other engineering teams to use.

---

## Background & Capabilities

**Experience:**
- Software Engineer at Kayenta (May 2025 – Apr 2026) — built a greenfield event-driven data quality monitoring platform (AWS EventBridge, Lambda, S3, DynamoDB); optimised high-volume data ingest pipelines
- Software Engineer at Lloyds Banking Group (Sep 2023 – May 2025) — designed and led a secure full-stack internal file delivery platform (React/TypeScript, FastAPI, Azure SSO, Active Directory, HashiCorp Vault); built a CLI for high-volume confidential file retrieval (1M+ downloads/month); won a Microsoft-sponsored hackathon building a cloud-native accessibility app using Azure OpenAI

**Stack:** React/TypeScript, Python (FastAPI, PydanticAI), AWS (Lambda, EventBridge, S3, DynamoDB, ECR, Step Functions), Terraform, GitHub Actions, HashiCorp Vault, Azure SSO/AD

**LLM experience:** Built and hosted a Spotify web app with Gemini via PydanticAI/Vertex AI — analysed listening history, performed emotion analysis on track lyrics, produced structured emotional profiles. Real auth, hosted on AWS. Taken down but the experience is real.

**Current learning:** Rust (Rust Book + Rustlings daily). Plan: complete book → Rustlings → Building an OS in Rust. Goal is systems-level thinking, not a specific end product.

---

## Career Goals

**Direction:** Become the engineer who turns complex, sensitive operational systems into safe, fast, and durable software — at companies where that work matters (AI safety, research, high-integrity infrastructure).

**Target roles in ~3 years:**
- Internal tooling / DevEx engineer at an AI lab
- Trust & Safety / integrity engineer
- AI platform / MLOps engineer (infrastructure layer, not research)

**Key things to build toward:**
- Agentic LLM integrations (orchestration, tool use, error recovery) — not just API wrappers
- Human-in-the-loop review systems (LLM triages, human reviews/corrects)
- Evaluation pipelines for LLM output quality
- Continued operations shadowing to find and fix high-risk manual processes

**Learning cadence outside work:**
- Rust: 1 hour/day, depth over breadth, no splitting attention
- Anthropic research papers: 1 per week, scheduled

---

## Current Work Project: AI Developer Tooling

### Problem
BMLL has exceeded its Claude budget multiple times. Engineers (including Ryan) are using Claude inefficiently — primarily through redundant context loading, asking Claude to re-scan the same codebases repeatedly rather than maintaining structured representations it can reference cheaply.

Additionally, the current workflow for picking up a ticket and getting Claude to start work involves many repetitive manual steps. Ryan has already built a basic CLI to automate git branch creation from ticket details. This project is the next iteration.

### Core Insight
Claude's effectiveness is bottlenecked by context quality, not capability. A structured context.md file per repo — describing what the system does, key architectural decisions, directory layout, and non-obvious developer knowledge — allows Claude to start work immediately without expensive cold-start exploration of the codebase.

### Vision
- Auto-updating context.md files per repo, triggered on merge to master via GitHub Actions
- Jira API integration to pull ticket details and generate structured Claude briefings
- Engineers shift to a "senior orchestration" role — treating Claude as a junior developer, writing descriptive briefs rather than code directly
- Claude Code used daily as the execution layer; engineers focus on systems thinking and problem decomposition

### MVP (to demonstrate before boss returns Wednesday)
**Build one thing end-to-end:**

> GitHub Actions workflow triggers on merge to master → calls Claude API → generates/updates context.md for the repo → commits it back automatically

That's the complete MVP. Nothing else in week 1.

**Do not build yet:** Jira integration, automated PR raising, multi-repo orchestration.

### Token Cost Trial (to quantify impact)
Run the same real task twice on the same repo:

| | Without context.md | With context.md |
|---|---|---|
| Prompt | "Here is the repo. Figure out what you need and do X." | "Here is a context file describing this repo. Using that, do X." |
| Session | Fresh terminal, fresh Claude Code session | Fresh terminal, fresh Claude Code session |
| Branch | Branch A | Branch B (so Claude doesn't see completed work) |

**Log:** input tokens and output tokens from each run (Claude Code prints a usage summary at end of session; API returns `usage.input_tokens` / `usage.output_tokens` in every response).

**Fresh terminal** = clean session cache (cache is server-side but tied to session).
**Separate branches** = Claude Code instance 2 doesn't see the task already done. These solve different problems — both needed.

### Measuring Business Impact
- Token delta per task × tasks per engineer per week = projected monthly saving
- Time from "I have a ticket" to "Claude has produced something reviewable" — stopwatch comparison across 2–3 real tasks
- Budget baseline: ask IT today — "I'm putting together a proposal to help engineers use Claude more efficiently and reduce spend. Do we have visibility on current monthly Claude cost? Even a rough figure would help."

### Ownership
This sits naturally in the platform team's remit — extending the existing mandate of building tooling that helps other engineers go faster. Frame to boss as: "AI tooling for engineers is an emerging cross-team need, it belongs in our team, here's the PoC." Have the demo ready before the conversation.
