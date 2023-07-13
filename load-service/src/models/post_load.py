#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from src.db.connection import Base


class PostLoad(Base):
    __tablename__ = "post_load"

    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)
