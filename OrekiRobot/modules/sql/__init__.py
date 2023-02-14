import sys

from OrekiRobot import DB_URI, LOGGER
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
try:
    SESSION: scoped_session = start()
except Exception as e:
    LOGGER.exception(f"PostgreSQL Failed to connect due to {e}")
    sys.exit()

LOGGER.info("PostgreSQL Connection successful, session started.")
