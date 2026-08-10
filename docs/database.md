# AI Study Assistant — Database Design

## 1. Database

Database Management System:

- PostgreSQL

The database uses a relational design with foreign-key relationships between users, subjects, conversations, study materials, and quizzes.

---

## 2. Tables

### users

Stores student and administrator accounts.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| name | VARCHAR(100) | NOT NULL |
| email | VARCHAR(255) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(255) | NOT NULL |
| role | VARCHAR(20) | NOT NULL |
| is_active | BOOLEAN | NOT NULL |
| created_at | TIMESTAMP | NOT NULL |
| updated_at | TIMESTAMP | NOT NULL |

---

### subjects

Stores subject workspaces.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| user_id | UUID | Foreign Key → users.id |
| name | VARCHAR(150) | NOT NULL |
| description | TEXT | NULL |
| created_at | TIMESTAMP | NOT NULL |
| updated_at | TIMESTAMP | NOT NULL |

Relationship:

users 1 → N subjects

---

### conversations

Stores AI chat conversations.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| user_id | UUID | Foreign Key → users.id |
| subject_id | UUID | Foreign Key → subjects.id, NULL |
| title | VARCHAR(200) | NOT NULL |
| created_at | TIMESTAMP | NOT NULL |
| updated_at | TIMESTAMP | NOT NULL |

---

### messages

Stores individual chat messages.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| conversation_id | UUID | Foreign Key → conversations.id |
| role | VARCHAR(20) | NOT NULL |
| content | TEXT | NOT NULL |
| created_at | TIMESTAMP | NOT NULL |

Allowed roles:

- user
- assistant
- system

---

### documents

Stores uploaded PDF/document metadata.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| user_id | UUID | Foreign Key → users.id |
| subject_id | UUID | Foreign Key → subjects.id |
| file_name | VARCHAR(255) | NOT NULL |
| file_path | TEXT | NOT NULL |
| file_size | BIGINT | NOT NULL |
| mime_type | VARCHAR(100) | NOT NULL |
| extracted_text | TEXT | NULL |
| created_at | TIMESTAMP | NOT NULL |

Large files should not normally be stored directly in PostgreSQL.

---

### summaries

Stores AI-generated summaries.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| document_id | UUID | Foreign Key → documents.id |
| user_id | UUID | Foreign Key → users.id |
| title | VARCHAR(200) | NOT NULL |
| content | TEXT | NOT NULL |
| created_at | TIMESTAMP | NOT NULL |

---

### flashcards

Stores AI-generated flashcards.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| user_id | UUID | Foreign Key → users.id |
| subject_id | UUID | Foreign Key → subjects.id |
| question | TEXT | NOT NULL |
| answer | TEXT | NOT NULL |
| source_document_id | UUID | Foreign Key → documents.id, NULL |
| created_at | TIMESTAMP | NOT NULL |

---

### quizzes

Stores generated quizzes.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| user_id | UUID | Foreign Key → users.id |
| subject_id | UUID | Foreign Key → subjects.id |
| title | VARCHAR(200) | NOT NULL |
| description | TEXT | NULL |
| created_at | TIMESTAMP | NOT NULL |

---

### quiz_questions

Stores questions belonging to quizzes.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| quiz_id | UUID | Foreign Key → quizzes.id |
| question_text | TEXT | NOT NULL |
| option_a | TEXT | NOT NULL |
| option_b | TEXT | NOT NULL |
| option_c | TEXT | NOT NULL |
| option_d | TEXT | NOT NULL |
| correct_option | VARCHAR(1) | NOT NULL |
| explanation | TEXT | NULL |
| marks | INTEGER | NOT NULL |

---

### quiz_attempts

Stores quiz attempts.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| quiz_id | UUID | Foreign Key → quizzes.id |
| user_id | UUID | Foreign Key → users.id |
| score | INTEGER | NOT NULL |
| total_marks | INTEGER | NOT NULL |
| started_at | TIMESTAMP | NOT NULL |
| completed_at | TIMESTAMP | NULL |

---

### quiz_answers

Stores answers selected during quiz attempts.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| attempt_id | UUID | Foreign Key → quiz_attempts.id |
| question_id | UUID | Foreign Key → quiz_questions.id |
| selected_option | VARCHAR(1) | NOT NULL |
| is_correct | BOOLEAN | NOT NULL |

---

## 3. Relationship Summary

```text
users
 │
 ├──< conversations
 │       └──< messages
 │
 ├──< subjects
 │       ├──< documents
 │       │      └──< summaries
 │       │
 │       ├──< flashcards
 │       │
 │       └──< quizzes
 │              └──< quiz_questions
 │
 └──< quiz_attempts
         └──< quiz_answers