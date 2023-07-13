#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import Union

from src.db.connector_repo import connector_repo
from src.models.connector import Connector
from src.validators.connector_validator import ConnectorValidator


class ConnectorService:
    """
    Business logic for different connector operations
    """

    @staticmethod
    async def get_all_connectors() -> list[Connector]:
        return await connector_repo.get_all()

    @staticmethod
    async def get_connector_by_id(connector_id) -> Union[None, Connector]:
        return await connector_repo.get_by_id(connector_id)

    @staticmethod
    async def delete_connector_by_id(connector_id) -> Union[None, Connector]:
        return await connector_repo.delete(connector_id)

    @staticmethod
    async def create_connector(
        body: ConnectorValidator,
    ) -> Union[None, Connector]:  # noqa
        response = await connector_repo.create(body.dict())
        return response

    @staticmethod
    async def update_connector(
        connector_id: str, body: ConnectorValidator
    ) -> Union[None, Connector]:  # noqa
        data = body.dict()
        data["id"] = connector_id
        response = await connector_repo.update(data)
        return response
