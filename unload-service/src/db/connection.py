#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import get_config

config = get_config()
SQLITE_DATABASE_URL = config["db"]["db_url"]

logger = logging.getLogger("app-logger")


# Construct database type and engine
engine = create_engine(
    url=SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,  # noqa
)

# Construct a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Construct a base class for declarative class definitions.
Base = declarative_base()


def get_db():
    """
    This function creates a database session,
    yield it to the get_db function, rollback the transaction
    if there's an exception and then finally closes the session.

    Yields:
        db: scoped database session
    """

    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()
