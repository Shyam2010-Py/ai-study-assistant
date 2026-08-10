from backend.app.db.session import engine
from backend.app.models.base import Base
from backend.app.models.user import User


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")