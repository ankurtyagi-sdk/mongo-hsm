#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from typing import List
from typing import Union

from fastapi import APIRouter
from fastapi import Path
from pydantic import conint
from src.validators.data_set_validator import DataSet
from src.validators.data_set_validator import DataSetMapping

router = APIRouter()


@router.post(
    "/data-sets",
    response_model=None,
    summary="Create a Data Set.",
    responses={"201": {"model": DataSet}},
    tags=["DataSets"],
)
def create_data_set(body: DataSet) -> Union[None, DataSet]:
    """
    Create DataSet.
    """
    pass


@router.get(
    "/data-sets",
    response_model=List[DataSet],
    summary="Returns a list of DataSets.",
    tags=["DataSets"],
)
def list_all_data_set() -> List[DataSet]:
    """
    Returns a list of DataSets.
    """
    pass


@router.get(
    "/data-sets/job/{jobId}/validate",
    response_model=None,
    summary="Validate the constraints of table in target dataset related with "
    "foriegn key constraints.",
    tags=["DataSets"],
)
def validate_data_set_by_job_id(
    job_id: conint(ge=1) = Path(..., alias="jobId")
) -> None:
    """
    Validate the constraints of table in target dataset related with
    foriegn key constraints.
    """
    pass


@router.get(
    "/data-sets/mapping",
    response_model=List[DataSetMapping],
    summary="Returns a list of DataSet Mappings.",
    tags=["DataSets"],
)
def list_all_data_set_mapping() -> List[DataSetMapping]:
    """
    Returns a list of DataSet Mappings.
    """
    pass


@router.post(
    "/data-sets/mapping",
    response_model=None,
    summary="DataSet Job mapping.",
    responses={"201": {"model": DataSetMapping}},
    tags=["DataSets"],
)
def create_mapping_data_set_job(
    body: DataSetMapping,
) -> Union[None, DataSetMapping]:  # noqa
    """
    DataSet Job mapping.
    """
    pass


@router.put(
    "/data-sets/mapping/{dataSetMappingId}",
    response_model=DataSetMapping,
    summary="Update an existing mapping of DataSet with Job.",
    tags=["DataSets"],
)
def update_mapping_data_set_job(
    data_set_mapping_id: conint(ge=1) = Path(..., alias="dataSetMappingId"),
    body: DataSetMapping = ...,
) -> DataSetMapping:
    """
    Update an existing mapping of DataSet with Job.
    """
    pass


@router.get(
    "/data-sets/{dataSetId}",
    response_model=DataSet,
    summary="get DataSet by ID.",
    tags=["DataSets"],
)
def get_data_set(
    data_set_id: conint(ge=1) = Path(..., alias="dataSetId")
) -> DataSet:  # noqa
    """
    get DataSet by ID.
    """
    pass


@router.put(
    "/data-sets/{dataSetId}",
    response_model=DataSet,
    summary="Update an existing DataSet.",
    tags=["DataSets"],
)
def update_data_set(
    data_set_id: conint(ge=1) = Path(..., alias="dataSetId"),
    body: DataSet = ...,  # noqa
) -> DataSet:
    """
    Update an existing DataSet.
    """
    pass


@router.delete(
    "/data-sets/{dataSetId}",
    response_model=None,
    summary="Delete an existing DataSet.",
    tags=["DataSets"],
)
def delete_data_set(
    data_set_id: conint(ge=1) = Path(..., alias="dataSetId")
) -> None:  # noqa
    """
    Delete an existing DataSet.
    """
    pass
