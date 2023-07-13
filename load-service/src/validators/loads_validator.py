#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

from enum import Enum
from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import constr


class ConnectorResponse(BaseModel):
    id: Optional[int] = Field(
        None, description="The Connector object entity ID."
    )  # noqa
    jdbc_url: str = Field(..., description="The jdbc_url of this connector.")
    user: constr(min_length=1, max_length=256) = Field(
        ..., description="The username of this connector."
    )
    connection_properties: Optional[str] = Field(
        None,
        description="The optional additional properties of this connector.",
    )


class FileInfoItem(BaseModel):
    file_path: constr(min_length=1) = Field(
        ..., description="relative path of the masked file."
    )
    file_metadata: Dict[str, str] = Field(
        ...,
        description="file metadata details like enclosure, "
        "delimiter and endOFRecord etc.",
    )


class LoadMetadatum(BaseModel):
    source_key: Dict[str, str] = Field(
        ...,
        description="object providing the information like schema_name, "
        "table_name or file_name of the source datasource",
    )
    file_info: List[FileInfoItem] = Field(
        ...,
        description="Array of multiple objects, each object providing"
        " the information like file path and file metadata.",
        max_items=10000,
        min_items=1,
    )


class Load(BaseModel):
    id: Optional[int] = None
    execution_id: int = Field(..., description="ID of the Execution model.")
    job_id: int = Field(..., description="ID of the registered Job model.")
    load_metadata: Optional[List[LoadMetadatum]] = Field(
        None,
        description="Array of multiple objects, each object providing"
        " the information like sourceKey and file_info.",
        max_items=1000,
        min_items=1,
    )


class PostLoad(BaseModel):
    execution_id: int = Field(..., description="ID of the Execution model.")


class Status(Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class DataInfoItem1(BaseModel):
    source_key: Dict[str, str] = Field(
        ...,
        description="object providing the information like schema_name,"
        " table_name "
        "or file_name of the source datasource",
    )
    rows_loaded: Optional[int] = Field(
        None, description="Total number of rows loaded to the database table."
    )
    masked_file_path: Optional[constr(min_length=1)] = Field(
        None, description="relative path of the target masked file."
    )
    status: Optional[Status] = Field(
        None, description="The status of the load process."
    )
    error: Optional[str] = Field(None, description="Error details.")


class Status1(Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class Status2(Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class ObjectDetail(BaseModel):
    type: Optional[str] = Field(
        None, description="Component type of Post Load Task Component Status."
    )
    total: Optional[int] = Field(
        None, description="Total components of all Post Load Task Components."
    )
    processed: Optional[int] = Field(
        None,
        description="Processed components of all Post Load Task Components.",
    )
    status: Optional[Status2] = Field(
        None, description="The status of the load process."
    )
    start_time: Optional[str] = Field(
        None, description="The time when the load process is started."
    )
    end_time: Optional[str] = Field(
        None,
        description="The time when the post load "
        "task component process is completed.",
    )
    error: Optional[str] = Field(None, description="Error details.")


class DataInfoItem2(BaseModel):
    table_set: Optional[List[str]] = Field(
        None,
        description="Array of multiple table set for post load task.",
        max_items=10000,
        min_items=1,
    )
    object_details: Optional[List[ObjectDetail]] = Field(
        None,
        description="Array of multiple post load task object details, "
        "each component providing the information "
        "like total and processed.",
        max_items=10000,
        min_items=1,
    )


class PostLoadResponse(BaseModel):
    id: Optional[int] = None
    execution_id: Optional[int] = Field(
        None, description="Post Load Response model."
    )  # noqa
    status: Status1 = Field(
        ..., description="The status of the post load process."
    )  # noqa
    start_time: str = Field(
        ..., description="The time when the load process is started."
    )
    end_time: Optional[str] = Field(
        None,
        description="The time when the post load task"
        " component process is completed.",
    )
    data_info: Optional[List[DataInfoItem2]] = Field(
        None,
        description="Array of multiple table set with corresponding "
        "task object details for post load task.",
        max_items=10000,
        min_items=1,
    )
    error: Optional[str] = Field(None, description="Error details.")


class Status3(Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"


class ExecutionStatus(BaseModel):
    status: Status3 = Field(..., description="The status of the load process.")
    error: Optional[str] = Field(None, description="Optional, error detail.")


class ApiVersion(BaseModel):
    versionId: constr(min_length=1, max_length=50) = Field(
        ...,
        description="The VersionId is used to return "
        "the current version of service.",
    )


class Connector(ConnectorResponse):
    password: constr(min_length=1, max_length=256) = Field(
        ..., description="The password of this connector."
    )
    jdbc_url: str = Field(..., description="The jdbc_url of this connector.")
    user: constr(min_length=1, max_length=256) = Field(
        ..., description="The username of this connector."
    )


class LoadResponse(ExecutionStatus):
    execution_id: int = Field(..., description="ID of the Execution model.")
    job_id: int = Field(..., description="ID of the registered Job model.")
    start_time: Optional[str] = Field(
        None, description="The time when the load process is started."
    )
    end_time: Optional[str] = Field(
        None, description="The time when the load process is completed."
    )
    data_info: Optional[List[DataInfoItem1]] = Field(
        None,
        description="Array of multiple objects, each object providing "
        "the information like sourceKey and file_info.",
        max_items=10000,
        min_items=1,
    )
