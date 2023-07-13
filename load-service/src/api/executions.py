#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from fastapi import APIRouter
from src.validators.executions_validator import ExecutionStatus
from src.validators.loads_validator import LoadResponse
from src.validators.loads_validator import PostLoadResponse
from starlette import status

router = APIRouter(
    prefix="/executions",
    tags=["Executions"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get(
    "/post-load/{execution_id}",
    response_model=PostLoadResponse,
    summary="Get the post load status of specific execution",
)
def get_post_load_execution_status(execution_id: int) -> PostLoadResponse:
    """
    Get the post load status of specific execution
    """
    pass


@router.delete(
    "/{execution_id}",
    response_model=None,
    summary="Cleanup the existing load execution.",
)
def clean_up_execution(execution_id: int) -> None:
    """
    Cleanup the existing load execution.
    """
    pass


@router.get(
    "/{execution_id}/status",
    response_model=LoadResponse,
    summary="Get status of specific execution",
)
def get_execution_status(execution_id: int) -> LoadResponse:
    """
    Get status of specific execution
    """
    pass


@router.put(
    "/{execution_id}/status",
    response_model=None,
    summary="Update status of existing execution.",
)
def update_execution_status(
    execution_id: int, body: ExecutionStatus = ...
) -> None:  # noqa
    """
    Update status of existing execution.
    """
    pass
