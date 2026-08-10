# AI Study Assistant — API Design

## 1. Base URL

All application endpoints use:

`/api/v1`

---

## 2. Authentication

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /auth/register | Create account |
| POST | /auth/login | Login |
| POST | /auth/logout | Logout |
| GET | /auth/me | Get current user |

Authentication uses secure HTTP cookies.

---

## 3. Users

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /users/me | Get current profile |
| PATCH | /users/me | Update profile |

---

## 4. Subjects

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /subjects | List subjects |
| POST | /subjects | Create subject |
| GET | /subjects/{subject_id} | Get subject |
| PATCH | /subjects/{subject_id} | Update subject |
| DELETE | /subjects/{subject_id} | Delete subject |

---

## 5. Conversations

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /conversations | List conversations |
| POST | /conversations | Create conversation |
| GET | /conversations/{conversation_id} | Get conversation |
| PATCH | /conversations/{conversation_id} | Rename conversation |
| DELETE | /conversations/{conversation_id} | Delete conversation |

---

## 6. AI Chat

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /conversations/{conversation_id}/messages | Send AI chat message |

The endpoint saves the user's message, sends the conversation context to the AI service, stores the AI response, and returns the response.

---

## 7. Messages

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /conversations/{conversation_id}/messages | Get messages |
| DELETE | /messages/{message_id} | Delete message |

---

## 8. Documents

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /documents | Upload PDF |
| GET | /documents | List documents |
| GET | /documents/{document_id} | Get document |
| DELETE | /documents/{document_id} | Delete document |

PDF uploads use `multipart/form-data`.

---

## 9. Summaries

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /documents/{document_id}/summarize | Generate summary |
| GET | /documents/{document_id}/summaries | List summaries |
| GET | /summaries/{summary_id} | Get summary |
| DELETE | /summaries/{summary_id} | Delete summary |

---

## 10. Flashcards

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /flashcards/generate | Generate flashcards |
| GET | /flashcards | List flashcards |
| GET | /flashcards/{flashcard_id} | Get flashcard |
| PATCH | /flashcards/{flashcard_id} | Update flashcard |
| DELETE | /flashcards/{flashcard_id} | Delete flashcard |

---

## 11. Quizzes

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /quizzes/generate | Generate quiz |
| GET | /quizzes | List quizzes |
| GET | /quizzes/{quiz_id} | Get quiz |
| DELETE | /quizzes/{quiz_id} | Delete quiz |
| POST | /quizzes/{quiz_id}/attempts | Submit quiz attempt |
| GET | /quizzes/{quiz_id}/attempts | Get quiz attempts |

---

## 12. Admin

Admin endpoints require administrator authorization.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /admin/users | List users |
| GET | /admin/users/{user_id} | View user |
| PATCH | /admin/users/{user_id} | Update user |
| DELETE | /admin/users/{user_id} | Disable/delete user |
| GET | /admin/statistics | System statistics |

---

## 13. HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 204 | Successful request with no response body |
| 400 | Bad request |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Resource not found |
| 409 | Conflict |
| 422 | Validation error |
| 500 | Internal server error |

---

## 14. Security

- Private endpoints require authentication.
- Admin endpoints require administrator authorization.
- Users can only access their own resources.
- Passwords are never returned by the API.
- AI API keys remain on the backend.
- Secrets are stored in environment variables.
- Uploaded files are validated.
- Request data is validated using Pydantic.

---

## 15. API Documentation

FastAPI will provide interactive API documentation during development:

- `/docs`
- `/redoc`