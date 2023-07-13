#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import List
from typing import Union

from fastapi import APIRouter
from fastapi import HTTPException
from src.services.connector_management_service import ConnectorService
from src.validators.connector_validator import ConnectorResponse
from src.validators.connector_validator import ConnectorValidator
from starlette import status

router = APIRouter(
    prefix="/connectors",
    tags=["ConnectorManagement"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post(
    "",
    response_model=None,
    responses={status.HTTP_201_CREATED: {"model": ConnectorResponse}},
    status_code=status.HTTP_201_CREATED,
)
async def create_connector(
    body: ConnectorValidator,
) -> Union[None, ConnectorResponse]:  # noqa
    """
    Create Connector.
    """
    resp = await ConnectorService.create_connector(body)
    if resp:
        return ConnectorResponse(**resp.__dict__)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Database Integrity Error",  # noqa
    )


@router.get(
    "",
    response_model=List[ConnectorResponse],
)
async def list_all_connector() -> List[ConnectorResponse]:
    """
    Returns a list of connectors.
    """
    connectors = await ConnectorService.get_all_connectors()
    return [ConnectorResponse(**i.__dict__) for i in connectors]


@router.get(
    "/{connector_id}",
    response_model=ConnectorResponse,
)
async def get_connector(connector_id: int) -> ConnectorResponse:
    """
    Get connector by id.
    """
    connector = await ConnectorService.get_connector_by_id(connector_id)
    if connector:
        return ConnectorResponse(**connector.__dict__)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Connector Not Found"
    )


@router.put(
    "/{connector_id}",
    response_model=ConnectorResponse,
)
async def update_connector(
    connector_id: int, body: ConnectorValidator
) -> ConnectorResponse:  # noqa
    """
    Update a Connector.
    """
    resp = await ConnectorService.update_connector(connector_id, body)
    if resp:
        return ConnectorResponse(**resp.__dict__)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Connector Not Found"
    )


@router.delete(
    "/{connector_id}",
    response_model=ConnectorResponse,
)
async def delete_connector(connector_id: int) -> None:
    """
    Remove a Connector.
    """
    connector = await ConnectorService.delete_connector_by_id(connector_id)
    if connector:
        return ConnectorResponse(**connector.__dict__)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Connector Not Found"
    )
