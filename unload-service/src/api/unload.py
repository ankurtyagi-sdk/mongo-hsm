#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import Union

from fastapi import APIRouter
from fastapi import Path
from pydantic import conint
from src.validators.unload_validator import ExecutionStatus
from src.validators.unload_validator import SourceData
from src.validators.unload_validator import Unload
from src.validators.unload_validator import UnloadResponse
from starlette import status

router = APIRouter(
    tags=["UnloadProcess"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post(
    "/unload",
    response_model=None,
    summary="Create a unload process to unload data to files from the source database.",  # noqa
    responses={status.HTTP_201_CREATED: {"model": UnloadResponse}},
)
def create_unload(body: Unload) -> Union[None, UnloadResponse]:
    """
    Create a unload process to unload data to files from the source database.
    """
    pass


@router.get(
    "/unload/status/{executionId}",
    response_model=UnloadResponse,
    summary="Returns a Unload status by execution ID.",
)
def get_unload_status_by_execution_id(
    execution_id: conint(ge=1) = Path(..., alias="executionId")
) -> UnloadResponse:
    """
    Returns a Unload status by execution ID.
    """
    pass


@router.put(
    "/unload/status/{executionId}",
    response_model=None,
    summary="Update status of existing execution.",
)
def update_execution_status(
    execution_id: conint(ge=1) = Path(..., alias="executionId"),
    body: ExecutionStatus = ...,
) -> None:
    """
    Update status of existing execution.
    """
    pass


@router.delete(
    "/executions/{executionId}",
    response_model=None,
    summary="Cleanup the existing unload execution.",
)
def clean_up_execution(
    execution_id: conint(ge=1) = Path(..., alias="executionId")
) -> None:
    """
    Cleanup the existing unload execution.
    """
    pass


@router.get(
    "/source-data/{executionId}",
    response_model=SourceData,
    summary="Returns the source data by execution ID.",
)
def get_source_data_by_execution_id(
    execution_id: conint(ge=1) = Path(..., alias="executionId")
) -> SourceData:
    """
    Returns the source data by execution ID.
    """
    pass
