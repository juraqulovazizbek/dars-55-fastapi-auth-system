from sqlalchemy.orm import sessionmaker

from app.db.engine import engine

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    return db

    # try:
    #     yield db
    # except:
    #     db.close()
    