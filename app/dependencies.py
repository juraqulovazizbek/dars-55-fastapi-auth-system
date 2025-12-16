from app.db import get_session


def get_db():
    return get_session()
