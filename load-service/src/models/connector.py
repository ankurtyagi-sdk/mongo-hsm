# coding: utf-8
#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from src.db.connection import Base


class Connector(Base):
    __tablename__ = "connector"

    id = Column(Integer, primary_key=True)
    user = Column(Text(25), nullable=False)
    password = Column(Text(25), nullable=False)
    jdbc_url = Column(Text, nullable=False)
    certificate_key_file = Column(Text)
    tls_ca_file = Column(Text)
    ssl = Column(Boolean, default=False)
