# coding: utf-8
#
# Copyright (c) 2023 by Delphix. All rights reserved.
#
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from src.db.connection import Base


class DataSet(Base):
    __tablename__ = "data_set"

    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)
