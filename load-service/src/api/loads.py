#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel
from pydantic import Field
from src.validators.loads_validator import Load
from src.validators.loads_validator import LoadResponse
from src.validators.loads_validator import PostLoadResponse
from starlette import status

router = APIRouter(
    prefix="/loads",
    tags=["Loads"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post(
    "/load",
    response_model=None,
    summary="Load API to load the multiple files to a target database table.",
    responses={"201": {"model": LoadResponse}},
    tags=["Loads"],
)
def load(body: Load) -> Union[None, LoadResponse]:
    """
    Load API to load the multiple files to a target database table.
    """
    pass


class PostLoad(BaseModel):
    execution_id: int = Field(..., description="ID of the Execution model.")


@router.post(
    "/load/post-load",
    response_model=None,
    summary="Post load API to execute the post load processing.",
    responses={"201": {"model": PostLoadResponse}},
    tags=["Loads"],
)
def post_load(body: PostLoad) -> Union[None, PostLoadResponse]:
    """
    Post load API to execute the post load processing.
    """
    pass


@router.post(
    "/load/post-load/restart",
    response_model=None,
    summary="Post load API to retrigger the post load processing.",
    responses={"201": {"model": PostLoadResponse}},
    tags=["Loads"],
)
def restart_post_load(body: PostLoad) -> Union[None, PostLoadResponse]:
    """
    Post load API to retrigger the post load processing.
    """
    pass
