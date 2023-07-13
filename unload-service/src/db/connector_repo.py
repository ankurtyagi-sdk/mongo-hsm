#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.db.connection import get_db
from src.models.connector import Connector


class ConnectorRepository:
    """
    Connector repository class responsible for all
    DB operations related to connector
    """

    def __init__(self) -> None:
        self.db: Session = get_db().__next__()

    async def create(self, payload: dict):
        new_connector = Connector(**payload)
        try:
            self.db.add(new_connector)
            self.db.commit()
            self.db.refresh(new_connector)
            return new_connector
        except IntegrityError:
            self.db.rollback()

    async def get_by_id(self, _id: str):
        return (
            self.db.query(Connector).filter(Connector.id == _id).first()
        )  # noqa

    async def get_all(self):
        connectors = self.db.query(Connector).all()
        return connectors

    async def delete(self, _id: str):
        connector = self.db.query(Connector).filter_by(id=_id).first()
        if connector:
            self.db.delete(connector)
            self.db.commit()
            return connector
        return None

    async def update(self, payload: dict):
        updated_connector = Connector(**payload)
        existing_connector = (
            self.db.query(Connector).filter_by(id=payload["id"]).first()
        )
        if existing_connector:
            self.db.merge(updated_connector)
            self.db.commit()
            return updated_connector
        return None


connector_repo = ConnectorRepository()
