from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from itsdangerous import BadSignature, URLSafeTimedSerializer

from backend.app.core.config import settings


password_hasher = PasswordHasher()

cookie_serializer = URLSafeTimedSerializer(
    settings.SECRET_KEY,
    salt="ai-study-assistant-auth",
)


def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return password_hasher.verify(password_hash, password)
    except VerifyMismatchError:
        return False


def create_auth_token(user_id: str) -> str:
    return cookie_serializer.dumps({"user_id": user_id})


def verify_auth_token(token: str, max_age: int = 60 * 60 * 24 * 7):
    try:
        return cookie_serializer.loads(token, max_age=max_age)
    except BadSignature:
        return None