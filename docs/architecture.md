# AI Study Assistant — System Architecture

## 1. Project Overview

The AI Study Assistant is a web-based learning platform designed to help students understand, organize, revise, and test their knowledge using Artificial Intelligence.

The system provides:

- AI-powered study chat
- Subject-based workspaces
- PDF document upload
- AI-generated summaries
- Flashcard generation
- Quiz generation
- Chat history
- Student authentication
- Administrative management

---

## 2. Architecture Pattern

The application follows a layered client-server architecture.

```text
┌───────────────────────────────┐
│          STUDENT              │
│     Web Browser / Tablet      │
└───────────────┬───────────────┘
                │
                │ HTTP / HTTPS
                ▼
┌───────────────────────────────┐
│          FRONTEND             │
│        React + Vite           │
│                               │
│  • Login                      │
│  • Dashboard                  │
│  • AI Chat                    │
│  • Subjects                   │
│  • PDFs                       │
│  • Summaries                  │
│  • Flashcards                 │
│  • Quizzes                    │
│  • Admin Interface            │
└───────────────┬───────────────┘
                │
                │ REST API
                ▼
┌───────────────────────────────┐
│           BACKEND             │
│            FastAPI            │
│                               │
│  • Authentication             │
│  • User Management            │
│  • Chat Management            │
│  • Subject Management         │
│  • PDF Processing             │
│  • Summary Generation         │
│  • Flashcard Generation       │
│  • Quiz Generation            │
│  • Admin Operations           │
└───────────┬───────────┬───────┘
            │           │
            ▼           ▼
┌────────────────┐  ┌────────────────┐
│   PostgreSQL   │  │   AI Service   │
│    Database    │  │      LLM       │
└────────────────┘  └────────────────┘